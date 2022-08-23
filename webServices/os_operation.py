import sys
import os
sys.path.append(os.path.abspath("."))


import logging
import platform
from webServices.configuration import Configuration
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
logger = logging.getLogger()

FILE = "env.csv"
FILE = Configuration.ENVIRONMENT_FILE
DELIMITER = ";"
HEADER = "key;value"


def setEnvironmentVariable(name: str, value: str) -> None:
    system = platform.system().lower()
    if system == "windows":
        logger.info("Windows  operating system")
        try:
            success=os.system(f"setx {name} {value}")
            if success != 0:
                raise Exception("Wrong command")
            logger.info(f"{name} variable set successfully")
        except:
            logger.error(f"{name} variable not set successfully")
    elif system == "linux":
        logger.info("Linux operating system")
        try:
            success = os.system(f"EXPORT {name}=\"{value}\"")
            if success != 0:
                raise Exception("Wrong command")
            logger.info(f"{name} variable set successfully")
        except:
            logger.error(f"{name} variable not set successfully")
    else:
        logger.error("Unknown operating system")


def environmentVariableExist(name: str) -> bool:
    value = os.environ[name]
    if value == None: 
        return False
    else: 
        return True 
    
def removeEnvironmentVariable(name: str) -> None:
    
    value = os.environ[name]
    system = platform.system().lower()
    
    if system == "windows":
        logger.info("Windows  operating system")
        try:
            if value == None: 
                logger.warning(f"{name} does not exist")
                
            else:
                success = os.system(f"setx {name} \"\"")
                if success !=0 : 
                    raise Exception("Wrong command")
                logger.info(f"{name} variable removed successfully")
        except:
            logger.error(f"{name} variable not removed successfully")
    
    if system == "linux":
        logger.info("Linux operating system")
        try:
            if value == None: 
                logger.warning(f"{name} does not exist")
            
            else: 
                success = os.system(f"UNSET {name}")
                if success !=0 : 
                    raise Exception("Wrong command")
                logger.info(f"{name} variable removed successfully")
        except:
            logger.error(f"{name} variable not removed successfully")
    else:
        logger.error("Unknown operating system")


def loadVariables() -> dict:
    dictionary = {}
    try:
        with open(FILE) as file:
            file.readline()
            while True:
                data = file.readline().strip()
                
                if not data: break
                
                datalist = [ str(x).strip() for x in data.split(DELIMITER)]
                if len(datalist) >=2:
                    dictionary[datalist[0]] = datalist[1]    
                else :
                    raise Exception(f"Wrong data from file {FILE}")
            file.close()
    except IOError:
        logger.error(f"Error opening file: {FILE}")

    return dictionary

def saveVariables(dictionary: dict):
    try:
        with open(FILE , "w") as file:
            file.write(f"{HEADER}\n")
            for key in dictionary.keys():
                file.write(f"{key}{DELIMITER}{dictionary[key]}\n")
            file.close()
    except IOError:
         logger.error(f"Error opening file: {FILE}")


def clearVariables() -> None:
    
    try:
        with open(FILE , "w") as file:
            file.write(f"{HEADER}\n")
            file.close()
    except IOError:
         logger.error(f"Error opening file: {FILE}")
        
        


def addVariable(key , value):
    dictionary = loadVariables()
    
    exist = True if key in dictionary else False 
    
    dictionary[key] = value 
    
    try: 
        saveVariables(dictionary)
        
        if exist: 
            logger.info(f"{key} variable updated successfully") 
        else :
            logger.info(f"{key} variable added successfully") 
    except : 
        logger.error(f"{key} variable not added successfully") 
    
    
def deleteVariable(key: str) ->None:
    dictionary = loadVariables()
    if key in dictionary:
        del(dictionary[key])
        saveVariables(dictionary)
        logger.info(f"{key} variable removed successfully")  
    else:
        logger.warning(f"{key} variable does not exist")