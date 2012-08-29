'''
Created on 2012-8-23

@author: qjwang2
'''
import paramiko
import re

pingrespattern = re.compile('from (.+?) \((.*?)\)')

'''
cat file action for properties file
return dict object
'''
def catPropsFile(client, file_path, token='='):
    stdout = executeComand(client, 'cat %s' % file_path)
    dictList = [line.strip().split(token) for line in stdout if line if line.find(token)>-1]
    return dict(dictList)

'''
ping dns for machine name
return ip
'''
def pingDNS(client, dnsName):
    stdout = executeComand(client, 'ping -c 1 %s' % dnsName)
    pingstr = stdout.read()
    matchGroup = re.search(pingrespattern, pingstr)
    if(matchGroup):
        return matchGroup.group(2)
    return ''

'''
SSH login based on environment
return sshclient for subsequent usage
'''
def loginSSH(env):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=env.server, username=env.username, password=env.password)
    return client

'''
SSH logout in order to release connection resource
''' 
def logoutSSH(client):
    return client.close()

'''
common shell command execution api
'''
def executeComand(client, commandstr):
    stdin,stdout,stderr = client.exec_command(commandstr)
    return stdout
