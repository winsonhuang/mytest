# encoding: utf-8
'''
Created on 2015年5月20日

@author: Huang
'''


import unittest
from selenium import webdriver
import xml.dom.minidom as xdm
from public import login


dom = xdm.parse('..\\test_data\\login_data.xml')
root = dom.documentElement

class test_login(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors =[]


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)


    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('null')
        uname = logins[0].getAttribute('uname')
        psd = logins[0].getAttribute('psd')
        prompt_info = logins[0].firstChild.data
        
        login.login(self,uname, psd)
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text, prompt_info)
        
    def test_null_psd(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('null_psd')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()