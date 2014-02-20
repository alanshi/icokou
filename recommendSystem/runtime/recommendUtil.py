#!/usr/bin/env python
#coding=utf-8

from food.runtime import foodUtil

'''
    运气随机抽取菜品
    1:与当前菜品基因不同
    2:根据用户行为抽取
'''
def GetGoodLuckFood():

    try:
        #随机抽取1款菜品
        foodObj = foodUtil.GetRandomFoods(1)
        return foodObj
    except Exception as e:
        raise e