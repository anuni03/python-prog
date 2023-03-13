import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

import platform
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%B-%d %I %p : %M : %S"))
