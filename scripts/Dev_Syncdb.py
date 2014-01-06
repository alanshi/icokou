#!/usr/bin/env python
#coding=utf-8


import os
import subprocess


# 回到 icokou 根目录
os.chdir('..')

# 基于 settingsDevLocal.py 为 Django 生成、同步数据库
commandStr = 'python manage.py syncdb --settings=icokou.settingsDevLocal'

outStr = subprocess.call(commandStr, shell=True)
