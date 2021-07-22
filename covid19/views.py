from django.shortcuts import render
from covid19.models import Data
from urllib import request
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import pandas as pd
# Create your views here.

def delete():
    d = Data.objects.all()
    d.delete()

def save(date, confirmed, death, released, tested, today):
    d = Data(date=date, confirmed=confirmed, death=death, released=released, tested=tested, today=today)
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
        # data[i][0] = datetime.strptime(data[i][0], '%Y%m%d')
        data[i][0] = pd.to_datetime(data[i][0], format='%Y%m%d')

    return data


def home(request):
    delete()
    data = covid19()
    for d in data:
        save(d[0], d[1], d[2], d[3], d[6], d[7])

    data_list = Data.objects.order_by('date')
    context = {'data_list':data_list}
    return render(request, 'covid19/home.html', context)