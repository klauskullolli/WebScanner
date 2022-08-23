
import requests

class urlModifyer:

    def __init__(self, url: str):
        self.url = url

    def getBaseUrlName(self) -> str:
        urlElements = self.url.split("/")
        return urlElements[2]
    
   
    def getBaseUrl(self) ->str:
        urlElements = self.url.split("/")
        return "/".join(urlElements[0:3])



    def isBaseUrlValid(self) -> bool:
        try:
            response =  requests.get(self.getBaseUrl()) 
            return True
        except:
            return False


    @staticmethod
    def isValidWebsite(url: str) -> bool:
        try:
            response =  requests.get(url)
            
            if response is not None:
                return True
            else:
                False
        except :
            return False
        
        
    @staticmethod
    def hasHTMLContent(url: str) -> bool:
        response = requests.get(url)
        decodeType = response.headers["content-type"].split(" ")[1].split("=")[1]
        content  = response.content.decode(decodeType)
        if "text/html" in response.headers["content-type"] and content != '':
            if "</html>" in  content:
                return True 
            else :
                return False
        else:
            return False



if __name__ == "__main__":
    # url = "https://stackoverflow.com/questions/16778435/python-check-if-website-exists"
    # urlMod = urlModifyer(url)
    # print(urlMod.getBaseUrlName())
    # print(urlMod.getBaseUrl())
    # print(urlMod.isBaseUrlValid())
    # print(urlModifyer.isValidWebsite("https://stackoverflow.com/questions/16778435"))
    # response = urlModifyer.hasHTMLContent("https://www.google.com/search?q=check+if+a+given+request+has+blank+content++python&rlz=1C1GCEA_enAL976AL976&ei=IAfrYsqdMZ2-xc8P1-yEWA&ved=0ahUKEwjKrZHs66v5AhUdX_EDHVc2AQsQ4dUDCA0&uact=5&oq=check+if+a+given+request+has+blank+content++python&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABKBAhGGABQvDhY5GNg9WRoBHABeACAAV6IAZALkgECMTeYAQCgAQHIAQjAAQE&sclient=gws-wiz")
    # response = requests.get("https://www.google.com/search?q=check+if+a+given+request+has+blank+content++python&rlz=1C1GCEA_enAL976AL976&ei=IAfrYsqdMZ2-xc8P1-yEWA&ved=0ahUKEwjKrZHs66v5AhUdX_EDHVc2AQsQ4dUDCA0&uact=5&oq=check+if+a+given+request+has+blank+content++python&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABKBAhGGABQvDhY5GNg9WRoBHABeACAAV6IAZALkgECMTeYAQCgAQHIAQjAAQE&sclient=gws-wiz")
    # print(response.headers["content-type"])
    # print(response.headers["content-type"].split(" ")[1].split("=")[1])
    # print(("</html>" in response.content.decode("ISO-8859-1")))
    # print(response)
    urlmod = urlModifyer.isValidWebsite("https://www.youtube.com/watch?v=vjUqxTEu-P8")
    print(urlmod)