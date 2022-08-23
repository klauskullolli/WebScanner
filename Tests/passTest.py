import sys
import os
sys.path.append(os.path.abspath("."))
import math 
import base64
from webServices import configuration
import  subprocess

if __name__ == '__main__':
    # conf  = configuration.Configuration()
    # conf.createConfigDirsAndFiles()
    # conf.updateDockerFile()
    
    # f = open(configuration.Configuration.LOGIN_CREDENTIALS, "r")
    # for line in f.readlines():
    #     print (base64.b64decode(line.strip().encode()).decode())
    # # print(os.path.abspath("./resources/config.yml"))
    # # open('C:/Users/User/Desktop/resources/config.yml', "r")
    # print (math.ceil(2.0/2))
    
    container = "test"
    p = subprocess.run("docker port webscanner" , capture_output=True)
    # out = p.stdout.decode()
    # if out == f"Error: No such container: {container} ": 
    #     print(out)
      
    print(configuration.Configuration.ceckContainerRunning())
    pass 