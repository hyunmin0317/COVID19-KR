from django.shortcuts import render
import requests
import datetime


def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data


def covid19_data():
    URL = 'https://raw.githubusercontent.com/jooeungen/coronaboard_kr/master/kr_daily.csv'
    req = requests.get(URL).text.split("\n")
    yesterday = req[-2].split(",")
    today = req[-1].split(",")
    cri = int(today[-1]) - int(yesterday[-1])

    if cri >= 0:
        crit = "+" + format(cri, ',')
    else:
        crit = format(cri, ',')

    critical = [format(int(today[-1]), ','), crit]
    return critical


def home(request):
    data_year = covid19_API(365)
    today, yesterday = data_year[0], data_year[1]
    critical = covid19_data()

    for data in data_year:
        data['W_DT'] = data['S_DT'][5:10]
        data['Y_DT'] = datetime.datetime.strptime(data['S_DT'],"%Y.%m.%d.%H").strftime('%Y-%m-%d')
    value = {'T_HJ':format(int(today['T_HJ']), ','), 'N_HJ':format(int(today['N_HJ']), ','), 'T_DT':today['T_DT'][:11], 'S_DT':data_year[0]['W_DT'],
             'T_DEATH':format(int(today['DEATH']), ','), 'N_DEATH': format(int(today['ALL_DAY_DEATH'])), 'T_CRI':critical[0], 'N_CRI':critical[1]}
    data_week = list(map(lambda x: [x['W_DT'], int(x['N_HJ']), int(x['N_HJ'])], data_year[:7]))
    data_year = list(map(lambda x: [x['Y_DT'], int(x['N_HJ'])], data_year))
    data_week.reverse()

    context = {"data_week":data_week, "data_year":data_year, 'value':value}
    return render(request, 'home.html', context)
