'''
Created on 2012-8-20

@author: qjwang2
'''
from Cli.service import sshutil
from EnvManagement.db_utils import getAllEnvs

cli_file_path = '/usr/local/tnconfig/cli_client.properties'

def getCliInfo(env):
    ssh_client = sshutil.loginSSH(env);
    clidict = sshutil.catPropsFile(ssh_client, cli_file_path)    
    clidict['ServerIp'] = sshutil.pingDNS(ssh_client, clidict['Server'])
    sshutil.logoutSSH(ssh_client)
    return clidict

def getEnvList():
    return getAllEnvs()

def getCliInfoList(envList):
    cliInfoList = [getCliInfo(env) for env in envList]
    return cliInfoList
