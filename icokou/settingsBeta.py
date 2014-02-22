#!/usr/bin/env python
#coding=utf-8

from settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'icokou',
        'USER': 'icokou',
        'PASSWORD':'3WbeC9KCwaTedLP4',
        'HOST':'',
        'PORT':'',
    }
}
ALLOWED_HOSTS = ['icokou.com']

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
)

STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# 避免在 lighttp-fastcgi 环境下 {% url %} 被加上 eveMapOnline.fcgi 的 url 前缀
FORCE_SCRIPT_NAME = ''

