import sys
import os
sys.path.append(os.path.abspath("."))

from lib2to3.pgen2.pgen import generate_grammar
# import subprocess
from datetime import datetime
# import utils
# import  psutil
from webServices.wordGenerator import  Generator

searchEngine = ["google.com" , "brave.com" , "bing.com", 
                "cdn.connectad.io","kite.com" , "windows.com", "msn.com",
                "prebid.smilewanted.com", "ssum.casalemedia.com","googleads.g.doubleclick.net",
                ""] 

def excluded(url) -> bool:
        for u in searchEngine:
            if u in url:
                return True
        return False    

if __name__ == "__main__":
    # proc = subprocess.Popen(["dir", "/b"], stdout=subprocess.PIPE, shell=True)
    # (out, err) = proc.communicate()
    # print("program output:", out.decode().split("\r\n"))
   
    # nltk.download("all")
   
    # """Generator"""
    # genrator =  Generator()
    # genrator.generateWords({"movie", "action", "fantasy", "stremaing", "Netflix", "entertain"})
   
    # genrator.generateCSV("dict.csv")
    # print(genrator.words)
   
   
    # a = set(["psutil"])
    # Package.installPackages(a)
   

   
   
    # key_logger.start()
    # key_logger.listener.stop()
    # del(key_logger.listener);


    # subprocess.Popen("setx klaus 1", stdout=subprocess.PIPE, shell=True)
    # proc = subprocess.Popen("echo %klaus%", stdout=subprocess.PIPE, shell=True)
    # out, err = proc.communicate()
    # out = out.decode().split("\r\n")

    # print(out[0])
    # os_operation.setEnvironmentVariable("klaus", 2)
    # os.system(f"setx klaus \"\"")
    # value= os.environ['klaus']
    # print (value)
    
    
    # os_operation.clearVariables()
    # os_operation.addVariable("cindy", 2)
    # os_operation.addVariable("ciku", 2)
    # os_operation.deleteVariable("ciku")
    # dictionary = os_operation.loadVariables()
    # print(dictionary)


    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print (current_time)
    
    # """Web Scanner"""
    # for process in psutil.process_iter():
    #     if("python" in process.name()):
    #         # time = datetime.fromtimestamp(process.create_time()).strftime("%H:%M:%S")
    #         print(f"{process} , time ->{process.create_time()}")
    
    # utils.stopWebScanner()
    # p1 = subprocess.Popen("python stopKeyLogger.py")
    
    yes = excluded("https://prebid.smilewanted.com/")
    print (yes)

    
    
    