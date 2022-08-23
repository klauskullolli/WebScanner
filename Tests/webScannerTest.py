import  spacy
import logging 
import webServices.utils as utils
from webServices.UrlMod import  urlModifyer
import threading
from cache.redisCache import RedisCache
from cache.webCacheStatus import  Status
import sys
import os
sys.path.append(os.path.abspath("."))

import  datetime 
import webServices.os_operation as os_operation

addr = "127.0.0.1"

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
logger = logging.getLogger()

nlp = spacy.load("en_core_web_lg")
lock = threading.Lock()
DELIMITER = ";"

visitedCache = RedisCache("visited", host="localhost", port=7002)
statisticsCache  = RedisCache("statistics", host="localhost", port=7002)

dictKeyWords = " ".join(utils.getDictionaryWords())

keyLoggerFile = "key_logger.log"


def keyLoggerFileAddLog(url: str) ->None:
    try:
        with open(keyLoggerFile , "a") as file:
            now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"{now} | {url}\n")
            file.close()
    except IOError:
         logger.error(f"Error opening file: {keyLoggerFile}")    
    


def connectionHandle(lock, data, addr):
    logger.info(f"Receive data -> {data.decode('utf-8')} from address -> {addr}")
    varDictionary = os_operation.loadVariables()
    
    try:
        searchWord = varDictionary["search"]
    except:
        searchWord = ""
    
    with lock:
        url = data.decode('utf-8')
        
        if urlModifyer.isValidWebsite(url):
        
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
        else:
            logger.error(f"This url  ->{url} is not valid")


if __name__ == "__main__":
    data  = "https://movies123.design/home/".encode('utf-8')
    
    thread = threading.Thread(target=connectionHandle,  args=(lock ,data, addr)).start()
    
    
  