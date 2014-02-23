#! /usr/bin/env python
#coding=utf-8
import hashlib
import urllib
import urllib2
import json

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

#根据地址转换经纬度
def GetGeoByAddress(address):
    xUrl = 'http://maps.google.com/maps/api/geocode/json?address=%s&language=zh-CN&sensor=false' % (address)
    xUrl = xUrl.encode('utf8')  
    reqStr = urllib2.urlopen(xUrl).read()
    return json.loads(reqStr)['results'][0]['geometry']['viewport']['northeast']

#根据经纬度转换地址
def GetGeoByLng(lon,lat):
    xUrl = 'http://maps.google.com/maps/api/geocode/json?latlng=%s,%s&language=zh-CN&sensor=false' % (lon, lat)
    reqStr = urllib2.urlopen(xUrl).read()
    return json.loads(reqStr)['results'][0]['formatted_address']


if __name__ == '__main__':
    #address =  GetGeoByLng(30.790022932132747,106.08777952190394)
    #print address
    lngInfo =  GetGeoByAddress(u'成都市牧电路10号')
    print lngInfo