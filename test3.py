# --*--  encoding=utf-8  --*--
import requests as re
url="https://www.amazon.cn/dp/B01MQYAX33/ref=cngwdyfloorv2_recs_0/458-1136155-3886908?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=R4GS8BQYV5KXRDRS8Q9C&pf_rd_r=R4GS8BQYV5KXRDRS8Q9C&pf_rd_t=36701&pf_rd_p=1835a352-38d8-4bc6-b91e-35385247593d&pf_rd_p=1835a352-38d8-4bc6-b91e-35385247593d&pf_rd_i=desktop"

kv={'user-agent':'Mozilla/5.0'}
r=re.get(url,headers = kv)
r.encoding=r.apparent_encoding



print (r.text[1000:2000])
