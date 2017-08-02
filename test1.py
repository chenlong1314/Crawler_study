# --*--  encoding=utf-8  --*--
import requests


def getHtml(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()  #如果不是200，提示httpError
        r.encoding="utf-8"
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url="https://www.baidu.com"
    print (getHtml(url))
