#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年5月27日

@author: winson
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import poplib

#
SmtpServer = 'smtp.exmail.qq.com'
PopServer = ' pop.exmail.qq.com'
Sender = 'huasheng.huang@xinzuji.com'
uName='huasheng.huang@xinzuji.com'
passWD='504248573a'


#
# Receiver = 'huasheng.huang@xinzuji.com'
Receiver = 'haohui.wang@xinzuji.com'
Subject = 'Python Email test'
msg = MIMEText('<html><h1>你好！</h1></html>', 'html' , 'utf-8')
msg['Subject'] = Header(Subject, 'utf-8')

#send
def send_mail():
    try:
        smtp = smtplib.SMTP()
        smtp.connect(SmtpServer)
        smtp.login(uName, passWD)
        smtp.sendmail(Sender, Receiver, msg.as_string())
        smtp.quit()
    except Exception, e:
        print e

send_mail()
# error
# def accpet_mail():
#     try:
#         pop = poplib.POP3()
#         pop.connect(PopServer)
#         pop.login(uName,passWD)
#         ret = pop.start()
#         print ret
#         
#         for i in range(1,ret[0]+1):
#             mlist = pop.top(i, 0)
#             print 'line:' ,len(mlist[1]) 
#         ret = pop.list()
#         print ret
#         down = pop.retr(1)
#         print 'lines:',len(down)
#         
#         for line in down[1]:
#             print line
#         pop.quit()
#     
#     except Exception,e:
#         print e
#         
# 
# accpet_mail()