from django.shortcuts import render
import requests
import datetime

def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data

def home(request):
    data_week, data_list = covid19_API(7), covid19_API(30)
    today, yesterday = data_week[0], data_week[1]
    data_week.reverse(), data_list.reverse()

    for data in data_week:
        data['S_DT'] = data['S_DT'][5:10]
    for data in data_list:
        data['S_DT'] = datetime.datetime.strptime(data['S_DT'],"%Y.%m.%d.%H").strftime('%Y-%m-%d')

    date = data_week[-1]['S_DT']
    death = format(int(today['DEATH']) - int(yesterday['DEATH']), ',')
    value = {'T_HJ':format(int(today['T_HJ']), ','), 'N_HJ':format(int(today['N_HJ']), ','),
             'T_DEATH':format(int(today['DEATH']), ','), 'N_DEATH': death, 'T_DT':today['T_DT'][:11], 'S_DT':date}

    context = {"data_week":data_week, "data_list":data_list, 'value':value}
    return render(request, 'home.html', context)