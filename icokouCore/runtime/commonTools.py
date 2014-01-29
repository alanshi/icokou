#!/usr/bin/env python
#coding=utf-8

#分离文件名和扩展名
# ex071107.log.1.exe
def GetFileNameAndExt(filename):
    try:
        import os
        (filepath,tempfilename) = os.path.split(filename)
        (shotname,extension) = os.path.splitext(tempfilename)
        return shotname,extension
    except Exception as e:
        print 'e:',e