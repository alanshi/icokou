#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from django.http import Http404

from food.runtime import foodUtil
from icokouCore.runtime import htmlContent
from icokouCore.runtime import coreInfo


#添加菜品
def AddFood(request):

    if request.method == 'GET':

        htmlContentDictRoot = {}
        urlPath = resolve(reverse('food:AddFood')).namespace
        return render_to_response('%s/%s' % (urlPath,'addFood.html') , 
            htmlContentDictRoot, context_instance=RequestContext(request)
            )
    if request.method == 'POST':
        #获取表单信息
        foodInfo = {}
        foodInfo['foodName'] = request.POST['foodName']
        foodInfo['foodMemo'] = request.POST['foodMemo']
        try:
            foodInfo['foodPrice'] = float(request.POST['foodPrice'])
        except Exception as e:
            foodInfo['foodPrice'] = 0.00
        foodInfo['foodAddress'] = request.POST['foodAddress']
        foodInfo['foodPic'] = request.FILES.get('foodPic', None)
        #获取当前用户名
        foodInfo['createUser'] = request.user
        #添加菜品
        foodObj = foodUtil.AddFood(foodInfo)

        return HttpResponseRedirect(reverse('food:ViewFood', kwargs={'fId':foodObj.id}))

#查看菜品
def ViewFood(request,fId):

    if request.method == 'GET':

        try:
            #获取ip地址
            ipAddr = coreInfo.GetClientIp(request.META)
            #获取菜品对象
            foodObj = foodUtil.GetFoodById(fId)
            #添加点击次数
            foodUtil.AddFoodHitLog(fId,request.user,ipAddr)

            htmlContentDictRoot = {}
            urlPath = resolve(reverse('food:AddFood')).namespace
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'food', {'obj':foodObj})
            return render_to_response('%s/%s' % (urlPath,'viewFood.html') , 
                htmlContentDictRoot, context_instance=RequestContext(request)
                )
        except Exception as e:
            raise Http404

#推荐菜品
def CommendFood(request,fId):

    if request.method == 'GET':

        try:
            #获取ip地址
            ipAddr = coreInfo.GetClientIp(request.META)
            #添加推荐
            foodUtil.AddFoodCommendLog(fId,request.user,ipAddr)
            return HttpResponseRedirect(reverse('food:ViewFood', kwargs={'fId':fId}))
        except Exception as e:
            raise Http404

#收藏菜品
def CollectsFood(request,fId):


    if request.method == 'GET':

        try:
            #添加收藏
            foodUtil.AddFoodCollectsLog(fId,request.user)
            return HttpResponseRedirect(reverse('food:ViewFood', kwargs={'fId':fId}))

        except Exception as e:
            
            raise Http404
        
#编辑菜品
def EditFood(request,fId):

    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass   
  