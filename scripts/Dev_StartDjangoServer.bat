REM ====================
REM �������Է����������ű�

REM ��������·��
REM SET PATH=%PATH%;C:\Python26;C:\Python26\Lib\site-packages\django\bin

REM �ص���Ŀ��Ŀ¼
cd ..

REM ǿ��ɾ���ɵ�pyc�ļ�
del/S *.pyc

REM ���� settingsDevLocal.py �����ļ�����Django����������
python manage.py runserver 192.168.199.192:8000 --settings=icokou.settingsDevLocal

pause