from EnvManagement.models import environment

#session = environment(env_name='DEV_FP',server='hqd-fptn72csvr-01',username='tnuser',password='tndev',tomcat_path='/usr/local/apache-tomcat-6.0.20',zipfolder_path='/home/tnuser/zipFolder',service_locator_path='/home/tnuser/serviceLocator')
#session.save()

def getEnv():
    dbValue = environment.objects.all()
    for env in dbValue:
        print env.id
