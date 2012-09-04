# Create your views here.
from Cli.service import cli_service

from django.shortcuts import render_to_response
import collections

def lookupCliInfo(request,template):
    envList = cli_service.getEnvList()
    cliInfoList = cli_service.getCliInfoList(envList)    
    CliItem = collections.namedtuple('CliItem', 'environment_name,server,cli_server_ip')
    cli_items = []
    for i in range(len(envList)):
        p1 = envList[i].env_name
        p2 = envList[i].server
        p3 = cliInfoList[i]['ServerIp']
        cli_item = CliItem(environment_name=p1,server=p2,cli_server_ip=p3)
        cli_items.append(cli_item)

    return render_to_response(template,{'cli_items':cli_items});
    
    
    
    
