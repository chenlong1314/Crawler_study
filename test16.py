# --*-- coding:utf-8 --*--
import requests
from bs4 import BeautifulSoup
import re

headers = {'content-type': 'text/html','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
resp = requests.get('http://www.baidu.com/s?tn=mswin_oem_dg&ie=utf-16&word=ip', headers=headers)
html = resp.text
r = re.findall(r'ip地址[1-9].*\d',html)[0]

p=re.findall(r'\d.*',r)[0]


print(p)