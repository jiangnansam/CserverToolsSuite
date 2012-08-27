'''
Created on 2012-8-21

@author: njiang
'''
from EnvManagement.models import environment

#get all the environment's information from DB
def getAllEnvs():
    return environment.objects.all()


