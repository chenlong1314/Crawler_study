# --*-- coding:utf-8 --*--
# author: leif
# 淘宝商品信息抓取
import re
import requests

def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html)
        num = re.findall(r'\"view_sales\"\:\"[\d\.]*人付款\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])     # eval 去除双引号，  split 用 ： 作为分割，取后半部
            title = eval(tlt[i].split(':')[1])
            number = eval(num[i].split(':')[1])
            ilt.append([price,number,title])
    except:
        print("")

def printInfo(ilt):
    tplp = "{:4}\t{:8}\t{:8}\t{:18}"
    print(tplp.format("序号","价格","付款数","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplp.format(count, g[0], g[1], g[2]))

def main():
    goods="裙子"
    depth=2
    start_url='https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url=start_url + '&s=' + str(44*i)
            html = getHtml(url)
            parsePage(infoList,html)
        except:
            continue
    printInfo(infoList)

main()


