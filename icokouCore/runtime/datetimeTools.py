#! /usr/bin/env python
#coding=utf-8

from time import strftime, localtime
from datetime import timedelta, date
import calendar
import time

"""
日期和时间公用函数
"""
year = strftime("%Y",localtime())
mon  = strftime("%m",localtime())
day  = strftime("%d",localtime())
hour = strftime("%H",localtime())
min  = strftime("%M",localtime())
sec  = strftime("%S",localtime())


#获取当前time
def GetTime():
    return time.time()

#获取当前时间戳字符串,不带符号
def GetUnsignedTimeStamp():

    #timeStamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    timeStamp  = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    return timeStamp


#获取当前时间戳字符串
def GetTimeStamp():
    timeStamp  = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return timeStamp

#返回日期范围
#GetDateRange(2010043020100506)
def GetDateRange(timedelta):


    #拆分日期范围
    startDateY = int(timedelta[0:4])
    startDateM = int(timedelta[4:6])
    startDateD = int(timedelta[6:8])
    endDateY = int(timedelta[8:12])
    endDateM = int(timedelta[12:14])
    endDateD = int(timedelta[14:16])

    #日期跨度
    dateBegin = date(startDateY, startDateM, startDateD)
    dateEnd = date(endDateY, endDateM, endDateD)
    return dateBegin,dateEnd


#获取人性化的时间：
#GetFriendlyTime(datetime)
def GetFriendlyTime(ts):
   delta = datetime.datetime.now() - ts
   if delta.days >= 365:
       return u'%d 年前' % (delta.days / 365)
   elif delta.days >= 30:
       return u'%d 个月前' % (delta.days / 30)
   elif delta.days > 0:
       return u'%d 天前' % delta.days
   elif delta.seconds < 60:
       return u"%d 秒前!" % delta.seconds
   elif delta.seconds < 60 * 60:
       return u"%d 分钟前" % (delta.seconds / 60)
   else:
       return u"%d 小时前" % (delta.seconds / 60 / 60)

#获取任意一个月的最后一天
def GetLastDayOfMonth(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = date(year, month, i)
        except ValueError:
            continue
        else:
            return end.day
    return None



#获取任意个月之前或之后的月份
#GetBeforeOrAfterMonth(1)表示一个月之后,GetBeforeOrAfterMonth(-2)表示两个月之前
def GetBeforeOrAfterMonth(months=1):
    year, month, day = date.today().timetuple()[:3]
    new_month = month + months
    return date(year + (new_month / 12), new_month % 12, day)

def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''
    return date.today()

def todaystr():
    '''''
    get date string
    date format="YYYYMMDD"
    '''
    return year+mon+day

def datetime():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return strftime("%Y-%m-%d %H:%M:%S",localtime())

def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year+mon+day+hour+min+sec

def getdayofday(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)
#获取任意一个月的天数
def getdaysofmonth(year,mon):
    '''''
    get days of month
    '''
    return calendar.monthrange(year, mon)[1]

def getfirstdayofmonth(year,mon):
    '''''
    get the first day of month
    date format = "YYYY-MM-DD"
    '''
    days="01"
    if(int(mon)<10):
        mon = "0"+str(int(mon))
    arr = (year,mon,days)
    return "-".join("%s" %i for i in arr)

#获取任意一个月的最后一天
def getlastdayofmonth(year,mon):
    '''''
    get the last day of month
    date format = "YYYY-MM-DD"
    '''
    days=calendar.monthrange(year, mon)[1]
    mon = addzero(mon)
    arr = (year,mon,days)
    return "-".join("%s" %i for i in arr)

def get_firstday_month(n=0):
    '''''
    get the first day of month from today
    n is how many months
    '''
    (y,m,d) = getyearandmonth(n)
    d = "01"
    arr = (y,m,d)
    return "-".join("%s" %i for i in arr)

def get_lastday_month(n=0):
    '''''
    get the last day of month from today
    n is how many months
    '''
    return "-".join("%s" %i for i in getyearandmonth(n))

def get_today_month(n=0):
    '''''
    get last or next month's today
    n is how many months
    date format = "YYYY-MM-DD"
    '''
    (y,m,d) = getyearandmonth(n)
    arr=(y,m,d)
    if(int(day)<int(d)):
        arr = (y,m,day)
    return "-".join("%s" %i for i in arr)

def getyearandmonth(n=0):
    '''''
    get the year,month,days from today
    befor or after n months
    '''
    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon+n
    if(n>=0):
        if(totalmon<=12):
            days = str(getdaysofmonth(thisyear,totalmon))
            totalmon = addzero(totalmon)
            return (year,totalmon,days)
        else:
            i = totalmon/12
            j = totalmon%12
            if(j==0):
                i-=1
                j=12
            thisyear += i
            days = str(getdaysofmonth(thisyear,j))
            j = addzero(j)
            return (str(thisyear),str(j),days)
    else:
        if((totalmon>0) and (totalmon<12)):
            days = str(getdaysofmonth(thisyear,totalmon))
            totalmon = addzero(totalmon)
            return (year,totalmon,days)
        else:
            i = totalmon/12
            j = totalmon%12
            if(j==0):
                i-=1
                j=12
            thisyear +=i
            days = str(getdaysofmonth(thisyear,j))
            j = addzero(j)
            return (str(thisyear),str(j),days)
#自动补0
def addzero(n):
    '''''
    add 0 before 0-9
    return 01-09
    '''
    nabs = abs(int(n))
    if(nabs<10):
        return "0"+str(nabs)
    else:
        return nabs


