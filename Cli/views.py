# Create your views here.
from Cli.service import cli_service

from django.shortcuts import render_to_response
import collections
import threading

viewlock = threading.RLock()
cli_items = []

def lookupCliInfo(request,template):
    global cli_items
    viewlock.acquire()
    if(cli_items):
        pass
    else:
        envList = cli_service.getEnvList()
        cliInfoList = cli_service.getCliInfoList(envList)
        
        CliItem = collections.namedtuple('CliItem', 'environment_name,server,cli_server_ip')
        
        for i in range(len(envList)):
            p1 = envList[i].env_name
            p2 = envList[i].server
            p3 = cliInfoList[i]['ServerIp']
            cli_item = CliItem(environment_name=p1,server=p2,cli_server_ip=p3)
            cli_items.append(cli_item)
    viewlock.release()
    return render_to_response(template,{'cli_items':cli_items});
    
    
    
    
