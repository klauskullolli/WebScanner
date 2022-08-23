import sys
import os
sys.path.append(os.path.abspath("."))

import spacy
import socket
import logging
import threading
import time 
from webServices.UrlMod import urlModifyer
import webServices.os_operation as os_operation
from cache.redisCache import RedisCache
from cache.webCacheStatus import  Status
import webServices.utils as utils
import datetime
from webServices.configuration import  Configuration


loggerFile = "webScannerLogger.log"
loggerFile = Configuration.WEB_SCANNER_LOG_FILE

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')

file_handler = logging.FileHandler(loggerFile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)




localhost = "127.0.0.1"
try:
    port = int(sys.argv[1]) if sys.argv[1] is not None else Configuration.WEB_SCANNER_PORT
except:
    port = Configuration.WEB_SCANNER_PORT
bufferSize = 4096

nlp = spacy.load(Configuration.SPACY_FILE)
lock = threading.Lock()
DELIMITER = ";"

visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
statisticsCache  = RedisCache("statistics", host="localhost", port=Configuration.REDIS_PORT)

dictKeyWords = " ".join(utils.getDictionaryWords())

keyLoggerFile = "key_logger.log"
keyLoggerFile = Configuration.KEY_LOGGER_WEB_LOG



def keyLoggerFileAddLog(url: str) ->None:
    try:
        with open(keyLoggerFile , "a") as file:
            now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"{now} | {url}")
            file.close()
    except IOError:
         logger.error(f"Error opening file: {keyLoggerFile}")    
    


def clearFile(filename: str) ->None:
    try:
        with open(filename , "w") as file:
            file.close()
    except IOError:
         logger.error(f"Error opening file: {filename}")
        
    

def connectionHandle(lock, data, addr):
    logger.info(f"Receive data -> {data.decode('utf-8')} from address -> {addr}")
    varDictionary = os_operation.loadVariables()
    
    try:
        searchWord = varDictionary["search"]
    except:
        searchWord = ""
    
    with lock:
        url = data.decode('utf-8')
        
        logger.info(f"This url ->{url} is valid")
        urlMod = urlModifyer(url)
        baseURL = urlMod.getBaseUrl()
        
        visitUrl = ""
        
        if urlMod.isBaseUrlValid :
                visitUrl = baseURL
        else:
                visitUrl = url

        if not (visitedCache.keyExist(baseURL) or visitedCache.keyExist(url)):
            
            websiteKeyWords = " ".join(utils.findKeyWordsFromWebSite(url))
            similar = utils.checkKeysSimilarity(websiteKeyWords, dictKeyWords ,nlp)

            if similar:
                visitedCache.add(visitUrl, Status.BLOCKED)
                if utils.bestSimilarRatioWithURL(url=url, word=searchWord) >=0.7:
                    keyLoggerFileAddLog(url)
                
                
            else :
                visitedCache.add(visitUrl, Status.VISITED)   
                
            statisticsCache.add(visitUrl , 1) 
        
        else :
            times = int(statisticsCache.get(visitUrl)) + 1
            statisticsCache.add(visitUrl , times)
      


if __name__ == "__main__":
    try:
        clearFile(loggerFile)
        clearFile(keyLoggerFile)
        os_operation.addVariable("webScanner", time.time()-5)
        webScanner = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        webScanner.bind((localhost, port))

        logger.info(f"Server is listening at port -> {port} ......")
        
        
        
        while True:
            data, addr = webScanner.recvfrom(bufferSize)
            thread = threading.Thread(target=connectionHandle, args=(lock, data, addr)).start()



    except Exception as e:
        logger.error("Server did not start successfully")
        print(e)
