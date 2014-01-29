#!/usr/bin/env python
#coding=utf-8

from django.db import models

"""
菜品
"""
class food(models.Model):
    """
    菜品模型
    """
    #名称
    name = models.CharField(u'名称', max_length = 50)
    #一句话介绍 30字内的一个简要介绍--摘要
    abstract = models.CharField(u'摘要', max_length = 60)
    #菜品详细说明
    intro = models.TextField(blank=True, null=True)
    #原料，成分   ['生姜','大蒜','料酒','精瘦肉']
    material = models.CharField(u'原料', max_length = 400,blank=True, null=True)
    #口味(甜，咸，酸) ['微辣','酸']
    taste  = models.CharField(u'口味', max_length = 30,blank=True, null=True)
    #价格
    price = models.FloatField(default=0.0)
    #每天限时供应,大概什么时候卖完
    time_limit = models.TimeField(blank=True, null=True)
    #添加到系统的日期
    create_time = models.DateTimeField(auto_now_add=True)
    #浏览次数
    hits = models.IntegerField(default=0)
    #推荐次数
    commends = models.IntegerField(default=0)
    #收藏次数
    collects = models.IntegerField(default=0)    
    #菜品图片
    #pic = models.ImageField(u'菜品图片原图',upload_to='icokou/static/upload', max_length = 100,blank=True, null=True)odels.ImageField(u'菜品图片原图',upload_to='icokou/static/upload', max_length = 100,blank=True, null=True)
    pic = models.CharField(u'菜品图片', max_length = 100,blank=True, null=True)

    #位置,地理经纬度坐标
    location = models.CharField(u'位置', max_length = 50)
    
    class Meta:
        app_label = 'food'