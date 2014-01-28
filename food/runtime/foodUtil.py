#!/usr/bin/env python
#coding=utf-8
from food.models.model import food as foodModel

#添加菜品
def AddFood(foodInfo):
    
    try:

    	foodObj = foodModel(
    		name = 	foodInfo['foodName'],
    		intro = foodInfo['foodMemo'],
    		pic = 	foodInfo['foodPic'],
    		)
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
		raise
#编辑菜品
def EditFood(fId,foodInfo):
    pass
    
