#! /usr/bin/env python
#coding=utf-8

import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#通行证管理接口
class PassportManager(BaseUserManager):
    
    #创建普通帐号
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email = PassportManager.normalize_email(email),
            username = username,
            uuid = str(uuid.uuid1()),
        )
 
        user.set_password(password)
        user.uuid = str(uuid.uuid1())
        user.save(using=self._db)
        return user
    
    #创建超级管理员
    def create_superuser(self, email,username, password):
    
        user = self.create_user(email,
            username = username,
            password = password,

        )
        user.uuid = str(uuid.uuid1())
        user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

#通行证
class passport(AbstractBaseUser):
    #唯一UUID
    uuid = models.CharField(max_length=36,unique=True, db_index=True,primary_key=True)
    #用户名
    username = models.CharField(max_length=12, unique=True, db_index=True)
    #电子邮箱
    email = models.EmailField(max_length=254)
    #管理员权限
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    #地址
    address = models.CharField(default='',max_length=140,blank=True, null=True)
    #生日
    birth = models.DateField(blank=True, null=True)
    #身份证
    id_card = models.CharField(default='',max_length=20,blank=True, null=True)
    #移动电话
    mobile_no = models.CharField(default='',max_length=30,blank=True, null=True)
    #真实姓名
    real_name = models.CharField(default='',max_length=20,blank=True, null=True)
    #注册时间
    reg_time =  models.DateTimeField(auto_now_add=True,blank=True, null=True)
    #最后登录时间
    last_login_time = models.DateTimeField(blank=True, null=True)
    #最后登录ip
    last_login_ip = models.IPAddressField(blank=True, null=True)
    #邮箱认证标记
    email_is_verified = models.BooleanField(default=False)
    #美食基因
    food_genetic = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = PassportManager()
    
    class Meta:
        app_label = 'passport'