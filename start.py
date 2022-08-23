import sys
import os
sys.path.append(os.path.abspath("."))

from webServices.package import Package
from webServices.configuration import Configuration


packageSet  = set(Configuration.PACKAGE_LIST)

if __name__ == "__main__":
    
    Package.installPackages(packageSet)
    
    import yaml
    stream = open(Configuration.CONFIG_RESOURCES, "r")
    loadData = yaml.safe_load(stream)
    stream.close()
    
    if loadData["docker"]:
        
        if Configuration.ceckContainerRunning():
        
            if loadData["config"] : 
                import FE.login as login 
                login.start_up()
            else:
                import FE.configPage as configPage
                configPage.start()
        
        else :
            from tkinter import  messagebox
            messagebox.showerror("Error Message"  , "Run docker compose up inside project directory first")
    else:
        from tkinter import  messagebox
        messagebox.showerror("Error Message"  , "Run docker compose up inside project directory first")
        
        