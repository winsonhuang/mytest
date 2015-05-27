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
        self.driver.implicitly_wait(5)
        self.base_url = 'http://www.local.xinzuji.com/login/index'
        self.verificationErrors = []

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#     def test_null(self):
#         login.keyadd(self, 'null')
# 
#     def test_null_psd(self):
#         login.keyadd(self, 'null_psd')
# 
#     def test_null_uname(self):
#         login.keyadd(self, 'null_uname')
# 
#     def test_err(self):
#         login.keyadd(self, 'err')
#      
    def test_nomal(self):
        login.keyadd(self,'nomal')
        login.logout(self)
        
        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()