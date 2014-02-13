#! /usr/bin/env python
#coding=utf-8
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from passport.models.model import passport

'''
    根据username获取passport对象
'''
def GetPassportObjByUsername(userName):

    try:
        return passport.objects.get(username = userName)
    except Exception as e:
        raise e
    return None

'''
    根据uuid获取passport对象
'''
def GetPassportObjByUUID(passportUUID):

    try:
        return passport.objects.get(uuid = passportUUID)
    except Exception as e:
        raise e
    return None



'''
    判断passport username是否存在
'''

def IsPassportUserExists(userName):

    try:
        passportObj = GetPassportObjByUsername(userName)
        isExists = False
        if passportObj.username != None:
            isExists = True

    except ObjectDoesNotExist as e:
        isExists = False
    return isExists

'''
    判断passport密码是否正确
'''
def VerifyPassportPassword(username,password):

    try:

        #用户验证
        passportObj = auth.authenticate(username = username, password = password)
        if passportObj is not None:
            return True
    except Exception as e:
        return False
    return False