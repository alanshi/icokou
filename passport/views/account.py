#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import auth

from icokouCore.runtime import htmlContent


'''
    passport帐号视图,用于对帐号注册,登录,注销等提供服务
'''

#登录
def Login(request):

    if request.method == 'GET':

        htmlContentDictRoot = {}
        urlPath = resolve(reverse('passport:Login')).namespace
        return render_to_response('%s/%s' % (urlPath,'login.html') , 
            htmlContentDictRoot, context_instance=RequestContext(request)
            )

    if request.method == 'POST':
        #获取表单信息
        pass

#注册
def Reg(request):

    if request.method == 'GET':

        htmlContentDictRoot = {}
        urlPath = resolve(reverse('passport:Reg')).namespace
        return render_to_response('%s/%s' % (urlPath,'reg.html') , 
            htmlContentDictRoot, context_instance=RequestContext(request)
            )
        
#注销
def Logout(request):

    auth.logout(request)
    return HttpResponseRedirect(reverse('passport:Login'))
