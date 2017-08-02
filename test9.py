#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")

demo=r.text

soup=BeautifulSoup(demo,"html.parser")

t=soup.prettify()

x=re.findall('hello.*?',demo)

print (x)