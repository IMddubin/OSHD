#!/usr/bin/python3
import requests  # http 요청용 모듈
import json  # json 파일 변환용 모듈
import xmltodict


def get_weather():  # 날씨 정보 파싱용 함수
    API_KEY = "a9cb3f5a1ae7443549a23f5b794a71c8"  # openweathermap에서 발급받은 API키 입력
    API_ADDRESS = "http://api.openweathermap.org/data/2.5/weather?q=Sejong&appid={}".format(API_KEY)  # API주소
    weather = {}  # 날씨 정보 저장용 dict생성
    response = requests.get(API_ADDRESS)  # 날씨 API에 정보 요청
    if response.status_code == 200:  # 상태코드가 200(정상) 이면
        weather_json = json.loads(response.text)  # weather정보를 불러옴
        weather['weather'] = weather_json['weather'][0]['main']  # weather_json 정보에서 메임 날씨 정보를 추출해서 weather에 저장
        weather['temp'] = weather_json['main']['temp'] - 273.15  # weather_json 정보에서 현재온도를 추출해서 weather에 저장
        print(weather)
        return weather  # 날씨 정보 반환
    else:  # http요청에 에러가 있으면
        return weather  # 비어있는 weather 요소 반환


def get_dust():  # 미세먼지 정보 파싱용 함수
    API_KEY = "A2RYVh03%2B1HXvwgk%2BGgYBIvg%2B7%2BR7Akl49LYhjpQqMp8n2DXK%2B%2BlU6CKujlrr5UkagT0O%2F1QYUO3WPCL1HXcIQ%3D%3D"  # data포털에서 발급받은 API키 입력
    API_ADDRESS = "http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?year=2022&pageNo=1&numOfRows=100&returnType=xml&serviceKey={}".format(API_KEY)

    response = requests.get(API_ADDRESS)  # 미세먼지 API에 http요청
    if response.status_code == 200:  # 상태코드가 200(정상)이면
        dust_data = xmltodict.parse(response.text)  # 미세먼지 정보 저장
        dust = dust_data['response']['body']['items']['item']['issueVal']  # 미세먼지 정보에서 pm10에 해당하는 미세먼지 추출
        print(dust)
        return int(dust)  # 미세먼지 수치 반환
    else:  # 요청에 에러가 있으면
        dust = None
        return dust

weather = get_weather()                             # 현재 날씨 정보 얻어오기
dust = get_dust()                                  # 현재 미세먼지 정보 얻어오기

if weather:
    str(weather['temp']) + "C"
else:
    print("Warning, no weather information found!")

if dust:  # 미세먼지 정보가 있으면
    if dust <= 30:
        print("좋음")
    elif dust > 30 and dust <= 80:
        print("보통")
    elif dust > 80 and dust <= 150:
        print("나쁨")
    elif dust > 150:
        print("매우나쁨")

else:  # 미세먼지 정보가 없으면
    print("Warning, no Dust information found!")  # 터미널창에 경고 문구 표시