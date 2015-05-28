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
from email.header import Header

# def attachment(filename):
#     fd = file(filename,"rb")
#     mimetype,mimeencoding = mimetypes.guess_type(filename)
#     if mimeencoding or (mimetype is None):
#         mimetype = "application/octet-stream"
#     maintype,subtype = mimetype.split("/")
#     
#     if maintype == "text":
#         retval = MIMEText(fd.read(),_subtype = subtype)
#     else:
#         # 如果不是text
#         retval = MIMEBase(maintype,subtype)
#         retval.set_payload(fd.read())
#         Encoders.encode_base64(retval)
#     retval.add_header("Content-Disposition","attachment",filename = filename)
#     fd.close()
#     return retval


def send_mail(file_new):
    
    #item
    SmtpServer = 'smtp.exmail.qq.com'
    PopServer = ' pop.exmail.qq.com'
    Sender ='<huasheng.huang@xinzuji.com>'
    uName='huasheng.huang@xinzuji.com'
    passWd='504248573a'
    
    Receiver = 'yulong.ding@xinzuji.com@xinzuji.com'   
#    Receiver = 'haohui.wang@xinzuji.com@xinzuji.com'   
#  Receiver = 'huasheng.huang@xinzuji.com'
    Subject = u'Python Selenium自动化测试报告'


   
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = Header (Subject, 'utf-8')
    msgRoot['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msgRoot['To'] = Receiver
    msgRoot['From'] = Sender
    
    
        #open HTML
    body  = MIMEText(open (file_new, 'rb').read(),'html' , 'utf-8')
    msgRoot.attach(body)
    
    # att

    att = MIMEText(open('%s'%file_new, 'rb').read(), 'base64', 'utf-8')#添加附件
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