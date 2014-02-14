#!/usr/bin/env python
#coding=utf-8

from icokouCore.runtime import imageUtil
from food.models.model import food as foodModel

#添加菜品
def AddFood(foodInfo):
    
    try:
        picName = foodInfo['foodPic'].name
        picObj = foodInfo['foodPic']
        foodPic = imageUtil.SavePicFile(picName,picObj,'food')
        foodObj = foodModel(
            name =  foodInfo['foodName'],
            intro = foodInfo['foodMemo'],
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
    
