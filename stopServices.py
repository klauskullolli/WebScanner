import sys
import os
sys.path.append(os.path.abspath("."))

from webServices.sysprox import Proxy
import psutil
from webServices.configuration import Configuration
import yaml
if __name__ == '__main__':
    proxy = Proxy("127.0.0.1", 8080)
    proxy.cleanup()
    
    for process in psutil.process_iter():
        if("mitmproxy" in process.name()):
            print(f"{process} -> {process.create_time()}")
            process.terminate()
    
    stream  = open(Configuration.CONFIG_RESOURCES ,"r")
    yamlData = yaml.safe_load(stream)
    stream.close()
    
    yamlData["webScanner"] = False
    yamlData["keylogger"] = False
    yamlData["mproxy"] = False
    stream  = open(Configuration.CONFIG_RESOURCES ,"w")
    stream.write(yaml.dump(yamlData))
    stream.close()
    
            
    for process in psutil.process_iter():
        if("python" in process.name()):
            print(f"{process} -> {process.create_time()}")
            process.terminate()

   
    