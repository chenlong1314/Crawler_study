#coding:utf-8

import requests

url="http://www.ip138.com/ips138.asp?ip="

try:
    r=requests.get(url+'112.121.132.122')
    r.encoding=r.apparent_encoding
    print r.text
except:
    print 'errer'