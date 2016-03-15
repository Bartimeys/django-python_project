from django.core.management.base import BaseCommand, CommandError
import requests
import json


class Command(BaseCommand):
    help = 'Get currenices'

    def handle(self, *args, **options):
        url = 'http://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        jsonObj = requests.get(url).text
        entrie = json.loads(jsonObj)

        for key in entrie:
            print '{0} {1} {2}'\
                .format(key['txt'].encode('utf-8'), key['rate'], key['cc'], key['exchangedate'])

#cmd = Command()
#cmd.handle()
