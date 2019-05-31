from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import urllib.parse as urllib
import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        bus_data = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_line = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            bus_data.append(bus_line)
    page = request.GET.get('page')
    if page == None:
        page = 1
    page = int(page)
    bs = bus_data[(page - 1)*10:page*10]
    if page - 1 == 0:
        purl = None
    else:
        purl = '?' + urllib.urlencode({'page': page - 1})
    nurl = '?' + urllib.urlencode({'page': page + 1})
    return render_to_response('index.html', context={
        'bus_stations': bs,
        'current_page': page,
        'prev_page_url': purl,
        'next_page_url': nurl,
    })

