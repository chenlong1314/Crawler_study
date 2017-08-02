# --*--  encoding=utf-8  --*--

import requests as re

kv= {'wd':'python'}
r=re.get("https://www.baidu.com/s",params=kv)

print r.status_code

print len(r.text)
