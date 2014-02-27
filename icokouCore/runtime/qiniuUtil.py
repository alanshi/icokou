#!/usr/bin/env python
#coding=utf-8

#上传图片文件
def UploadImageFile(fileName,fileObj):
    
    import qiniu.conf

    #设置key
    qiniu.conf.ACCESS_KEY = "tWaPOLnCQTDJMqND7cMULs5JiFVUWDVKhNwR2ZGH"
    qiniu.conf.SECRET_KEY = "whS0vfEoumhPJvNnLtRI3vfif7C6HBhYSZeHa_iU"

    #初始化资源凭证
    import qiniu.rs
    policy = qiniu.rs.PutPolicy('icokou')
    uptoken = policy.token()


    #准备上传
    import qiniu.io
    extra = qiniu.io.PutExtra()

    #开始上传
    ret, err = qiniu.io.put(uptoken, fileName, fileObj, extra)

    if err is not None:
        sys.stderr.write('error: %s ' % err)
        print err
        return err

    return ret

if __name__=='__main__':

    import StringIO

    fileObj = StringIO.StringIO("hello!")

    UploadImageFile('test.txt',fileObj)
