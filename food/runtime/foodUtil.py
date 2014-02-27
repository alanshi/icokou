#!/usr/bin/env python
#coding=utf-8

from food.models.model import food as foodModel
from food.models.model import view_food_log as foodViewLogModel
from food.models.model import commend_food_log as foodCommendLogModel
from food.models.model import collects_food_log as foodCollectsLogModel

from icokouCore.runtime import imageUtil
from icokouCore.runtime import coreInfo
from passport.runtime import passportProfile

#添加菜品
def AddFood(foodInfo):
    
    try:
        picName = foodInfo['foodPic'].name
        picObj = foodInfo['foodPic']
        #上传菜品图片并获取返回路径
        #foodPic = imageUtil.SavePicFileByQiNiu(picName,picObj)
        foodPic = imageUtil.SavePicFile(picName,picObj,'food')
        #获取菜品所在地理地址
        address = foodInfo['foodAddress']
        #转换经纬度坐标
        lngInfo = coreInfo.GetGeoByAddress(address)
        #获取来路IP所对应的城市名和城市id
        ipAddress = foodInfo['ipAddress']
        geoInfo = coreInfo.GetGeoByIpAddress(ipAddress)

        cityId = geoInfo['data']['city_id']
        cityName = geoInfo['data']['city']

        foodObj = foodModel(
            name =  foodInfo['foodName'],
            intro = foodInfo['foodMemo'],
            price = foodInfo['foodPrice'],
            address = foodInfo['foodAddress'],
            pic =   foodPic,
            lng = lngInfo['lng'],
            lat = lngInfo['lat'],
            city_id = cityId,
            city_name = cityName,
            )
        foodObj.save()
        #判断是否为注册用户添加
        if foodInfo['createUser'].is_authenticated():
            foodObj.create_user = foodInfo['createUser']
            foodObj.save()
        return foodObj

    except Exception as e:

        raise e

#获取菜品信息
def GetFoodById(fId):

    try:
        foodObj = foodModel.objects.get(id = fId)
        return foodObj
    except Exception as e:
        raise e

#获取随机个数菜品信息
def GetRandomFoods(randomNum):

    try:
        #随机获取 基于浏览次数,推荐次数,关注次数和分数
        foodObjList = foodModel.objects.order_by('?','-hits','-commends','-collects')[:randomNum]
        return foodObjList
    except Exception as e:
        raise e
        
#编辑菜品
def EditFood(fId,foodInfo):
    pass

'''
添加菜品浏览记录
基于IP，每IP每24小时访问最多添加1次浏览记录(!!!暂未实现)
'''
def AddFoodHitLog(fId,passportObj,ipAddr):

    try:
        #初始化是否能够添加浏览次数的布尔值
        #isCanAddHits = False
        #获取菜品基本资料        
        foodObj = GetFoodById(fId)

        #菜品浏览日志+1
        vflObj = foodViewLogModel(
                ip = ipAddr,
                food = foodObj,
            )
        vflObj.save()

        #如果是注册用户浏览
        if passportObj.is_authenticated():
            vflObj.passport = passportObj

        #菜品浏览记录+1
        foodObj.hits+=1
        foodObj.save()

    except Exception as e:
        raise e


#添加菜品推荐记录
def AddFoodCommendLog(fId,passportObj,ipAddr):

    try:
 
        #获取菜品基本资料
        foodObj = GetFoodById(fId)

        #如果允许推荐
        if not foodCommendLogModel.objects.filter(food=foodObj,passport=passportObj).exists():
            #添加菜品推荐记录 
            fclObj = foodCommendLogModel(
                    ip = ipAddr,
                    food = foodObj,  
                    passport = passportObj                  
                )   
            fclObj.save()
         
            #菜品推荐次数+1
            foodObj.commends+=1
            foodObj.save()    
            return True
        return False
    except Exception as e:
        return False


#添加菜品收藏记录 
def AddFoodCollectsLog(fId,passportObj):

    try:
  
        #获取菜品基本资料
        foodObj = GetFoodById(fId)

        #如果允许收藏
        if not foodCollectsLogModel.objects.filter(food=foodObj,passport=passportObj).exists():
            #添加菜品收藏记录 
            fclObj = foodCollectsLogModel(
                    food = foodObj,
                    passport = passportObj
                )   
            fclObj.save()  
            #菜品收藏次数+1
            foodObj.collects+=1
            foodObj.save()    
            return True
        return False
    except Exception as e:
        return False

#搜索菜品
def SearchFood(foodName):

    try:
        searchResult = foodModel.objects.filter(name__contains = foodName)
        foodList = searchResult[:9]
        return foodList
    except Exception as e:
        raise e
