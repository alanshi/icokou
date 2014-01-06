#!/usr/bin/env python
#coding=utf-8


import os
import subprocess


# 回到 icokou 根目录
os.chdir('..')

# 基于 settingsDevLocal.py 导入 Django 初始化数据
commandStr = 'python manage.py loaddata scripts/initial_data.json --settings=icokou.settingsDevLocal'

outStr = subprocess.call(commandStr, shell=True)
