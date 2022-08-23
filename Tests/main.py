import sys
import os
sys.path.append(os.path.abspath("."))


import webServices.utils as utils
from webServices.sysprox import  Proxy 
from cache.redisCache import  RedisCache




# from mitmproxy import http
# from mitmproxy import ctx
# from bs4 import BeautifulSoup
# from cache.redisCache import  RedisCache

# class Counter:
    
    
    
#     def __init__(self):
#         self.num = 0
#         self.visitedCache = RedisCache("visited", host="localhost", port=7002)
#         self.statisticsCache = RedisCache("statistics", host="localhost", port=7002)
   
#     def response(self, flow: http.HTTPFlow):
#         flow.request.url
        
#         # print(flow.response.content.decode("ufc-8"))
#         # if "Content-Security-Policy" in flow.response.headers:
#         #     del flow.response.headers["Content-Security-Policy"]

#         f = open("text.txt", "a+")

#         # if 'text/html' in flow.response.headers["content-type"][0]:
#         # html = bs(flow.response.content)
#         # html_text = html.get_text()
#         # print(flow.response.text)
#         # f.write(flow.response.text)
#         flow.response.content = b"""<!DOCTYPE html>
#                         <html>
#                         <body>
                        
#                         <h2>Absolute URLs</h2>
#                         <p><a href="https://www.w3.org/">W3C</a></p>
#                         <p><a href="https://www.google.com/">Google</a></p>
                        
#                         <h2>Relative URLs</h2>
#                         <p>HTML Images</a></p>
#                         <p><a href="/css/default.asp">CSS Tutorial</a></p>
                        
#                         </body>
#                         </html>"""
#         html = bs(flow.response.content.decode("utf-8"), "html.parser")
#         if bool(html.find()):
#             f.write("url: " + flow.request.pretty_url + "\n")
#             f.write(html.get_text() + "\n")
#             # f = open("html_text.txt", "w")  # Creating html_text.txt File

#             # # for line in html_text:
#             #     f.write(line)
#         f.close()
# addons = [Counter()]

if __name__ == "__main__":
    proxy = Proxy("127.0.0.1", 8080)
    proxy.engage()
    # print(f"Path --> {os.path.dirname(__file__)}")
    
    # print(utils.findKeyWordsFromWebSite("https://www.w3schools.com/css/css_text_transformation.asp"))
    # utils.startMitmProxy()