# -*- coding: utf-8 -*-

def login(self,uname,psd):
    driver = self.driver
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys(uname)
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys(psd)
    driver.find_element_by_id("loginBtn").click()

def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u'退出').click()