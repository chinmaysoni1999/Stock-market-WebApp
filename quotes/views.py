from django.shortcuts import render
from .models import Tickers
import requests
import json

def home(request):
    tickers = Tickers.objects.all()
    all_tickers = []
    for i in tickers:
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+str(i)+'/quote?token=pk_3f723762156246aa8395298a377c3a67')
        try:
            api = json.loads(api_request.content)
            all_tickers.append(api)
        except Exception as e:
            api = 'Error'

    return render(request,'quotes/home.html',{'all_tickers':all_tickers})

def about(request):
    return render(request,'quotes/about.html',{})
