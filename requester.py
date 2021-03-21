import requests
import json

URL = "https://weather-report-predprof.herokuapp.com/"

def getCityNameById(id):
    if id == "Алмазный": return 0
    elif id ==  "Западный": return 1
    elif id == "Курортный": return 2
    elif id =="Лесной"   : return 3
    elif id =="Научный"  : return 4
    elif id =="Полярный"  : return 5
    elif id =="Портовый" : return 6
    elif id =="Приморский": return 7
    elif id =="Садовый"  : return 8
    elif id =="Степной"  : return 9
    elif id == "Таежный" : return 10
    elif id ==  "Южный"  : return 11
    elif id == "Северный" : return 12

def getPredictionForDay(city, day):
    cityName = getCityNameById(city)
    response = requests.get(URL + f"getPredictionForDay/{cityName}/{day}")
    return json.loads(response.text)

def getPredictionForMonth(city, month):
    cityName = getCityNameById(city)
    response = requests.get(URL + f"getPredictionForMonth/{cityName}/{month}")
    return json.loads(response.text)

def getPredictionForYear(city):
    cityName = getCityNameById(city)
    response = requests.get(URL + f"getPredictionForYear/{cityName}")
    return json.loads(response.text)