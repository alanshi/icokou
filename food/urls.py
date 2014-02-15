#!/usr/bin/env python
#coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'food.views.views',
    url(regex = r'^add/$',view = 'AddFood', name = 'AddFood'),
    url(regex = r'^(?P<fId>\d+)/view$',view = 'ViewFood', name = 'ViewFood'),
    url(regex = r'^(?P<fId>\d+)/commend$',view = 'CommendFood', name = 'CommendFood'),
    url(regex = r'^(?P<fId>\d+)/collects$',view = 'CollectsFood', name = 'CollectsFood'),
)    