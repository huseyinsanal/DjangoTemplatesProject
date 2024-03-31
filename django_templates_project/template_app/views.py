from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,"template_app/first.html")

def weather_view(request):
    weather_dictionary = {
        "İstanbul" : "30",
        "Amsterdam" : "20",
        "Paris" : [10,14,20,21],
        "Rome" : {"Morning" : 10, "Evening" : 20}   
        }
    
    return render(request,"template_app/weather.html",context=weather_dictionary)