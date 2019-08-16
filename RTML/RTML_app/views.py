from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django import forms
import datetime

# Create your views here.
@login_required
def home(request):
    #today=datetime.date.today()
    #serv_list=[]
    #for s in Service.objects.all():
    #    serv_list.append(s.Serv_name)
    #print(serv_list)
    return render(request,'RTML_app/Home.html')


def login(request):
    return render(request, 'RTML_app/login.html')

@login_required
def getTable(request):
    return render(request,'RTML_app/GetTable.html')
