#!/usr/bin/python
import sys, os
 
# Add a custom Python path.
#sys.path.insert(0, "/home/user/python")
 
# Switch to the directory of your project. (Optional.)
# os.chdir("/home/user/myproject")
 
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "icokou.settingsBeta"
 
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
