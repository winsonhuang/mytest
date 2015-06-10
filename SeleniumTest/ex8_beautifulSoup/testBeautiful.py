# -*- coding: utf-8 -*-

'''
Created on 2015年6月9日下午7:01:26

@author: Huang
'''

import urllib
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/s'

values= {'wd':'baidu'}
encode_parm = urllib.urlencode(values)

full_url = url +'?' +encode_parm
response = urllib.urlopen(full_url)

soup = BeautifulSoup(response)
alinks = soup.find_all('baidu')
