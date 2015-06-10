#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on May 29, 2015

@author: winson
'''
from selenium import webdriver
from time import sleep

def searchkw(key):
    dr = webdriver.Firefox()
    dr.get(" http://www.baidu.com")
    dr.implicitly_wait(10)
    dr.find_element_by_id("kw").clear()
    dr.find_element_by_id("kw").send_keys(key)
    dr.find_element_by_id("su").click()
    dr.implicitly_wait(10)
    
    dr.find_element_by_xpath(".//*[@id='1']/h3/a").click()
    dr.implicitly_wait(10)
    dr.quit()
    
for i in range(10):
    
    searchkw(u"新足迹")
    print i





# Login Baidu
def login(self):
    dr = self
    dr.find_element_by_link_text("登录").click()
    dr.implicitly_wait(10)
    dr.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("shengsing")
    dr.find_element_by_id("TANGRAM__PSP_8__password").send_keys("504248573a")
    dr.find_element_by_id("TANGRAM__PSP_8__submit").click()
    dr.implicitly_wait(10)
    


# 
# #qzonje
# dr.get(" http://qzone.qq.com")
# dr.implicitly_wait(10)
# dr.switch_to_frame("login_frame")
# dr.find_element_by_id("switcher_plogin").click()
# dr.find_element_by_id("u").send_keys("xxxxxxxxxx")
# dr.find_element_by_id("p").send_keys("xxxxxxxxxx")
# dr.find_element_by_id("login_button").click()
# dr.switch_to_default_content()
# dr.quit()