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
            foodObj = foodUtil.GetFoodById(fId)
            foodPic = str(foodObj.pic)
            foodPic = foodPic.replace('icokou','')
            foodObj.pic = foodPic
            #添加点击次数
            foodUtil.AddFoodHitLog(fId,request.user)

            htmlContentDictRoot = {}
            urlPath = resolve(reverse('food:AddFood')).namespace
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'food', {'obj':foodObj})
            return render_to_response('%s/%s' % (urlPath,'viewFood.html') , 
                htmlContentDictRoot, context_instance=RequestContext(request)
                )
        except Exception as e:
            raise Http404
        
#编辑菜品
def EditFood(request,fId):

    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass   
  