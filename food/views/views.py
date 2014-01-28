#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve

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
        foodInfo['foodPic'] = request.FILES.get('foodPic', None)
        foodObj = foodUtil.AddFood(foodInfo)

        return HttpResponseRedirect(reverse('food:ViewFood', kwargs={'fId':foodObj.id}))

#查看菜品
def ViewFood(request,fId):

    if request.method == 'GET':

        foodObj = foodUtil.GetFoodById(fId)
        foodPic = str(foodObj.pic)
        foodPic = foodPic.replace('icokou','')
        foodObj.pic = foodPic

        htmlContentDictRoot = {}
        urlPath = resolve(reverse('food:AddFood')).namespace
        htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'food', {'obj':foodObj})
        return render_to_response('%s/%s' % (urlPath,'viewFood.html') , 
            htmlContentDictRoot, context_instance=RequestContext(request)
            )
        
#编辑菜品
def EditFood(request,fId):

    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass   
  