from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import collections
import json
import re
import requests

username='njiang@telenav.cn'
passwd='@wsx3edc'

NO_ROOT_CAUSE_ERROR = '10001'
OUT_OF_RELEASE_ERROR = '10002'
NO_DATA_ERROR = '10003'

def get_fixverison(request,template):
    fixversion_list=[]
    p = re.compile('CSVR-201[3-9]')
    r = requests.get('http://jira.telenav.com:8080/rest/api/2/project/TNCSERVER', auth=(username,passwd))
    project_info = json.loads(r.text)
    for version in project_info['versions']:
        if p.search(version['name']) != None:
            fixversion_list.append(version['name'])
    return render_to_response(template,{'fixversion_list':fixversion_list})

@csrf_exempt
def query_jira(request,template):
    svn_dict = {}
    mapping_dict = collections.OrderedDict()
    req = ''
    error_msg = {NO_ROOT_CAUSE_ERROR:'',OUT_OF_RELEASE_ERROR:'',NO_DATA_ERROR:''}
    for key in request.POST.keys():
        req = key
    p = re.compile("http:.*?\d{8,10}")
    r = requests.get('http://jira.telenav.com:8080/rest/api/2/search?jql=component=TN6xDBChange+and+fixVersion=%22' 
                     + str(req) + '%22', auth=(username,passwd))
    tasks_info = json.loads(r.text)
    if tasks_info.has_key('issues') and len(tasks_info['issues']) > 0:
        for issues in tasks_info['issues']:
            svn_path = issues['fields']['customfield_10051']
            if svn_path != None:
                svn_dict[issues['key']] = p.search(svn_path).group()
            else:
                error_msg[NO_ROOT_CAUSE_ERROR] = error_msg[NO_ROOT_CAUSE_ERROR] + issues['key'] + ','
        for dict in sorted(svn_dict.iteritems(),key = lambda v:v[1]):
            for issues in tasks_info['issues']:
                depend_issue_str = ''
                if dict[0] == issues['key'] and issues['fields'].has_key('issuelinks'):
                    for depend_issues in issues['fields']['issuelinks']:
                        if depend_issues.has_key('outwardIssue') and depend_issues['outwardIssue'] != None:
                            depend_issue_str = depend_issue_str + depend_issues['outwardIssue']['key'] + ','
                    mapping_dict[issues['key']] = depend_issue_str.rstrip(',')
    else:
        error_msg[NO_DATA_ERROR] = str(req)
    issue_list = sort_issue_id(mapping_dict)
    error_msg[OUT_OF_RELEASE_ERROR] = validate_task(mapping_dict)
    return HttpResponse(init_html(svn_dict,issue_list,error_msg))

def validate_task(mapping_dict):
    error_msg = ''
    for key in mapping_dict.keys():
        if len(mapping_dict[key]) > 0:
            for issue_key in mapping_dict[key].split(','):
                if not mapping_dict.has_key(issue_key):
                    error_msg = error_msg + issue_key + ','
    return error_msg

def sort_issue_id(mapping_dict):
    issue_list = []
    for key in mapping_dict.keys():
        issue_list.append(key)
    for key in mapping_dict.keys():
        if len(mapping_dict[key]) > 0:
            for depend_key in mapping_dict[key].split(','):
                if issue_list.index(depend_key) > issue_list.index(key):
                    issue_list.remove(depend_key)
                    issue_list.insert(issue_list.index(key),depend_key)
    return issue_list
            
def init_html(svn_dict,issue_list,error_msg):
    html = '<ol>'
    for issue in issue_list:
        html = html + '<li>' + svn_dict[issue] + '</li>'
    html = html + '</ol>'
    if len(error_msg[NO_ROOT_CAUSE_ERROR]) > 0:
        html = html + '<h6>' 
        for task in error_msg[NO_ROOT_CAUSE_ERROR].split(','):
            html = html + '<a href=\"http://jira.telenav.com:8080/browse/' + task + '" target="_blank">' + task + '</a> '
        html = html + 'don\'t contain svn path content in "root cause" item.</h6>'
    if len(error_msg[OUT_OF_RELEASE_ERROR]) > 0:
        html = html + '<h6>'
        for task in error_msg[OUT_OF_RELEASE_ERROR].split(','):
            html = html + '<a href="http://jira.telenav.com:8080/browse/' + task + ' target="_blank">' + task + '</a> '
        html = html + ' don\'t in this release train.</h6>'
    if len(error_msg[NO_DATA_ERROR]) > 0:
        html = html + '<h6>No Jira tickets.</h6>'
    return html

