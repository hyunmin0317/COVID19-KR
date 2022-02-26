from django.shortcuts import render
from xml.etree.ElementTree import fromstring, ElementTree
import requests
import datetime

def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data

def vaccine_API():
    URL = 'https://nip.kdca.go.kr/irgd/cov19stats.do?list=all'
    response = requests.get(URL).text
    data = []

    return 0, 1

    # tree = ElementTree(fromstring(response))
    # root = tree.getroot()
    #
    # for item in root.iter("item"):
    #     value = int(item.find('thirdCnt').text)
    #     value = format(value, ',')
    #     data.append(value)
    # print(data)
    # return data[0], data[2]

def home(request):
    today, yesterday = covid19_API(1)[0], covid19_API(2)[1]
    data_week, data_list = covid19_API(7), covid19_API(30)
    vaccine_today, vaccine = vaccine_API()

    data_week.reverse()
    data_list.reverse()

    for data in data_week:
        data['S_DT'] = data['S_DT'][5:10]
    for data in data_list:
        data['S_DT'] = datetime.datetime.strptime(data['S_DT'],"%Y.%m.%d.%H").strftime('%Y-%m-%d')
    today['S_DT'] = today['S_DT'][:11]

    death = int(today['DEATH']) - int(yesterday['DEATH'])
    released = int(today['RECOVER']) - int(yesterday['RECOVER'])
    death = format(death, ',')
    released = format(released, ',')
    date = data_week[-2]['S_DT']
    value = {'T_HJ':format(int(today['T_HJ']), ','), 'N_HJ':format(int(today['N_HJ']), ','),
             'DEATH':format(int(today['DEATH']), ','), 'RECOVER':format(int(today['RECOVER']), ',')}

    context = {"today":today, "data_week":data_week, "data_list":data_list, 'death':death, 'released':released,
               'vaccine_today':vaccine_today, 'vaccine':vaccine, 'value':value, 'date':date}
    return render(request, 'home.html', context)