#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on May 28, 2015

@author: winson
'''
import re
import urllib

checkURL=[]
checkList=[]
bugList=[]


    
def getUrls(url):
    
    opener=urllib.urlopen(url)
    urls=findList.finditer(opener.read())
    opener.close()
    
    for u in urls:
        u = u.groups()[0]
        if u not in checkList:
            checkList.append(u)
        else: 
            continue
        getUrls(url+u)
        

def opList(checkList):
    if checkList:
        for check in checkList:
            if '"' in check:
                checkList.remove(check)
            if check == ('logout/'):
                checkList.remove('logout/')
        checkList.insert(0,'')
        print 'CheckList ',len(checkList)
        print checkList
    if not checkList:
        print "CheckList is empty"


def getBugs(url,checkList):
    for val in checkList:
        newUrl=url+val
        m=re.compile(r'\?').search(newUrl)
        if m:
            newUrl=newUrl+'&_uid=215'
        else:
            newUrl=newUrl+'?_uid=215'
        check=urllib.urlopen(newUrl).read()
        match=findBug.search(check)
        if match:
            print 'ErrPHP: '+newUrl
            bugList.append(match)
    print 'ErrCount: ',len(bugList)
    print ''


def clearList():
    checkList=[]
    bugList=[]


checkURL.append('http://www.local.xinzuji.com/')
checkURL.append('http://m.local.xinzuji.com/')
checkURL.append('http://publish.local.xinzuji.com/')

findBug=re.compile(r'<h4>A PHP Error was encountered</h4>')
findList=re.compile(r'<a href="/(.+?)"')

print ''
for i in checkURL:
    print '-----------------------------BEGIN------------------------------'
    print 'Checking',i
    getUrls(i)
    opList(checkList)
    getBugs(i,checkList)
    clearList()
    print 'Checkover',i
    print '------------------------------END-------------------------------'
