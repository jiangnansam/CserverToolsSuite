from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CserverToolsSuite.views.home', name='home'),
#     url(r'^CserverToolsSuite/', include('CserverToolsSuite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     #to expose the static css&js files to outside
     url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
     
     url(r'^cli/$','Cli.views.lookupCliInfo',{'template':'cli/cli.html'}),
     
     
     #for environment operations
     url(r'^environment/list','EnvManagement.views.get_env',{'template':'env/list.html'}),
     
     url(r'^environment/new','EnvManagement.views.new_env',{'template':'env/new_and_edit.html'}),
     
     url(r'^environment/save','EnvManagement.views.add_env',{'template':'env/list.html'}),
     
     url(r'^environment/edit/(?P<envID>\d+)','EnvManagement.views.edit_env',{'template':'env/new_and_edit.html'}),
     
     url(r'^environment/delete/(?P<envID>\d+)','EnvManagement.views.delete_env',{'template':'env/list.html'}),
)
