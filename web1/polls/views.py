# Vantage apikey=6O76G8ISWG17Q90H
# World trading data apikey=VNVp92kSb0N61VlHVn4YdnkGqxxcmib1fbpUXFJRybMOvVFppziMKaj8AtQx
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render, redirect
import requests 
from django.http import *
from .models import *
from .forms import * 
from django.contrib.auth.models import User
#print(datetime.date(datetime.now()))
def index(request):
	url = 'https://api.iextrading.com/1.0/stock/amzn/ohlc'
	city = 'Amazon'
	r = requests.get(url.format(city)).json()
	company = {
            'city' : city,
            'open' : r['open']['price'],
            'high' : r['high'],
            'low' : r['low'],
            'close' : r['close']['price'],
        }

	url1 = 'https://api.iextrading.com/1.0/stock/msft/ohlc'
	city1 = 'Microsoft'
	r = requests.get(url1).json()
	company1 = {
            'city1' : city1,
            'open' : r['open']['price'],
            'high' : r['high'],
            'low' : r['low'],
            'close' : r['close']['price'],
        }
    
	#print(company)
	return render(request,'weath.html',{'company' : company,'company1' : company1})

def index1(request):
    url2 = 'https://api.iextrading.com/1.0/stock/infy/ohlc'
    city2 = 'Infosys'
    r = requests.get(url2.format(city2)).json()
    company = {
            'city' : city2,
            'open' : r['open']['price'],
            'high' : r['high'],
            'low' : r['low'],
            'close' : r['close']['price'],
        }

    url3 = 'https://api.iextrading.com/1.0/stock/acn/ohlc'
    city3 = 'Accenture'
    r = requests.get(url3).json()
    company1 = {
            'city1' : city3,
            'open' : r['open']['price'],
            'high' : r['high'],
            'low' : r['low'],
            'close' : r['close']['price'],
        }
    
    #print(company)
    return render(request,'india.html',{'company' : company,'company1' : company1})

def index2(request):
    url2 = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=btc&to_currency=usd&apikey=6O76G8ISWG17Q90H'
    r = requests.get(url2).json()
    company = {
            'city' : r['Realtime Currency Exchange Rate']['2. From_Currency Name'],
            'open' : r['Realtime Currency Exchange Rate']['5. Exchange Rate'],
            'date1' : r['Realtime Currency Exchange Rate']['6. Last Refreshed'],
            #'low' : r['low'],
            #'close' : r['close']['price'],print(datetime.date(datetime.now()))
        }

    url3 = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=eth&to_currency=usd&apikey=6O76G8ISWG17Q90H'
    r = requests.get(url3).json()
    company1 = {
            'city1' : r['Realtime Currency Exchange Rate']['2. From_Currency Name'],
            'open' : r['Realtime Currency Exchange Rate']['5. Exchange Rate'],
            'date1' : r['Realtime Currency Exchange Rate']['6. Last Refreshed'],
            #'low' : r['low'],
            #'close' : r['close']['price'],
        }

    url4 = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=bch&to_currency=usd&apikey=6O76G8ISWG17Q90H'
    r = requests.get(url4).json()
    company2 = {
            'city1' : r['Realtime Currency Exchange Rate']['2. From_Currency Name'],
            'open' : r['Realtime Currency Exchange Rate']['5. Exchange Rate'],
            'date1' : r['Realtime Currency Exchange Rate']['6. Last Refreshed'],
            #'low' : r['low'],
            #'close' : r['close']['price'],
        }
    return render(request,'crypto.html',{'company' : company,'company1' : company1,'company2' : company2})


def stocks(request):
    return render(request, 'stocks.html')
