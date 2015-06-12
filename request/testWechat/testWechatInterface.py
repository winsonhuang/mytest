# -*- coding: utf-8 -*-

'''
Created on 2015年6月11日下午5:39:30

@author: Huang
'''

import requests

APPID = 'wx26432920705737d3'
APPSECRET = 'c09b4fb9b7f0cd179d8228920b7433c3'
rUrl='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+APPID+'&secret='+APPSECRET

print rUrl

r = requests.get(rUrl)

print r.text
