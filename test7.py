import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")

demo=r.text

soup=BeautifulSoup(demo,"html.parser")

print (soup.title)

print (soup.a)

print (soup.p)

print (soup.a.attrs["href"])

#print soup.name


