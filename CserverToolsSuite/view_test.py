'''
Created on 2012-8-27

@author: kwwang
'''
from EnvManagement.models import environment
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


def list_env(request,template):
    env_list=[environment(id=111,env_name='dev_fp',server='172.16.10.101',username="tnuser",password="tndev",tomcat_path="/home/tnuser/tomcat",zipfolder_path="/home/tnuser/zipfolder",service_locator_path="/home/tnuser/servicelocator")]
    return render_to_response(template,{'env_list':env_list})

def new_env(request,template):
    return render_to_response(template)
@csrf_exempt
def save_env(request,template):
    print request.POST.get("password")
    return render_to_response(template)