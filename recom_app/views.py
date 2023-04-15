from django.shortcuts import render
from .scripts.mc_basic_retrieval_tr import runall
# Create your views here.
from django.http import HttpResponse
import tensorflow as tf


def index(request):
    return HttpResponse("Hello, world. Look at urls py and views for other links.")

def run(request):

    yeni_girdi_list = [
        {"movie_title": "Twelve Monkeys (1995)",
         "user_id": "12345678"},
        {"movie_title": "Terminator 2: Judgment Day (1991)",
         "user_id": "12345678"},
        {"movie_title": "Alien 3 (1992)",
         "user_id": "12345678"},
        {"movie_title": "Jurassic Park (1993)",
         "user_id": "12345678"},
        {"movie_title": "Men in Black (1997)",
         "user_id": "12345678"} 
    ]
    
    oneriler=runall(yeni_girdi_list)
    oneriler_string=""
    for x in range(10):
        #print(oneriler[0,x])
        oneriler_string += oneriler[0,x].numpy().decode("utf-8") +"<br>"
    return HttpResponse(oneriler_string)
    
    return render(request, 'recom_app/home.html')

