REM ====================
REM 开发测试服务器启动脚本

REM 设置搜索路径
REM SET PATH=%PATH%;C:\Python26;C:\Python26\Lib\site-packages\django\bin

REM 回到项目根目录
cd ..

REM 强制删除旧的pyc文件
del/S *.pyc

REM 基于 settingsDevLocal.py 配置文件启动Django开发服务器
python manage.py runserver 192.168.199.192:8000 --settings=icokou.settingsDevLocal

pause