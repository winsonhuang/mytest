#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年5月27日

@author: winson
'''
# coding = utf- 8
import os
import time

k = 1
while k <2:
    now_time = time.strftime('%H_%M')
    if now_time == '21_00':
        print u'Start_run'
        os.chdir('')
        os.system('')
        print u'End'
        break
    else:
        time.sleep(10)
        print now_time
        