#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月27日

@author: winson
'''

from selenium import webdriver
import unittest


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
        
    def test_baiduH(self):
        u' 百度搜索H'
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element("id", "kw").send_keys("H")
        driver.find_element("id", "su").click()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.vErrors)
