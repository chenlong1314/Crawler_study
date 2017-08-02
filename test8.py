#coding=utf-8
import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")

demo=r.text

soup=BeautifulSoup(demo,"html.parser")

print soup.head

print soup.head.contents

print soup.body.contents

print len(soup.body.contents)

print soup.body.contents[1]
print "父节点"
print soup.body.parent