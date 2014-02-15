#!/usr/bin/env python
#coding=utf-8

from food.models.model import food as foodModel
from food.models.model import view_food_log as foodViewLogModel
from food.models.model import commend_food_log as foodCommendLogModel
from food.models.model import collects_food_log as foodCollectsLogModel

from icokouCore.runtime import imageUtil
from passport.runtime import passportProfile 

#添加菜品
def AddFood(foodInfo):
    
    try:
        picName = foodInfo['foodPic'].name
        picObj = foodInfo['foodPic']
        foodPic = imageUtil.SavePicFile(picName,picObj,'food')
        foodObj = foodModel(
            name =  foodInfo['foodName'],
            intro = foodInfo['foodMemo'],
            price = foodInfo['foodPrice'],
            address = foodInfo['foodAddress'],
            pic =   foodPic,
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
def AddFoodHitLog(fId,passportObj):

    try:
        #初始化是否能够添加浏览次数的布尔值
        #isCanAddHits = False
        #获取菜品基本资料        
        foodObj = GetFoodById(fId)
        #菜品浏览日志+1
        vflObj = foodViewLogModel(
                food = foodObj,
                passport = passportObj
            )
        vflObj.save()
        #菜品浏览记录+1
        foodObj.hits+=1
        foodObj.save()

    except Exception as e:
        raise e


#添加菜品推荐记录
def AddFoodCommendLog(fId,passportObj):

    try:
 
        #获取菜品基本资料
        foodObj = GetFoodById(fId)

        #如果允许推荐
        if not foodCommendLogModel.objects.filter(food=foodObj,passport=passportObj).exists():
            #添加菜品推荐记录 
            fclObj = foodCommendLogModel(
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
        raise e


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
        raise e
