import requests
import re
class test:
    def __init__(self):
        print("初始化jxhczzz")

    def getHtmlText(self,url):
        try:
            html=requests.get(url).text
        except:
            return None
    def resultList(self,html):
        for a in html:
            print(a)

a=test()
html=a.getHtmlText("http://www.baidu.com")
resultlist=re.findAll(r'\d{3}-\d{7,8}(-\d{\d}?)')
reslt=a.resultList(resultlist)

