from django.shortcuts import render_to_response
from EnvManagement.models import environment
from django.views.decorators.csrf import csrf_exempt

#get all the environment from database
def get_env(request,template):
    db_value = environment.objects.all()
    return render_to_response(template,{'env_list':db_value})

#insert or update environment data
@csrf_exempt
def add_env(request, template):
    if request.POST.get('id') != '':
        db_value = environment.objects.filter(id=request.POST.get('id'))
        db_value.update(env_name = request.POST.get('env_name'), server = request.POST.get('server'), username = request.POST.get('username'), password = request.POST.get('password'), tomcat_path = request.POST.get('tomcat_path'), zipfolder_path = request.POST.get('zipfolder_path'), service_locator_path = request.POST.get('service_locator_path'))
    else:
        session = environment(env_name=request.POST.get('env_name'),server=request.POST.get('server'),username=request.POST.get('username'),password=request.POST.get('password'),tomcat_path=request.POST.get('tomcat_path'),zipfolder_path=request.POST.get('zipfolder_path'),service_locator_path=request.POST.get('service_locator_path'))
        session.save()
    return render_to_response(template,{'env_list':environment.objects.all()})

#delete environment        
def delete_env(request, envID, template):
    db_value = environment.objects.filter(id=envID)
    if db_value:
        environment.objects.filter(id=envID).delete()
    return render_to_response(template, {'env_list':environment.objects.all()})

#add new environment page
def new_env(request, template):
    return render_to_response(template)

#edit environment
def edit_env(request, envID, template):
    db_value = environment.objects.get(id=envID)
    return render_to_response(template, {'env':db_value})

