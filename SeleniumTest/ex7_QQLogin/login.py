#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on May 29, 2015

@author: winson
'''
from selenium import webdriver
dr = webdriver.Firefox()
#baidu
dr.get(" http://www.baidu.com")
dr.implicitly_wait(10)
dr.find_element_by_link_text("登录").click()
dr.implicitly_wait(10)
dr.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("xxxxxx")
dr.find_element_by_id("TANGRAM__PSP_8__password").send_keys("xxxxxx")
dr.find_element_by_id("TANGRAM__PSP_8__submit").click()

#qzone
dr.get(" http://qzone.qq.com")
dr.implicitly_wait(10)
dr.switch_to_frame("login_frame")
dr.find_element_by_id("switcher_plogin").click()
dr.find_element_by_id("u").send_keys("xxxxxxxxxx")
dr.find_element_by_id("p").send_keys("xxxxxxxxxx")
dr.find_element_by_id("login_button").click()
dr.switch_to_default_content()
dr.quit()