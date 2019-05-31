import os
from os import path, listdir, stat
from _datetime import datetime
import time

FILES_PATH = os.path.join(r'D:\GitHub\netology_django\request-handling\file_server', 'files')

# print(listdir(FILES_PATH))
# for file in listdir(FILES_PATH):
#     print(file)
#     statinfo = stat(FILES_PATH +'\\' + file)
#     print(statinfo)
#     print(time.gmtime(statinfo.st_mtime))
#     mt = time.gmtime(statinfo.st_mtime)
#     print(mt.tm_mon)
#     d = datetime(mt.tm_year, mt.tm_mon, mt.tm_mday)
#     print(d, type(d))
mt = '2019-01-02'

print(datetime.strptime(mt, '%Y-%m-%d'))
#   print(time.ctime(statinfo.st_ctime))
