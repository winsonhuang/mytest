# -*- coding: utf-8 -*-
'''
Created on 2015年5月20日

@author: Huang
'''
# import sys
# sys.path.append("..")
# from SeleniumTest.ex1.TestCase.public import login

import unittest
from selenium import webdriver
from public import login


class test_Login(unittest.TestCase):
    def setUp(self):
        # self.profileDir = 'D:\\FirefoxProfile'
        # self.profile = webdriver.FirefoxProfile(self.profileDir)
        # self.driver = webdriver.Firefox(self.profile)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.local.xinzuji.com/login/index'

    def tearDown(self):
        self.driver.quit()

    def test_null(self):
        u'用户密码为空'
        login.keyadd(self, 'null')
  
    def test_null_psd(self):
        u'密码为空'
        login.keyadd(self, 'null_psd')
  
    def test_null_uname(self):
        u'用户名为空'
        login.keyadd(self, 'null_uname')
  
    def test_err(self):
        u'异常用户名密码'
        login.keyadd(self, 'err')
       
    def test_nomal(self):
        u'正常登录'
        login.keyadd(self,'nomal')
        login.logout(self)
        
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()