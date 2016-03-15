from django.core.management.base import BaseCommand, CommandError
import requests
import json



class Command(BaseCommand):
    help = 'Get weather by country '

    def handle(self, *args, **options):
        country=raw_input("Please enter your country: ")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'
        appid = 'b1b15e88fa797225412429c1c50c122a'
        jsonData = requests.get(url.format(country,appid)).text
        appData = json.loads(jsonData)
        for key in appData['weather']:
            print "Today are",appData['weather'][0]['main']
            print "Weather is ",appData['weather'][0]['description']
        for el in appData['main']:
            if el == 'humidity':
                print appData['main'][el],"humidity"
        for item in appData:
            if item == 'name':
                print appData[item]
        for elem in appData['wind']:
            if elem == 'speed':
                print appData['wind'][elem],"m/s speed of wind"
