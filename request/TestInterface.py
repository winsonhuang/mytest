#coding=UTF-8

import requests
import re

#处理空格dict
def bulidDict(r):
    d={}
    temp=re.compile(r'\n')
    map(lambda x:d.setdefault(x.split(': ')[0], x.split(': ')[1]), temp.split(r))
    return d

rUrl='http://www.local.xinzuji.com/evaluate/getCommentApi'

rHeaders ='''Host: www.local.xinzuji.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://www.local.xinzuji.com/evaluate/
Content-Length: 399
Cookie: client_id=5085hguwy3thm3t0; home-visited=40; user_id=215; token_expire=3600; Hm_lvt_3c304c0c2bcc7f37fef1f7b49a6ef701=1430272379,1430359931,1430808290; session=sdn0y6v1; redirect=%2F
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache'''

rPayload='report%5Bmi_linguistic%5D=3.33&report%5Bmi_logical%5D=4.44&report%5Bmi_spatial%5D=6.67&report%5Bmi_bodily%5D=7.78&report%5Bmi_musical%5D=7.78&report%5Bmi_social%5D=3.33&report%5Bmi_interpersonal%5D=8.89&report%5Bmi_naturalist%5D=6.67&report%5Bgender%5D=2&report%5Bprovince%5D=%E5%B9%BF%E4%B8%9C&report%5Bcity%5D=%E5%B9%BF%E5%B7%9E&report%5Bbirthday%5D=2015-05-06&report%5Bgrade%5D=%E5%B0%8F%E4%BA%8Cmi_finish_time%5D=1431424896'

r = requests.get(rUrl,data = rPayload , headers = bulidDict(rHeaders))

print r.json()

