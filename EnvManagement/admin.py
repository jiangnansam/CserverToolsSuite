'''
Created on 2012-8-15

@author: njiang
'''
from django.contrib import admin
from EnvManagement.models import environment

class EnvAdmin(admin.ModelAdmin):
    list_display = ('env_name','server','username','password','tomcat_path','zipfolder_path','service_locator_path')

admin.site.register(environment,EnvAdmin)

