import sys
import os
sys.path.append(os.path.abspath("."))

from webServices.configuration import Configuration
import yaml

if __name__ == "__main__":
    
    stream = open(Configuration.CONFIG_RESOURCES, "r")
    loadData = yaml.safe_load(stream)
    stream.close()
    con  = Configuration()
    con.updateDockerFile()
    
    loadData["docker"] = True
    stream = open(Configuration.CONFIG_RESOURCES, "w")
    stream.write(yaml.dump(loadData))
    stream.close()
    