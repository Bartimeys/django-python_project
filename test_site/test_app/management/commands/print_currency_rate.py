from django.core.management.base import BaseCommand, CommandError
import requests
import json



class Command(BaseCommand):
    help = 'Get currenices'

    def handle(self, *args, **options):
        url = 'http://www.apilayer.net/api/live?access_key={0}&format=1'
        accestoken = 'f28733e4475f61ef6f4928c4a969cfa1'
        jsonObj = requests.get(url.format(accestoken)).text
        entrie = json.loads(jsonObj)
        for key in entrie['quotes']:
            if key == 'USDUAH':
                print "1 USD is",entrie['quotes'][key],"UAH"
            elif key =='USDRUB':
                print "1 USD is",entrie['quotes'][key],"RUB"
            elif key == 'USDGBP':
                print "1 USD is",entrie['quotes'][key],"GBP"
            elif key =='USDPLN':
                print "1 USD is",entrie['quotes'][key],"PLN"
            elif key == 'USDEUR':
                print "1 USD is",entrie['quotes'][key],"EUR"
            elif key == 'USDEUR':
                print "1 USD is",entrie['quotes'][key],"EUR"
            elif key =='USDBYR':
                print "1 USD is",entrie['quotes'][key],"BYR"
            elif key == 'USDJPY':
                print "1 USD is",entrie['quotes'][key],"JPY"
            elif key =='USDDJF':
                print "1 USD is",entrie['quotes'][key],"DJF"
            elif key =='USDCAD':
                print "1 USD is",entrie['quotes'][key],"CAD"
#cmd = Command()
#cmd.handle()