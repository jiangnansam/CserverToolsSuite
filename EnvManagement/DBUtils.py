'''
Created on 2012-8-21

@author: njiang
'''
from EnvManagement.models import environment

#get all the environment's information from DB
def getAllEnvs():
    return environment.objects.all()


#session = environment(env_name='DEV_FP',server='hqd-fptn72csvr-01',username='tnuser',password='tndev',tomcat_path='/usr/local/apache-tomcat-6.0.20',zipfolder_path='/home/tnuser/zipFolder',service_locator_path='/home/tnuser/serviceLocator')
#session.save()