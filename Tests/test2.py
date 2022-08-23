import psutil
from datetime import datetime


def getDictionaryWords() -> list:
    words = []
    with open("dict.csv") as file: 
        file.readline()
        while True:
            data = file.readline()
            if not data : break 
            word = data.split(";")[0]
            words.append(word)
    return words

if __name__== "__main__":
    
    """Proccessors"""
    for process in psutil.process_iter():
        if("python" in process.name()):
           
            print(f"{process} -> {process.create_time()}")
    #         process.terminate()

    # # process = psutil.Process(10256)
    # # process.terminate()
    # key_logger.stop()
    # prccess = subprocess.Popen("python test.py",  shell=True)
    # print (proccess.pid)
    
    # print(getDictionaryWords())