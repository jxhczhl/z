import requests
class test:
    def __init__(self):
        print("初始化")

    def getHtmlText(self,url):
        try:
            html=requests.get(url).text
        except:
            return None

