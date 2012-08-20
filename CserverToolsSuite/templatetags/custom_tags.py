'''
Created on 2012-8-20

@author: kwwang
'''

from django import template
import datetime

register=template.Library()

def currentTime(parser,token):
    try:
        tag_name,content=token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,"tag parsing failed.."
    return CurrentTimeNode(content)


class CurrentTimeNode(template.Node):
    def __init__(self,content):
        self.content=content
    
    def render(self,context):
        return datetime.datetime.now().strftime(self.content)
    
register.tag("currentTime",currentTime)