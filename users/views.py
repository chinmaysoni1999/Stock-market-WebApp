from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,StockForm
from django.contrib.auth.decorators import login_required
from .models import Stocks
import requests
import json

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Succesfully registerd {username}")
            return redirect('home')

    else:
        form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})

    form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def login(request):
    return render(request,'users/login.html',{})

@login_required
def profile(request):
    tickers = Stocks.objects.filter(owner=request.user)
    all_tickers = []
    for i in tickers:
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+str(i)+'/quote?token=pk_3f723762156246aa8395298a377c3a67')
        try:
            api = json.loads(api_request.content)
            all_tickers.append(api)
        except Exception as e:
            api = 'Error'

    if request.method=='POST':
        form = StockForm(request.POST,instance=request.user)
        if form.is_valid():
            ticker1 = str(form.cleaned_data.get('ticker'))
            api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+ticker1+'/quote?token=pk_3f723762156246aa8395298a377c3a67')
            try:
                api = json.loads(api_request.content)
                stock_detail = Stocks(ticker=ticker1,owner=request.user)
                stock_detail.save()
                ticker = form.cleaned_data.get('ticker')
                messages.success(request,f"Succesfully added {ticker}")
                return redirect('profile')
            except Exception as e:
                messages.warning(request,f"{ticker1} doesn't exist")
                return redirect('profile')

    else:
        form = StockForm()
        return render(request,'users/profile.html',{'form':form,'all_tickers':all_tickers})
