#d7452bd969c04438b6872642220606 weather api

import requests
import json

info = '''
1. Seoul
2. Pusan
3. Gwangju
'''
print(info)
inputVal = input('번호를 입력하세요:')
cityName = 'Seoul'
if int(inputVal) == 2:
    cityName = 'Pusan'
elif int(inputVal) == 3:
    cityName == 'Gwangju'
else:
    cityName == 'Seoul'

response = requests.get('https://api.weatherapi.com/v1/current.json?key=d7452bd969c04438b6872642220606&q='
                        + cityName +'&aqi=yes')
jsonObj = json.loads(response.text)

print(cityName, '의 기온은',jsonObj['current']['temp_c'], '기상상태는',jsonObj['current']['condition']['text'],'미세먼지는 '
      , jsonObj['current']['air_quality']['pm10'])
