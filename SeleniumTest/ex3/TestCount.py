#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月27日

@author: winson
'''
import unittest
from Count import Count

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testAdd(self):
        self.j = Count(2, 3)
        self.add = self.j.add()
        self.assertEqual(self.add,0)
        
    def testAdd1(self):
        self.j = Count(5, 5)
        self.add = self.j.add()
        self.assertEqual(self.add, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()