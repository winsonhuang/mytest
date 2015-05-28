#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月27日

@author: winson
'''

from selenium import webdriver
import unittest
import HTMLTestRunner
import time


class Baidu(unittest.TestCase):


    def setUp(self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.baidu.com"
        # verificationErrors
        self.vErrors = []
        
    def test_baiduSearch(self):
        u' 百度搜索HTML'
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element("id", "kw").send_keys("HTML")
        driver.find_element("id", "su").click()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.vErrors)


if __name__ == "__main__":
    #TestSuit
    testunit = unittest.TestSuite()
    
    testunit.addTest(Baidu("test_baiduSearch"))
    
    #getnow
    now = time.strftime("%y_%m_%d %H:%M:%S")
    
    filename = "/home/winson/test_object/report/result "+now+".html"
    # 'wb' 以二进制写模式打开
    f = file(filename, 'wb')
    
    runner = HTMLTestRunner.HTMLTestRunner(
                                           stream=f,
                                           title=u"百度搜索测试报告",
                                           description=u"用例执行情况：")
    
    runner.run(testunit)
    f.close()