# -*- coding: utf-8 -*-

import xml.dom.minidom 
#dom = xml.dom.minidom .parse("..\\TestData\\login_data.xml")

dom = xml.dom.minidom .parse("../TestData/login_data.xml")
root = dom.documentElement

def login(self,uName,psd):
    driver = self.driver
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys(uName)
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys(psd)
    driver.find_element_by_id("loginBtn").click()

def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u'退出').click()
    
def keyadd(self,key):
    driver = self.driver
    driver.get(self.base_url)
    logins = root.getElementsByTagName(key)
    uName = logins[0].getAttribute('uName')
    psd = logins[0].getAttribute('psd')
    prompt_info = logins[0].firstChild.data
    
    login(self, uName, psd)
        
    text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
    self.assertEqual(text, prompt_info)