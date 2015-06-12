#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年5月27日

@author: winson
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
import HTMLTestRunner
import time,os
import ConfigParser
from email.header import Header


def send_mail(file_new):
     
    #item
    SmtpServer = cp.get("baseconf", "SmtpServer")
    PopServer = cp.get("baseconf", "PopServer")
    Sender = cp.get("baseconf", "Sender")
    uName = cp.get("baseconf", "uName")
    passWd = cp.get("baseconf", "passWd")
    
    Receiver = 'yulong.ding@xinzuji.com@xinzuji.com'   
#    Receiver = 'haohui.wang@xinzuji.com@xinzuji.com'   
#  Receiver = 'huasheng.huang@xinzuji.com'
    Subject = u'Python Selenium自动化测试报告'


   
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = Header (Subject, 'utf-8')
    msgRoot['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msgRoot['To'] = Receiver
    msgRoot['From'] = Sender
    
    
    # add HTML
    body  = MIMEText(open (file_new, 'rb').read(),'html' , 'utf-8')
    msgRoot.attach(body)
    
    # add att
    att = MIMEText(open('%s'%file_new, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"'%file_new
    msgRoot.attach(att)
    
    # struct email
    smtp = smtplib.SMTP()
    smtp.connect(SmtpServer)
    smtp.login(uName, passWd)
    smtp.sendmail(Sender, Receiver, msgRoot.as_string())
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
    print filename
    fp = file(filename, 'w')
    runner = HTMLTestRunner.HTMLTestRunner(
                                           stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况：')
    alltestnames = createSuite()
    runner.run(alltestnames)
    fp.close()
    
if __name__ == '__main__':
    cp = ConfigParser.ConfigParser()
    cp.readfp(open(r'D:\test\test_object\data.ini'))
    test_dir = cp.get("windows", "ConfRoot")
    testreport= cp.get("windows", "ReportRoot")
    createTestReport(testreport)
    send_report(testreport)