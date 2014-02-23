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
        try:
            #获取表单信息
            foodInfo = {}

            #创建htmlContentDictRoot内容
            htmlContentDictRoot = {}
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'nextPage', {'url':reverse('food:AddFood')})

            foodInfo['foodName'] = request.POST['foodName']

            if foodInfo == '':
                htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'error', {'content':u'菜品名不允许为空'})
                raise

            foodInfo['foodMemo'] = request.POST['foodMemo']
            if foodInfo['foodMemo'] == '':
                htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'error', {'content':u'菜品介绍不允许为空'})
                raise                

            try:
                foodInfo['foodPrice'] = float(request.POST['foodPrice'])
            except Exception as e:
                foodInfo['foodPrice'] = 0.00

            foodInfo['foodAddress'] = request.POST.get('foodAddress',u'未知')

        
            foodInfo['foodPic'] = request.FILES.get('foodPic', None)
            if foodInfo['foodPic'] == None:
                htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'error', {'content':u'未上传菜品图片'})
                raise                 

            #获取当前用户名
            foodInfo['createUser'] = request.user
            #添加菜品
            foodObj = foodUtil.AddFood(foodInfo)

            return HttpResponseRedirect(reverse('food:ViewFood', kwargs={'fId':foodObj.id}))

        except Exception as e:
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'exception', {'content':e}) 
            return render_to_response('error.html', htmlContentDictRoot, context_instance=RequestContext(request))

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
            print e

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
  
#搜索菜品表单视图
def SearchForm(request):

    if request.method == 'POST':
        
        foodName = request.POST['foodName']
        return HttpResponseRedirect(reverse('food:SearchFood', kwargs={'foodName':foodName}))


#搜索菜品
def SearchFood(request,foodName=""):

    if request.method == 'GET':
        
        try:
            htmlContentDictRoot = {}
            urlPath = resolve(reverse('food:AddFood')).namespace
            foodObjList = foodUtil.SearchFood(foodName)
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'foodObjList', {'obj':foodObjList})
            return render_to_response('%s/%s' % (urlPath,'foodList.html') , 
                htmlContentDictRoot, context_instance=RequestContext(request)
                )            

        except Exception as e:
            raise e
