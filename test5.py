#coding:utf-8

import requests
import os

url="http://tb-video.bdstatic.com/tieba-smallvideo-spider/10987457_e8fd27fc591979796581735e51eced37.mp4"
root="pic/"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print 'sucess'
    else:
        print 'all been'
except:
    print 'error'