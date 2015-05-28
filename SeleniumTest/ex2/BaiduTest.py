#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月27日

@author: winson
'''
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest

def is_element_prestent(self, how, what):   
    try:
        self.driver.find_element(by = how, value = what)
    except NoSuchElementException:
        return False
    return True
     
     
def is_alert_prestent(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException:
        return False
    return True
    
def closeAlert_and_getText(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True
        
        
class BaiduTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com/'
        self.verificationErrors = []
        self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


    def testBaidu(self):
        driver = self.driver
        driver.get(self.base_url)
#         driver.find_element_by_id('kw').clear()
#         driver.find_element_by_id('kw').send_keys('selenium')
#         driver.find_element_by_id('su').click()
        
        is_element_prestent(self, 'id', 'kw')
     
     
   
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()