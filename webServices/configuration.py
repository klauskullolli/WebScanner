import sys
import os
sys.path.append(os.path.abspath("."))

import logging
import  yaml
import  shutil
import  base64
import  subprocess


class Configuration:
    
    
    DOCKER_IMG = "webScanner-redis"

    BASE_PATH = "/".join(os.getcwd().split("\\")[0:3]) 
    BASE_DIR_PATH = BASE_PATH + "/.web-scanner"
    
    KEY_LOGGER_DIR = BASE_DIR_PATH + "/keyLogger"
    KEY_LOGGER_KEY_FILE = KEY_LOGGER_DIR + "/keylogger.csv"
    KEY_LOGGER_SEARCH_FILE = KEY_LOGGER_DIR + "/key_logger.csv"
    
    # Create log if only last search is similar to webside searched 
    KEY_LOGGER_WEB_LOG = KEY_LOGGER_DIR + "/key_logger.log"
    
    ENVIRONMENT_DIR = BASE_DIR_PATH + "/environment"
    ENVIRONMENT_FILE = ENVIRONMENT_DIR + "/env.csv"
    
    NLP_DIR = BASE_DIR_PATH + "/nlp"
    NLP_FILE = NLP_DIR + "/dict.csv"
    
    WEB_SCANNER_LOG_FILE = BASE_DIR_PATH + "/webScannerLogger.log"
    MPROXY_LOG_FILE = BASE_DIR_PATH + "/mproxy.log"
    
    LOGIN_CREDENTIALS = BASE_DIR_PATH + "/login.txt"

    PACKAGE_LIST = ["mitmproxy", "tk", "beautifulsoup4", "nltk", "pynput",
                    "trafilatura", "logging", "psutil",
                    "requests", "redis", "spacy", "pyyaml","pybase64", 
                    "pycopy-webbrowser", "cdifflib", "keybert", "matplotlib"]
    
    SPACY_FILE = "en_core_web_lg"
    
    WEB_SCANNER_PORT = 3000
    
    REDIS_PORT = 7002 
    
    USERNAME = "admin"
    
    PASSWORD = "admin"
    
    CONFIG_RESOURCES = os.path.abspath("./resources/config.yml")
    
    REDIS_CONTAINER_NAME = "webscanner"
    



    
    
    def updateDockerFile(self):
        logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
        logger = logging.getLogger()
        yamlData = {}
        with open("docker-compose.yml", "r") as stream:
            try:
                # print(yaml.safe_load(stream))
                yamlData = yaml.safe_load(stream)
                ports  = yamlData["services"]["redis"]["ports"]
                ports[0] = ":".join([str(self.REDIS_PORT), ports[0].split(":")[1]])
                stream.close()
            except yaml.YAMLError as exc:
                stream.close()
                logger.error(exc)
                
        with open("docker-compose.yml", "w") as stream:
            try:
                # print(yaml.safe_load(stream))
                yamlData["services"]["redis"]["container_name"] = Configuration.REDIS_CONTAINER_NAME
                stream.write(yaml.dump(yamlData))
                logger.info("docker-compose.yml updated successfully")
            except Exception as exc:
                stream.close()
                logger.error(exc)          
     
        
    def createConfigDirsAndFiles(self):
        
        if(os.path.exists(self.BASE_DIR_PATH)):
            shutil.rmtree(self.BASE_DIR_PATH)
            
        try: 
            os.mkdir(self.BASE_DIR_PATH)
            os.mkdir(self.KEY_LOGGER_DIR)
            os.mkdir(self.ENVIRONMENT_DIR)
            os.mkdir(self.NLP_DIR)
        except Exception as e:
            print(e)
            
        open(self.KEY_LOGGER_KEY_FILE, "w").close()
        open(self.KEY_LOGGER_WEB_LOG, "w").close()
        open(self.ENVIRONMENT_FILE, "w").close()
        open(self.NLP_FILE, "w").close()
        open(self.WEB_SCANNER_LOG_FILE, "w").close()
        open(self.MPROXY_LOG_FILE, "w").close()
        f = open(self.LOGIN_CREDENTIALS,"w")
        f.write(base64.b64encode(self.USERNAME.encode()).decode() + "\n")
        f.write(base64.b64encode(self.PASSWORD.encode()).decode())
        stream = open(self.CONFIG_RESOURCES, "r")
        yamlData = yaml.safe_load(stream)
        stream.close()
        
        yamlData["config"] = False
        
        stream = open(self.CONFIG_RESOURCES, "w")
        stream.write(yaml.dump(yamlData))
        stream.close()

    def ceckContainerRunning()-> bool:
        container = "webscanner"
        p = subprocess.run(f"docker port {container}" , capture_output=True)
        
        if p.stdout.decode() !="":
            return True
        else:
            return False 
        
    
