# encoding: utf-8
'''
Created on 2015年5月20日

@author: Huang
'''
import unittest

from test_case import test_login


suite = unittest.TestSuite
#suite.addTest(testadd.Testadd(""))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite)