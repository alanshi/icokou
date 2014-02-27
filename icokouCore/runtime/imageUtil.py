#! /usr/bin/env python
#coding=utf-8

try:
    from PIL import Image
except ImportError:
    import Image

import os,sys
import hashlib
import commonTools
import qiniuUtil

#切割并保存图片文件
def CuttingPic(picFile,filePath,sizes=(75, 32)):

    base, ext = os.path.splitext(filePath)
    try:
        #打开图片
        im = Image.open(picFile)
    except IOError:
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255,255,255), None, bgmask)
        else:
            im = im.convert('RGB')

    width, height = im.size
    if width == height:
        region = im
    else:
        if width > height:
            delta = (width - height)/2
            box = (delta, 0, delta+height, height)
        else:
            delta = (height - width)/2
            box = (0, delta, width, delta+width)
        region = im.crop(box)

    filename = base +  ".jpg"
    thumb = region.resize((sizes[0],sizes[1]), Image.ANTIALIAS)
    thumb.save(filename, quality=100) # 默认 JPEG 保存质量是 75, 不太清楚。可选值(0~100)

    return filename

#保存图片文件--七牛
def SavePicFileByQiNiu(fileName,fileObj):

    try:
        import time
        
        #拆分文件扩展名
        uploadFileNameExt = commonTools.GetFileNameAndExt(fileName)[1].lower()
        #设置文件名
        uploadFileName = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        #拼接路径
        fullFileName = uploadFileName+uploadFileNameExt        
        #开始上传
        ret = qiniuUtil.UploadImageFile(fullFileName,fileObj)
        
        return 'http://icokou.qiniudn.com/%s' % (fullFileName)

    except Exception as e:
        raise e     

#保存图片文件
def SavePicFile(fileName,fileObj,fileType):

    try:
        #如果是菜品图片
        if fileType == 'food':
            filePath = MakeSaveFilePath(fileName,fileType)
            CuttingPic(fileObj,filePath[0],(400,350))
            return filePath[1]

    except Exception as e:
        raise  

#构造图片保存地址
def MakeSaveFilePath(fileName,fileType):
    import time
    #返回路径定义
    returnPath = '/static/upload/%s' % (fileType)
    BaseDir = os.path.dirname(__file__)
    #获取文件目录
    filePath = os.path.abspath(os.path.join(BaseDir,os.path.pardir,os.path.pardir,'icokou%s' % (returnPath)))
    #添加到sys.path
    try:
        sys.path.append(filePath)
    except Exception as e:
        print e
        
    #拆分扩展名
    uploadFileNameExt = commonTools.GetFileNameAndExt(fileName)[1].lower()
    
    # #设置文件名
    uploadFileName = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    #拼接路径
    fullFileName = uploadFileName+uploadFileNameExt

    #返回路径
    picDBPath = '%s/%s' %(returnPath,fullFileName)

    #设置保存文件名
    return os.path.join(filePath,fullFileName),picDBPath

if __name__=='__main__':
    #MakeSaveFilePath('f.jpg')
    #SavePicFile('f.jpg','food')   
    pass