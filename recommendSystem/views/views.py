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

#默认首页
def Index(request):

    if request.method == 'GET':

        try:
            htmlContentDictRoot = {}
            urlPath = resolve(reverse('recommendSystem:Index')).namespace
            foodObjList = foodUtil.GetRandomFoods(3)
            htmlContentDictRoot = htmlContent.CreateHtmlContentDict(htmlContentDictRoot,'foodObjList', {'obj':foodObjList})
            return render_to_response('%s/%s' % (urlPath,'index.html') , 
                htmlContentDictRoot, context_instance=RequestContext(request)
                )
        except Exception as e:
            pass
        
        
        

  