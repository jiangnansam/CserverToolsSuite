from django.shortcuts import render_to_response
from EnvManagement.models import environment

#get all the environment from database
def get_env(template):
    db_value = environment.objects.all()
    return render_to_response(template,{'db_value', db_value})

#insert or update environment data
def add_update_env(request, template):
    env_id = request.GET['id']
    if env_id:
        db_value = environment.objects.filter(id=env_id)
        return render_to_response(template,{'db_value', db_value})
    else:
        session = environment(env_name=request.GET['env_name'],server=request.GET['server'],username=request.GET['username'],password=request.GET['password'],tomcat_path=request.GET['tomcat_path'],zipfolder_path=request.GET['zipfolder_path'],service_locator_path=request.GET['service_locator_path'])
        session.save()
        return render_to_response(template)

#delete environment        
def delete_env(request, template):
    env_id = request.GET['id']
    db_value = environment.objects.filter(id=env_id)
    if db_value:
        environment.objects.filter(id=env_id).delete()
        return render_to_response(template, {'message', 'success!!!'})
    return render_to_response(template, {'message', 'can not find the data in database'})

#add new environment page
def new_env(template):
    return render_to_response(template)

#edit environment
def edit_env(request, template):
    env_id = request.GET['id']
    env_name=request.GET['env_name']
    server=request.GET['server']
    username=request.GET['username']
    password=request.GET['password']
    tomcat_path=request.GET['tomcat_path']
    zipfolder_path=request.GET['zipfolder_path']
    service_locator_path=request.GET['service_locator_path']
    
    db_value = environment.objects.get(id=env_id)
    if db_value:
        if db_value.env_name == env_name:
            db_value.env_name = env_name
        if db_value.server == server:
            db_value.server = server
        if db_value.username == username:
            db_value.username = username
        if db_value.password == password:
            db_value.password = password
        if db_value.tomcat_path == tomcat_path:
            db_value.tomcat_path = tomcat_path
        if db_value.zipfolder_path == zipfolder_path:
            db_value.zipfolder_path = zipfolder_path
        if db_value.service_locator_path == service_locator_path:
            db_value.service_locator_path = service_locator_path
        
        db_value.save()
        return render_to_response(template, {'message', 'success!!!'})
    else:
        return render_to_response(template, {'message', 'can not find the data in database'})

