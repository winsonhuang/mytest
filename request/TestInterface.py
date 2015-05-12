#coding=UTF-8

import requests
import re

#处理空格dict
def bulidDict(rheaders):
    d={}
    rheaders=re.compile(r'\n')
    map(lambda x:d.setdefault(x.split(': ')[0], x.split(': ')[1]), str.split(rheaders))
    return  dict

rUrl='www.local.xinzuji.com'

rHeaders ='''Host: www.local.xinzuji.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Cookie: client_id=5085hguwy3thm3t0; home-visited=38; user_id=215; token_expire=3600; Hm_lvt_3c304c0c2bcc7f37fef1f7b49a6ef701=1430272379,1430359931,1430808290; session=61ae9xr8
Connection: keep-alive
Cache-Control: max-age=0'''
rPayload=''

r = requests.post(rUrl,data = rPayload , headers = rHeaders)

