'''
Created on 2012-8-20

@author: qjwang2
'''
from Cli.service.SSHHelper import SSHHelper
from EnvManagement.db_utils import getAllEnvs

cli_file_path = '/usr/local/tnconfig/cli_client.properties'


def getCliInfoByEnv(env):
    sshHelper = SSHHelper(env)
    sshHelper.loginSSH()
    stdout = sshHelper.executeComand('cat %s' % cli_file_path)
    dictList = []
    for line in stdout:
        if(line):
            if(line.find('=')>-1):
                dictList.append(line.strip().split('='))
    
    clidict = dict(dictList)
    clidict['ServerIp'] = sshHelper.pingDNS(clidict['Server'])
    sshHelper.logoutSSH()
    return clidict

def getEnvList():
    return getAllEnvs()
    
def getCliInfoList(envList):
    cliInfoList = [getCliInfoByEnv(env) for env in envList]
    return cliInfoList
