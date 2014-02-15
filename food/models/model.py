#!/usr/bin/env python
#coding=utf-8

from django.db import models
from passport.models.model import passport

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
    pic = models.CharField(u'菜品图片', max_length = 100,blank=True, null=True)
    #位置,地理经纬度坐标
    lon = models.CharField(u'经度', max_length = 20,blank=True, null=True)
    lat = models.CharField(u'纬度', max_length = 20,blank=True, null=True)
    #创建人
    create_user = models.ForeignKey(passport,blank=True, null=True)
    #地址
    address = models.CharField(u'地址', max_length = 50,blank=True, null=True)
    class Meta:
        app_label = 'food'



"""
    美食推荐日志
"""
class commend_food_log(models.Model):

    #访问ip
    ip = models.CharField(u'ip', max_length=15, blank=True, null=True)
    #推荐时间
    add_time= models.DateTimeField(auto_now_add=True)
    #所推荐的美食
    food = models.ForeignKey(food)
    #会员名称
    passport = models.ForeignKey(passport)
    #备注
    memo = models.CharField(u'备注', max_length=20, blank=True, null=True)
    class Meta:
        app_label = 'food'

"""
    美食收藏记录
"""
class collects_food_log(models.Model):
    #美食
    food = models.ForeignKey(food)
    #会员名称
    passport = models.ForeignKey(passport)
    #添加关注的日期
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'food'
        
"""
    美食浏览日志
"""
class view_food_log(models.Model):
    #访问ip
    ip = models.CharField(u'ip', max_length=15, blank=True, null=True)
    #访问时间
    add_time= models.DateTimeField(auto_now_add=True)
    #所访问的菜品
    food = models.ForeignKey(food)
    #会员名称
    passport = models.ForeignKey(passport,blank=True, null=True)

    class Meta:
        app_label = 'food'