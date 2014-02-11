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
from icokouCore.runtime import coreInfo
from icokouCore.runtime import datetimeTools


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
        
        try:
            #获取输入的帐户信息
            username = request.POST['username']
            password = request.POST['password']
            
            #创建htmlContentDictRoot内容
            htmlContentDictRoot = {}
            #默认下一个页面
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'nextPage', {'url':reverse('passport:Login')})
            
            #获取用户认证结果
            passportObj = auth.authenticate(username = username, password = password)
            
            #如果登录验证成功
            if passportObj is not None:

                #记录客户端最后登录时间和IP
                clientIp = coreInfo.GetClientIp(request.META)
                passportObj.last_login_ip = clientIp
                passportObj.last_login_time = datetimeTools.GetTimeStamp()
                passportObj.save()
                #登录认证信息
                auth.login(request, passportObj)
                #返回主页
                return HttpResponseRedirect(reverse('recommendSystem:Index'))

            #登录验证失败
            else:
                htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'error', {'content':u'您输入的用户名或密码存在错误,请重试'})
                raise

        #异常处理
        except Exception as e:
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'exception', {'content':e}) 

            return render_to_response('error.html', htmlContentDictRoot, context_instance=RequestContext(request))

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
