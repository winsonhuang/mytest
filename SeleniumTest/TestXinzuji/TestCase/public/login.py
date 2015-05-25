# -*- coding: utf-8 -*-

from xml.dom import minidom
#dom = xml.dom.minidom .parse("..\\TestData\\login_data.xml")

dom = minidom.parse("../TestData/login_data.xml")
root = dom.documentElement

def login(self,uname,psd):
    driver = self.driver
    driver.find_element_by_id("txtAccount").clear()
    driver.find_element_by_id("txtAccount").send_keys(uname)
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(psd)
    driver.find_element_by_id("btnLogin").click()

def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u'退出').click()
    
def keyadd(self,key):
    driver = self.driver
    driver.get(self.base_url)
    logins = root.getElementsByTagName(key)
    uname = logins[0].getAttribute('uname')
    psd = logins[0].getAttribute('psd')
    prompt_info = logins[0].firstChild.data
    
    login(self, uname, psd)
        
    #text = driver.find_element_by_xpath("//*[@id='txtErrorMessage']/p").text
    text = driver.find_element_by_id('txtErrorMessage').text
    self.assertEqual(text, prompt_info)