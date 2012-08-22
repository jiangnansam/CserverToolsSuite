from DBUtils import *


def getEnv():
    dbValue = environment.objects.all()
    for env in dbValue:
        print env.id
