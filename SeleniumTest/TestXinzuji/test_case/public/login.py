# -*- coding: utf-8 -*-

from xml.dom import minidom
from selenium.webdriver.common.action_chains import ActionChains
# dom = xml.dom.minidom .parse("..\\TestData\\login_data.xml")
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


dom = minidom.parse("/home/winson/git/mytest/SeleniumTest/TestXinzuji/test_data/login_data.xml")
root = dom.documentElement


def login(self, uName, psd):
    driver = self.driver
    driver.find_element_by_id("txtAccount").clear()
    driver.find_element_by_id("txtAccount").send_keys(uName)
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(psd)
    driver.find_element_by_id("btnLogin").click()


def keyadd(self, key):
    driver = self.driver
    driver.get(self.base_url)
    logins = root.getElementsByTagName(key)
    uName = logins[0].getAttribute('uName')
    passWd = logins[0].getAttribute('passWd')
    # prompt_info = logins[0].firstChild.data

    login(self, uName, passWd)

    # text = driver.find_element_by_xpath("//*[@id='txtErrorMessage']/p").text
    # text = driver.find_element_by_id('txtErrorMessage').text
    # self.assertEqual(text, prompt_info)


def logout(self):
    driver = self.driver
    driver.implicitly_wait(10)
    
    logtxt = driver.find_element_by_class_name('isLogin')
    # self.assertEqual(logtxt.text, '欢迎您\\n横村新技术开发区')
    #self.uname=u"横村新技术开发区"
    self.uName=unicode('横村新技术开发区' ,'utf-8')
    
    assert self.uName in logtxt.text
    
    
    chain = ActionChains(driver)
    a = driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[1]")
    chain.move_to_element(a).perform()
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/a[2]").click()

from xinzuji import Page
class LoginPage(Page):
   
    url = ''
   
    uName_loc = (By.ID, 'txtAccount')
    passWd_loc = (By.ID, 'txtPassword')
    submit_loc = (By.ID, 'btnLogin')
    
    def open(self):
        self._open(self.url)
        
    def type_uName(self, uName):
        self.find_element(*self.uName_loc).send_keys(uName)
    
    def type_passWd(self, passWd):
        self.find_element(*self.passWd_loc).send_keys(passWd)
      
    def type_submit(self):
        self.find_element(*self.submit_loc).click()
    

def test_user_login(driver,  uName, passWd):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_uName(uName)
    login_page.type_passWd(passWd)
    login_page.type_submit()
    sleep(3)
    
    assert(uName == 'shengsing@163.com'),u"用户名错误"
    