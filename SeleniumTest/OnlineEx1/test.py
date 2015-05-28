#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月26日

@author: winson
'''
from selenium import webdriver
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


    def testLogin(self):
        self.driver.find_element_by_xpath("//*[@class='lb']").click()
        loginName = '15817311208'
        loginPsd = '123456'



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()