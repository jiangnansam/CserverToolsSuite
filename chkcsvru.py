# coding=UTF-8
'''
Created on 2012-9-21

@author: Attis Wong
'''

import os
import re
import subprocess

'''
User Guide and Specification:
1.Only code in <block2> is for user to implement.
2.Implement your own checker object if necessary. And add your Checker to checkList with construction parameters you need.
3.When Implement you own checker. you need:
    1)contain it with a check method with empty parameter.
    2)return a Formatter object.
    3)the refinfo, actualinfo, and status could be provided in two ways. You may refer to SimpleSampleChecker and ComplexSampleChecker for details.
'''

#<block1>
#Common code do not need modify!!!
class Formatter(object):
    def __init__(self,desc,refinfo,status,actualinfo=None):
        self.desc = desc;
        self.refinfo = refinfo;
        self.actualinfo = actualinfo;
        self.status = status;

cplxtoken = '->'

print_gap = {'desc':len('desc'),'refinfo':len('refinfo'),'actualinfo':len('actualinfo'),'status':len('status')}

def setGap(formatter):
    print_gap['desc'] = max(len(formatter.desc),print_gap['desc'])
    
    if isinstance(formatter.refinfo, str):
        print_gap['refinfo'] = max(len(formatter.refinfo),print_gap['refinfo'])
        print_gap['actualinfo'] = max((formatter.actualinfo and len(formatter.actualinfo) or 0),print_gap['actualinfo'])
        print_gap['status'] = max(len(formatter.status),print_gap['status'])        

    if isinstance(formatter.refinfo, dict):
        for key,value in formatter.refinfo.items():
            print_gap['refinfo'] = max(len(key)+len(value)+len(cplxtoken),print_gap['refinfo'])
        if formatter.actualinfo is not None:
            for key,value in formatter.actualinfo.items():
                print_gap['actualinfo'] = max(len(key)+len(value)+len(cplxtoken),print_gap['actualinfo'])
        for item in formatter.status:
            print_gap['status'] = max(len(item),print_gap['status'])

def descStyleRule(currentline, alllines):
    return currentline == 0    

def printFormat(desc,refinfo,actualinfo,status,token=' ',gap=' '):
    if isinstance(refinfo, str):
        desc_space = print_gap['desc'] - len(desc)
        ref_space = print_gap['refinfo'] - len(refinfo)
        value_space = print_gap['actualinfo'] - ((actualinfo) and len(actualinfo) or 0) 
        result_space = print_gap['status'] - len(status)
        print (gap*4).join(['%s','%s','%s','%s']) % (desc + desc_space*token, 
                                                 refinfo + ref_space*token, 
                                                 (actualinfo and actualinfo or '') + value_space*token, 
                                                 status + result_space*token)
    elif isinstance(refinfo, dict):
        refinfotuple = refinfo.items()
        actualinfotuple = actualinfo.items()
        for i in range(len(refinfotuple)):
            if descStyleRule(i,len(refinfotuple)):
                printFormat(desc, refinfotuple[i][0]+cplxtoken+refinfotuple[i][1], actualinfotuple[i][0]+cplxtoken+actualinfotuple[i][1], status[i])
            else:
                printFormat('', refinfotuple[i][0]+cplxtoken+refinfotuple[i][1], actualinfotuple[i][0]+cplxtoken+actualinfotuple[i][1], status[i])

#<block2>
#Implement below, you should add your checker here.
#Sample checker, and you may implement your checker in this block
class SimpleSampleChecker(object):
    
    #Extra parameters you need could be provide to __init__ method
    def __init__(self,desc='Simple Checker'):
        self.desc = desc
    
    def check(self):
        return Formatter(self.desc,'refinfo','status','actualinfo')
    
class ComplexSampleChecker(object):
    
    def __init__(self, desc='Complex Checker'):
        self.desc = desc

    def check(self):
        refdict = {'checkitem1':'value1','checkitem2':'value2'}
        valuedict = {'checkitem1':'value1','checkitem2':'value2'}
        statuslist = ['statusa','statusb']
        return Formatter(self.desc,refdict,statuslist,valuedict)

class FolderExistenceChecker(object):
    
    def __init__(self, directory, desc='Folder Existence Checker'):
        self.desc = desc
        self.directory = directory
        
    def check(self):
        status = 'X'
        if os.path.isdir(self.directory):
            status = '√'
           
        return Formatter('Check Log Folder',self.directory,status)

class JavaVersionChecker(object):
    
    def __init__(self, refvalue, desc='Check java version'):
        self.desc = desc
        self.refvalue = refvalue
        
    def check(self):    
        javareg = re.compile('java version "(.+?)"')
        sp = subprocess.Popen(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ostring = sp.communicate()[1]
        matchGroup = re.search(javareg, ostring)
        if matchGroup:
            actualValue = matchGroup.group(1)
            if actualValue==self.refvalue:
                status = '√'
        
            else:
                status = 'X'
        else:
            status= '-'
        
        return Formatter(self.desc, self.refvalue, status, actualValue)        


checkList = [
             #SimpleSampleChecker(),
             #ComplexSampleChecker(),
             FolderExistenceChecker('/home/tnuser/logs/TeleNav60','Check Log Folder'),
             JavaVersionChecker('1.6.0_29')
             ]

#<block3>
#Print logic, do not touch.
formatterList = []

for checkItem in checkList:
    formatter = checkItem.check()
    formatterList.append(formatter)
    setGap(formatter)

print '\n'
print 'Check 7x CServer Deployment Configuration'
printFormat('', '', '', '', token='*', gap='*')
printFormat('desc', 'refinfo', 'actualinfo', 'status')
printFormat('', '', '', '', token='-', gap='-')
for formatter in formatterList:
    printFormat(formatter.desc, formatter.refinfo, formatter.actualinfo, formatter.status)


        