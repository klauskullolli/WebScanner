import trafilatura
from keybert import KeyBERT
import subprocess
import logging
import webServices.os_operation as os_operation
import psutil
from cdifflib import CSequenceMatcher
from webServices.UrlMod import  urlModifyer
from webServices.configuration import Configuration
import time 

defaltPort = 3000
defaltPort = Configuration.WEB_SCANNER_PORT
DELIMITER = ";"

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
logger = logging.getLogger()

def checkKeysSimilarity(set1: str, set2: str, nlp) -> bool:
    set1Nlp = nlp(set1)
    set2Nlp = nlp(set2)

    for token1 in set1Nlp:
        for token2 in set2Nlp:
            try:
                if token1.similarity(token2) > 0.85:
                    return True
            except:
                continue
    return False


def findKeyWordsFromWebSite(url: str) -> set:
    downloaded = trafilatura.fetch_url(url)
    doc = trafilatura.extract(downloaded)
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(doc, diversity=0.7, top_n=20)
    keys = {str(x[0]) for x in keywords}

    return keys


def startWebScanner(port=None):
    if port is not None:
        try:
            port = int(port)
            process = subprocess.Popen(f"python webServices/webScanner.py {port}")
        except:
            logger.error(f"webScanner did not start successful on port {port}")
            raise Exception(f"webScanner did not start successful on port {port}")


    else:
        try :
            process = subprocess.Popen(f"python webServices/webScanner.py")
        except :
            logger.error(f"webScanner did not start successful on port {defaltPort}")
            raise Exception(f"webScanner did not start successful on port {defaltPort}")
    



def stopWebScanner():
    variables = os_operation.loadVariables()
    const = True
    if "webScanner" in variables:
        time = str(variables["webScanner"]).strip()
        for process in psutil.process_iter():
            process_time = process.create_time()
            if "python" in process.name() and process_time <= float(time) + 5 and process_time >= float(time) - 5:
                process.terminate()
                logging.info(f"Process -> {process} terminated successfully")
                const = False
                break
        if const:
            logging.error("Web Scanner has not started or is not terminated successfully")
            raise Exception("Web Scanner has not started or is not terminated successfully")
    else:
        logging.error("Web Scanner has not started")
        raise Exception("Web Scanner has not started")
        

def getDictionaryWords() -> set:
    words = set()
    with open(Configuration.NLP_FILE) as file: 
        file.readline()
        while True:
            data = file.readline()
            if not data : break 
            word = data.split(DELIMITER)[0]
            words.add(word)
    return words

# used to find edit distance ratio 
def similarWords(a:str, b:str) -> float:
    return CSequenceMatcher(None, a, b).ratio()

def bestSimilarRatioWithURL(url: str , word:str) -> float:
    urlMod = urlModifyer(url)
    urlName = urlMod.getBaseUrlName()
    urlParts = urlName.split(".")
    # print(urlParts)
    maxRatio = similarWords(word , urlParts[0])
    
    for part in urlParts[1::]:
        ratio = similarWords(part, word)
        if ratio > maxRatio :
            maxRatio = ratio 
    
    return maxRatio
    
    
def closeMitmProxy() -> None:
    for process in psutil.process_iter():
        if("mitmproxy" in process.name()):
            logging.info(f"{process} -> {process.create_time()}")
            process.terminate()
            logger.info(f"{process} termianted successfully")
            
def startMitmProxy() -> None: 
    try:
        subprocess.Popen("mitmproxy -s webServices/mproxy.py")
        time.sleep(5)
    except Exception as e: 
        logger.error(e)
        logger.error("Mitmproxy did not start successfully")   
        raise e  

def startKeyLogger():
    try:
        subprocess.Popen("python webServices/runKeyLogger.py")
        time.sleep(2)
    except Exception as e:
        logger.error(e)
        logger.error("Key Logger did not start successfully") 
        raise e 
        

def passDecoding(s:str)-> str:
    pass       