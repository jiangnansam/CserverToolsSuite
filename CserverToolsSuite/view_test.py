'''
Created on 2012-8-27

@author: kwwang
'''
from EnvManagement.models import environment
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


mock_env=environment(id=111,env_name='dev_fp',server='172.16.10.101',username="tnuser",password="tndev",tomcat_path="/home/tnuser/tomcat",zipfolder_path="/home/tnuser/zipfolder",service_locator_path="/home/tnuser/servicelocator")

def list_env(request,template):
    env_list=[mock_env]
    return render_to_response(template,{'env_list':env_list})

def new_env(request,template):
    return render_to_response(template)
@csrf_exempt
def save_env(request,template):
    print request.POST.get("password")
    return render_to_response(template)

def edit_env(request,envID,template):
    return render_to_response(template,{'env':mock_env})

def delete_env(request,envID,template):
    print "delete environment"
    return render_to_response(template,{'env':mock_env})