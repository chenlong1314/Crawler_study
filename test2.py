# --*--  encoding=utf-8  --*--



import requests

url="https://item.jd.com/1763028134.html"

try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()  #如果不是200，提示httpError
    print r.text[0:1000]
except:
    print "产生异常"

