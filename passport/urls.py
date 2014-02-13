#!/usr/bin/env python
#coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'passport.views.account',
    url(regex = r'^login$',view = 'Login', name = 'Login'),
    url(regex = r'^reg$',view = 'Reg', name = 'Reg'),
    url(regex = r'^logout$',view = 'Logout', name = 'Logout'),
)
