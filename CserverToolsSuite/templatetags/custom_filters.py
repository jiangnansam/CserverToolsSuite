'''
Created on 2012-8-20

@author: kwwang
'''
from django import template
register = template.Library()

def sayHi(value,name):
    return value+" "+name



register.filter("sayHi", sayHi)