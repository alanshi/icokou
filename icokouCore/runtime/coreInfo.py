#! /usr/bin/env python
#coding=utf-8
import hashlib

#获取客户端IP
def GetClientIp(requestMETA):

    try:
        x_forwarded_for = requestMETA.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = requestMETA.get('REMOTE_ADDR')
    except Exception as e:
        ip = 'unKonw'
    return ip

#MD5加密
def MD5(pwdStr,upperSwitch=True):
    #如果选择大写开关
    if upperSwitch:
        md5Str = hashlib.md5(pwdStr).hexdigest().upper()
    else:
        md5Str = hashlib.md5(pwdStr).hexdigest()
    return md5Str




if __name__ == '__main__':
    pass