#!/usr/bin/env python
#coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'food.views.views',
    url(regex = r'^add/$',view = 'AddFood', name = 'AddFood'),
    url(regex = r'^(?P<fId>\d+)/view/$',view = 'ViewFood', name = 'ViewFood'),
    
)    