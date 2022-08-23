import sys
import os
sys.path.append(os.path.abspath("."))

from mitmproxy import http
from webServices.UrlMod import urlModifyer
from cache.redisCache import  RedisCache
from cache.webCacheStatus import  Status
import socket
from webServices.configuration import  Configuration

FILE = Configuration.MPROXY_LOG_FILE

class Counter:
    
    searchEngine = ["google.com" , "brave.com" , "bing.com", 
                "connectad.io","kite.com" , "windows.com", "msn.com",
                "smilewanted.com", "casalemedia.com","bttrack.com",
                "criteo.com","doubleclick.net","sync.richaudience.com"
                "pubmatic.com"] 
    
    
    
    def __init__(self):
        self.num = 0
        self.conf = Configuration()
        # open("mproxy.log", "w").close()
        open(FILE , "w").close()
        self.redisPort = self.conf.REDIS_PORT
        
    
    def excluded(self,url) -> bool:
        for u in self.searchEngine:
            if u in url:
                return True
        return False    
        
    def getBaseUrl(self, url) ->str:
        urlElements = url.split("/")
        return "/".join(urlElements[0:3])
    
    def sendUrl(self,file,url)->None:
            server_addr_port = ("127.0.0.1", self.conf.WEB_SCANNER_PORT)
   
            try:
                clinet = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                clinet.sendto(url.encode("utf-8"), server_addr_port)
                clinet.close()
                
                file.write(f"Url --> {url} sent successfully\n")
                
            except :
                file.write(f"Url --> {url} not sent successfully\n")
         
         
    
    def response(self, flow: http.HTTPFlow):

        # file = open("mproxy.log", "a+")
        file = open(FILE , "a+")
        response = flow.response
        
        visitedCache = RedisCache("visited", host="localhost", port =self.redisPort)
     
        decodeType = response.headers["content-type"].split(" ")[1].split("=")[1]
        content  = response.content.decode(decodeType)
        if not self.excluded(flow.request.pretty_url):
            if "text/html" in response.headers["content-type"] and content != '':
                if "</html>" in  content:
                    
                    file.write("url --> " + flow.request.pretty_url + "\n")
                    # file1.write("url --> " + flow.request.pretty_url + "\n")
                    
                    file.write(f"content-type --> {flow.response.headers['content-type']}\n")
                    # file1.write(f"content-type --> {flow.response.headers['content-type']}\n")
                    
                    baseUrl = self.getBaseUrl(flow.request.pretty_url)
                    
                    file.write(f"baseUrl --> {baseUrl}\n")
                    # file1.write(f"baseUrl --> {baseUrl}\n")
                    
                    self.sendUrl(file ,flow.request.pretty_url )
                    if visitedCache.keyExist(baseUrl) and visitedCache.get(baseUrl)==Status.BLOCKED:
                       
                        flow.response.content = b"""
                               <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Blocked Page</title>
                                </head>
                                <body>
                                
                                    <div style="text-align:center; border-width:5px;border-style:solid;border-color:
                                    red;margin-right: 10%;margin-left: 10%;margin-top:10%">
                                        <h1 style="color:red;text-align:center;text-transform:uppercase">This page can not be reached!</h1>
                                        <h1 style="color:red;text-align:center;text-transform:uppercase">Blocked for not allowed content!</h1>
                                    </div>
                                    
                                </body>
                                </html>"""
                                   
        file.close()
        
addons = [Counter()]