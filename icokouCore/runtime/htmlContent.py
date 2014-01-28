#! /usr/bin/env python
#coding=utf-8

#生成返回HTML的结果字典
def CreateHtmlContentDict(htmlContentDictRootInObj, keyName, keyValue):

    htmlContentDictRootOutObj = htmlContentDictRootInObj

    htmlContentDictRootOutObj[keyName] = keyValue

    return htmlContentDictRootOutObj

#从request.post获取数据并根据参数列表自动封装为 dict
def CreateFormDict(formInfoList,postData):

    formInfoDict = {}
    #如果post数据和参数列表都存在
    if formInfoList != None and postData !=None:
        #遍历参数列表
        for formInfo in formInfoList:
            #设定字典值
            formInfoDict[formInfo] = postData[formInfo]

        return formInfoDict

    return None