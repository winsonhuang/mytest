# -*- coding: utf-8 -*-

from xml.dom import minidom
from selenium.webdriver.common.action_chains import ActionChains
# dom = xml.dom.minidom .parse("..\\TestData\\login_data.xml")
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from platform import uName

dom = minidom.parse("../TestData/login_data.xml")
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
    psd = logins[0].getAttribute('psd')
    # prompt_info = logins[0].firstChild.data

    login(self, uName, psd)

    # text = driver.find_element_by_xpath("//*[@id='txtErrorMessage']/p").text
    # text = driver.find_element_by_id('txtErrorMessage').text
    # self.assertEqual(text, prompt_info)


def logout(self):
    driver = self.driver
    driver.implicitly_wait(5)
    
    logtxt = driver.find_element_by_class_name('isLogin')
    
    # self.assertEqual(logtxt.text, '欢迎您\\n横村新技术开发区')
    self.uname=u"横村新技术开发区"
    # self.uName=unicode('横村新技术开发区' ,'utf-8')
    assert self.uname in logtxt.text
    
    
    chain = ActionChains(driver)
    a = driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[1]")
    chain.move_to_element(a).perform()
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/a[2]").click()
