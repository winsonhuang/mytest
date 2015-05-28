#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年5月27日

@author: winson
'''
import smtplib
from email.mime.text import MIMEText
import unittest
import HTMLTestRunner
import time,os
from email.header import Header


def send_mail(file_new):
    
    #item
    SmtpServer = 'smtp.exmail.qq.com'
    PopServer = ' pop.exmail.qq.com'
    Sender ='<huasheng.huang@xinzuji.com>'
    uName='huasheng.huang@xinzuji.com'
    passWD='504248573a'
    
#    Receiver = 'yulong.ding@xinzuji.com@xinzuji.com'   
    Receiver = 'huasheng.huang@xinzuji.com'
    Subject = u'Python Selenium自动化测试报告'

    #send
    f = open (file_new, 'rb')
    mail_body = f.read()
    f.close()
   
    msg = MIMEText(mail_body,'html' , 'utf-8')
    msg['Subject'] =Header (Subject, 'utf-8')
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    
    smtp = smtplib.SMTP()
    smtp.connect(SmtpServer)
    smtp.login(uName, passWD)
    smtp.sendmail(Sender, Receiver, msg.as_string())
    smtp.quit()


#find and send TestReport
def send_report(testreport):
    result_dir = testreport
    lists = os.listdir(result_dir)
    lists.sort(key = lambda fn:os.path.getmtime(result_dir+fn))
    print lists[-1]
    file_new = os.path.join(result_dir, lists[-1])
    print file_new
    send_mail(file_new)
    
def createSuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir = None)
    
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
    return testunit

def createTestReport(testreport):
    now = time.strftime(' %Y-%m-%d %H:%M:%S')
    filename = testreport+'result'+now+'.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                                           stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况：')
    alltestnames = createSuite()
    runner.run(alltestnames)
    fp.close()
    
if __name__ == '__main__':
    test_dir = 'test_case'
    testreport= '/home/winson/test_object/report/'
    
    createTestReport(testreport)
    send_report(testreport)