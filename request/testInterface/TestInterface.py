#coding=UTF-8

import requests
import re

#处理空格dict
def bulidDict(r):
    do={}
    temp=re.compile(r'\n')
    map(lambda x:do.setdefault(x.split(': ')[0], x.split(': ')[1]), temp.split(r))
    return do

def rGet(r):
    return r

def rPost(p,rUrl,data,headers):
    p = requests.post(rUrl,data = data, headers = headers)
    return p
