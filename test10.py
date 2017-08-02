#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup

r=requests.get("http://888xxoo.com/vod/?1788.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
x=soup.find_all(string = re.compile("mp4"))
y=soup.find_all(string=".mp4")

print(y)
