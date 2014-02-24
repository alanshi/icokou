#!/usr/bin/env python
#coding=utf-8




# #extra.mime_type = "image/jpg"


# #data = Image.open('xxx.jpg')
# fileName = r'D:\\__WORK__\\icokounew\\icokouCore\\runtime\\xxx.jpg'
# #ret, err = qiniu.io.put(uptoken, 'xxx.jpg', data, extra)
# ret, err = qiniu.io.put_file(uptoken, 'xx.jpg', fileName)


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
    #fileName = r'D:\\__WORK__\\icokounew\\icokouCore\\runtime\\xxx.jpg'
    ret, err = qiniu.io.put(uptoken, fileName, fileObj, extra)
    
    #ret, err = qiniu.io.put_file(uptoken, 'xx.jpg', fileName)

    print ret
    print err    


#UploadImageFile('xxx','xxx')