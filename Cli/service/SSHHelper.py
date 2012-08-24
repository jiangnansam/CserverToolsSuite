'''
Created on 2012-8-23

@author: qjwang2
'''
import paramiko
import re

class SSHHelper(object):
    '''
    classdocs
    '''
    pingrespattern = re.compile('from (.+?) \((.*?)\)')
    
    def __init__(self, env):
        '''
        Constructor
        '''
        self.env = env

    def loginSSH(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.env.server, username=self.env.username, password=self.env.password)
        self.client = client
    
    def logoutSSH(self):
        return self.client.close()
        
    def executeComand(self, commandstr):
        stdin,stdout,stderr = self.client.exec_command(commandstr)
        return stdout
    
    def pingDNS(self, dnsName):
        stdout = self.executeComand('ping -c 1 %s' % dnsName)
        pingstr = stdout.read()
        matchGroup = re.search(self.pingrespattern, pingstr)
        if(matchGroup):
            return matchGroup.group(2)
        return ''