'''
Created on 2012-9-10

@author: Attis Wong
'''
import os

'''
How to run the script: run 'python chkcsvr.py' in command window.
How to add check item for check:
1)new a CheckItem with desc, ref, checker, value(optional) parameter.
2)choose a checker implementation, if not exist just implement yourself. 
 'msg' field could be overridden as what you like. checkRule method must be overridden to validate the rule.
3)when the check item need value to compare with reference value, the value parameter in init method should be 
 constructed outside and pass in when init the CheckItem object.
4)add the constructed check item to chk_items list.
'''


################################################################################################
##########used for init check item, value is not necessary if the not needed####################
################################################################################################
class CheckItem(object):
    
    def __init__(self, checker,desc, ref, value=''):
        self.desc = desc
        self.ref = ref
        self.value = value
        self.checker = checker
        
    def evaluate(self):
        self.result = self.checker.check(self.ref,self.value)
        return self


############################################Checker##############################################
##checker is a super interface for all checkers. once new rule's needed, you need implement it ##
##with subclass and you may rewrite the msg key value pairs as what you need, you also need    ##
##overwrite checkRule method with your check logic, and return True when validate success and  ##
##vice versa                                                                                   ##
#################################################################################################
class Checker(object):    
    
    msg = {'pass':'pass', 'fail':'fail'}
        
    def check(self, ref, value):
        if(self.checkRule(ref, value)):
            return self.msg['pass']
        else:
            return self.msg['fail']
    
    def checkRule(self, ref, value):
        return False

class FolderExistChecker(Checker):
   
    msg = {'pass':'exist', 'fail':'do not exist'}
   
    def checkRule(self, ref, value):
        return os.path.isdir(ref)
        
class ValueChecker(Checker):
    
    msg = {'pass':'match', 'fail':'mismatch'}
    
    def checkRule(self, ref, value):
        return ref == value       


print_gap = {'desc':len('desc'),'ref':len('ref'),'value':len('value'),'result':len('result')}

def setMaxPrintGap(chk_item):
    print_gap['desc'] = max(len(chk_item.desc),print_gap['desc'])
    print_gap['ref'] = max(len(chk_item.ref),print_gap['ref'])
    print_gap['value'] = max(len(chk_item.value),print_gap['value'])
    print_gap['result'] = max(len(chk_item.result),print_gap['result'])


########################################Check Items##############################################
##chk_items list defines all the check items need to be verified, check items should be new    ##
##with description of the check rule, reference value of the check item, and the concrete check##
##implementation of checker mandatory. the actual value of the items need be provided when     ##
##needed                                                                                       ##
#################################################################################################
chk_items = [
             CheckItem(desc='check log folder',ref='/home/tnuser/logs/TeleNav60',checker=FolderExistChecker()),
             #add CheckItem
             ]

for chk_item in chk_items:
    setMaxPrintGap(chk_item.evaluate())

def printFormat(desc,ref,value,result,token=' ',gap=' '):
    desc_space = print_gap['desc'] - len(desc)
    ref_space = print_gap['ref'] - len(ref)
    value_space = print_gap['value'] - len(value)
    result_space = print_gap['result'] - len(result)
    print (gap*4).join(['%s','%s','%s','%s']) % (desc + desc_space*token, 
                                                 ref + ref_space*token, 
                                                 value + value_space*token, 
                                                 result + result_space*token)

print '\n'
print 'Check 7x CServer Deployment Configuration'
printFormat('', '', '', '', token='*', gap='*')
printFormat('desc', 'ref', 'value', 'result')
printFormat('', '', '', '', token='-', gap='-')
for chk_item in chk_items:
    printFormat(chk_item.desc,chk_item.ref,chk_item.value,chk_item.result)
print '\n'
