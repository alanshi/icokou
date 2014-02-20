#!/usr/bin/env python
#coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'recommendSystem.views.views',
    url(regex = r'^$',view = 'Index', name = 'Index'),
    url(regex = r'^goodluck$',view = 'GetGoodLuckFood', name = 'GetGoodLuckFood'),
    
)    