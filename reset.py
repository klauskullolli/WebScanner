import sys
import os
sys.path.append(os.path.abspath("."))

from webServices.configuration import Configuration
import  yaml
import subprocess

if __name__ == '__main__':
    stream  = open(Configuration.CONFIG_RESOURCES ,"r")
    yamlData = yaml.safe_load(stream)
    stream.close()
    yamlData["config"] = False
    yamlData["webScanner"] = False
    yamlData["keylogger"] = False
    yamlData["mproxy"] = False
    yamlData["docker"] = False
   
    stream  = open(Configuration.CONFIG_RESOURCES ,"w")
    stream.write(yaml.dump(yamlData))
    stream.close()
    
    subprocess.Popen(f"docker rm {Configuration.REDIS_CONTAINER_NAME}")
    