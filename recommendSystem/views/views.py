#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve


#默认首页
def Index(request):

    if request.method == 'GET':

        try:
            pass
        except:
            pass
        
        htmlContentDictRoot = {}
        urlPath = resolve(reverse('recommendSystem:Index')).namespace
        
        return render_to_response('%s/%s' % (urlPath,'index.html') , 
            htmlContentDictRoot, context_instance=RequestContext(request)
            )
  