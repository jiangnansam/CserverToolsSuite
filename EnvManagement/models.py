from django.db import models

class environment(models.Model):
    env_name = models.CharField(max_length=64,blank=True)
    server = models.CharField(max_length=64,blank=True)
    username = models.CharField(max_length=64,blank=True)
    password = models.CharField(max_length=64,blank=True)
    tomcat_path = models.CharField(max_length=108,blank=True)
    zipfolder_path = models.CharField(max_length=108,blank=True)
    service_locator_path = models.CharField(max_length=108,blank=True)