import datetime
from datetime import datetime as d
import time
import os
from os import listdir, stat


from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_PATH = os.path.join(BASE_DIR, 'files')


def file_list(request, dat=None):
    template_name = 'index.html'
    file_l = []
    if dat:
        ddate = d.strptime(dat, '%Y-%m-%d')
        for file in listdir(FILES_PATH):
            statinfo = stat(FILES_PATH + '\\' + file)
            mt = time.gmtime(statinfo.st_mtime)
            mtime = datetime.date(mt.tm_year, mt.tm_mon, mt.tm_mday)
            ct = time.gmtime(statinfo.st_ctime)
            ctime = datetime.date(ct.tm_year, ct.tm_mon, ct.tm_mday)
            if ctime == ddate:
                file_info = {'name': file,
                             'ctime': ctime,
                             'mtine': mtime
                         }
                file_l.append(file_info)
        context = {'files': file_l,
                   'date': ddate
                   }
        return render(request, template_name, context)
    for file in listdir(FILES_PATH):
        statinfo = stat(FILES_PATH + '\\' + file)
        mt = time.gmtime(statinfo.st_mtime)
        mtime = datetime.date(mt.tm_year, mt.tm_mon, mt.tm_mday)
        ct = time.gmtime(statinfo.st_ctime)
        ctime = datetime.date(ct.tm_year, ct.tm_mon, ct.tm_mday)
        file_info = {'name': file,
                     'ctime': ctime,
                     'mtine': mtime
        }
        file_l.append(file_info)
    context = {'files': file_l
               }
    return render(request, template_name, context)


def file_content(request, name):
    with open(FILES_PATH + '\\' + name) as file:
        my_text = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': my_text}
    )

