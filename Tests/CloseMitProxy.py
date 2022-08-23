import os
import subprocess
import psutil
import time 
if __name__ == "__main__":
    # os.system("taskkill /IM \"mitmproxy.exe\" /F")
    # os.system("taskkill /IM \"cmd.exe\" /F")
    
    # subprocess.Popen("taskkill /IM \"mitmproxy.exe\" /F")
    subprocess.Popen("mitmproxy -s mproxy.py")
    time.sleep(10)
    
    for process in psutil.process_iter():
        if("mitmproxy" in process.name()):
            print(f"{process} -> {process.create_time()}")
            process.terminate()
            

    