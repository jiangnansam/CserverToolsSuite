'''
Created on 2012-8-20

@author: qjwang2
'''
from Cli.service import sshutil
from EnvManagement.db_utils import getAllEnvs
import threading

cli_file_path = '/usr/local/tnconfig/cli_client.properties'

cacheLock = threading.RLock()

env_info_cache = []
cli_info_cache = []


def getCliInfo(env):
    ssh_client = sshutil.loginSSH(env);
    clidict = sshutil.catPropsFile(ssh_client, cli_file_path)    
    clidict['ServerIp'] = sshutil.pingDNS(ssh_client, clidict['Server'])
    sshutil.logoutSSH(ssh_client)
    return clidict

def getEnvList():
    cacheLock.acquire()
    global env_info_cache
    if(not env_info_cache):
        env_info_cache = getAllEnvs()
    cacheLock.release()
    return env_info_cache
    

def getCliInfoList(envList):
    cacheLock.acquire()
    global cli_info_cache
    if(not cli_info_cache):
        cli_info_cache = [getCliInfo(env) for env in envList]
        
    cacheLock.release()
    return cli_info_cache

def refreshCache():
    cacheLock.acquire()
    global env_info_cache
    global cli_info_cache
    env_info_cache = []
    cli_info_cache = []
    getEnvList()
    getCliInfoList(env_info_cache)
    cacheLock.release()
    
    
