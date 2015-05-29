#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on May 29, 2015

@author: winson
'''
from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import sleep
from SeleniumTest.ex1.TestCase.public.login import login

class Page(object):
    login_url = 'www.xinzuji.com'
    
    def __init__(self, selenium_driver, base_url = login_url, parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.tabs = {}
    
    def _open(self, url):
        url = self.base_url + url
        self.driver(url)
        assert self.on_page(),'Did not land on %s'  %url
        
    def find_element (self, *loc):
        return self.driver.find_element(*loc)
    
    def open(self):
        return self._open(self.url)
    
    def on_page(self):
        return self.driver.current_url == (self.base_url +self.url )    
    
    def script(self, src):
        return self.driver.execute_script(src)
    
    def send_keys(self, loc, value, clear_first = True , click_first = True):
        try:
            loc = getattr(self, '_%s' %loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" loccator ' %(self, loc)
    
            
        