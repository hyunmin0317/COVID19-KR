import requests
from django.test import TestCase

URL = 'https://raw.githubusercontent.com/jooeungen/coronaboard_kr/master/kr_daily.csv'
req = requests.get(URL).text.split("\n")
yesterday = req[-2].split(",")
today = req[-1].split(",")

test = [int(today[4]), int(today[4])-int(yesterday[4])]
critical = [int(today[-1]), int(today[-1]) - int(yesterday[-1])]

print(test)
print(critical)