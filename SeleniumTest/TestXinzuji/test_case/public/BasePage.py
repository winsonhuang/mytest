#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on May 29, 2015

@author: winson
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod


class BasePage(object):
   
    
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        
    @abstractmethod
    def _verify_page(self):
        return
    
    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == locatorMode.ID:
            element = WebDriverWait (self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.ID, Locator)))
        elif locatorMode == locatorMode.ID:
            element = WebDriverWait (self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.NAME, Locator)))
        elif locatorMode == locatorMode.ID:
            element = WebDriverWait (self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.XPATH, Locator)))
        elif locatorMode == locatorMode.ID:
            element = WebDriverWait (self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
        else:
                raise Exception("Unsupported locator strategy. ")
        return element
    
    def wait_until_element_clickable(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == locatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.ID, Locator)))
        elif  locatorMode == locatorMode.Name:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.NAME, Locator)))
        elif  locatorMode == locatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.XPATH, Locator)))
        elif  locatorMode == locatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locator)))
        else:
             raise Exception("Unsupported locator strategy. ")
        return element
        
        
        def fill_out_field(self, locatorMode, Locator, text):
            self.find_element(locatorMode, Locator).clear()
            self.find_element(locatorMode, Locator).send_keys(text)
            
        def click(self, waitTime, locatorMode, Locator):
            self.wait_until_element_clickable(waitTime, locatorMode, Locator).click()
            

class IncorrectPageException(Exception):
     """
     This exception is raised when we try to instantiate the wrong page.
     """

            