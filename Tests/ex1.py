# import os
# from sysprox import Proxy
import subprocess


# import multiprocessing
# import key_logger
# import spacy
# import pandas as pd
# import trafilatura
# from keybert import KeyBERT
import sys
import os
sys.path.append(os.path.abspath("."))


import webServices.utils as utils
import threading
import time
import multiprocessing
file_name = "main.py"



if __name__ == "__main__":
    # # os.system("deactivate.bat")
    # # os.system(f"mitmproxy -s {file_name}")
    # proxy = Proxy("127.0.0.1", port=8080)
    # # proxy.engage()
    # proxy.cleanup()
    # subprocess.Popen("python runKeyLogger.py", stdout=subprocess.PIPE, shell=True)
    # time.sleep(2)
    # process =subprocess.Popen("python stopKeyLogger.py", stdout=subprocess.PIPE, shell=True)
    # time.sleep(2)
    # process.kill()
    # proccess1 = multiprocessing.Process(target=subprocess.Popen("python test.py", stdout=subprocess.PIPE, shell=True))
    # proccess1.start()
    # proccess1.join()
    
    # proccess2 = multiprocessing.Process(rocess =subprocess.Popen("python test2.py", stdout=subprocess.PIPE, shell=True))
    # # proccess2.start()
    # proccess2.join()
    # nlp = spacy.load("en_core_web_lg")
    # doc1 = nlp("wolf")
    # doc2 = nlp("dog")
    # print(doc1.similarity(doc2))
    # set1 = nlp("check if two words are synonyms python using spacy")
    # set2 = nlp("how to find if 2 words are synonyms python using spacy")
    # mylist = [ (token1.similarity(token2)) for token1 in set1 for token2 in set2]
    # # print(set1.similarity(set2))
    # # df = pd.DataFrame(mylist)
    # # print(df.head())
    # print(mylist)
    # print(checkKeysSimilarity("check if two words are synonyms python using spacy how to find if 2 words are synonyms python using spacy"
    #                         , "In the following example, we have two loops. The outer for loop iterates the first four numbers using the range()" +
    #                         "function, and the inner for loop also iterates the first four numbers."+ 
    #                         "If the outer number and a current number of the inner loop are the same, then break the inner (nested) loop"))
    
    
    """key bert"""
    # url = 'https://www.justwatch.com/in/movies'
    
    # keywords = utils.findKeyWordsFromWebSite(url)
    
    # print(keywords)
    
    
    """Web Scanner"""

    
    utils.startWebScanner()
    p1 = subprocess.Popen("python runKeyLogger.py")
   
    # time.sleep(3)
    
    # utils.stopWebScanner()
    
    
    # thr1 = threading.Thread(target=utils.startWebScanner)
    # thr1.start()
    # thr1.join()
    # time.sleep(3)
    # thr2 = threading.Thread(target=utils.stopWebScanner)
    # thr2.start()
    # thr2.join()
    # p1 = multiprocessing.Process(target=utils.startWebScanner) 
    # p1.run()
    # time.sleep(2)
    # p = multiprocessing.Process(target=utils.stopWebScanner)
    # p.run()

    # print("hello")
    # time.sleep(2)
    # print("kl")

   
    
