from django.shortcuts import render
from covid19.models import Data
from urllib import request
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime


def delete():
    d = Data.objects.all()
    d.delete()

def save(date, confirmed, death, released, critical, today):
    d = Data(date=date, confirmed=confirmed, death=death, released=released, critical=critical, today=today)
    d.save()

def covid19():
    URL = 'https://github.com/jooeungen/coronaboard_kr/blob/master/kr_daily.csv'
    data = []

    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

    for tr in soup.find_all('tr', class_='js-file-line'):
        td = tr.select('td')
        tds = []
        for d in td:
            if (not d.has_attr('class')):
                if (d.text == ''):
                    tds.append(0)
                else:
                    tds.append(int(d.text))
        tds.append(0)
        data.append(tds)
    data[0] = [20200120, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(data)):
        if i != 0:
            today = data[i][1] - data[i - 1][1]
            data[i][7] = today
        data[i][0] = pd.to_datetime(data[i][0], format='%Y%m%d')
        data[i][0] -= datetime.timedelta(1)

    return data

def update():
    data = covid19()

    if(Data.objects.count()!=0):
        last = Data.objects.last()
        if (last.date != data[-1][0]):
            delete()
            for d in data:
                save(d[0], d[1], d[2], d[3], d[6], d[7])
    else:
        for d in data:
            save(d[0], d[1], d[2], d[3], d[6], d[7])

def home(request):
    update()
    data_week = []
    data_list = Data.objects.order_by('-date')
    i = 0
    for data in data_list:
        i += 1
        if (i == 8):
            break
        data_week.append(data)
    data_week.reverse()
    data_list.reverse()



    today = format(data_list[0].today, ',')
    death = format(data_list[0].death - data_list[1].death, ',')
    released = format(data_list[0].released - data_list[1].released, ',')
    cri = data_list[0].critical - data_list[1].critical
    if cri >= 0:
        critical = "+" + format(cri, ',')
    else:
        critical = format(cri, ',')

    c = format(data_list[0].confirmed, ',')
    d = format(data_list[0].death, ',')
    r = format(data_list[0].released, ',')
    cr = format(data_list[0].critical, ',')

    data = Data.objects.last()
    context = {'data':data, 'data_list':data_list, 'data_week':data_week,
               'today':today,'death':death, 'released':released, 'critical':critical,
               'c':c, 'd':d, 'r':r, 'cr':cr}
    return render(request, 'covid19/home.html', context)