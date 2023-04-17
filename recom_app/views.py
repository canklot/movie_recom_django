from django.shortcuts import render
from .scripts.mc_basic_retrieval_tr import runall
from django.http import HttpResponse
import tensorflow as tf
from .forms import TextForm
import json

def index(request):
    return HttpResponse("Hello, world. Look at urls py and views for other links.")

def run(request):

    """ yeni_girdi_list = [
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
    ] """
    filmList = request.GET.get('filmList', '')
    filmList = json.loads(filmList)
    yeni_girdi_list = []

    for film in filmList:
        yeni_girdi_list.append(
            {"movie_title": film,"user_id": "12345678"})


    oneriler=runall(yeni_girdi_list)
    oneriler_string=""
    for x in range(10):
        #print(oneriler[0,x])
        oneriler_string += oneriler[0,x].numpy().decode("utf-8") +"<br>"
    return HttpResponse(oneriler_string)
    

def filmler(request):
    if request.method != 'POST':
        form = TextForm()
        return render(request, 'recom_app/home.html', {'form': form})

def printLikes(request):
    filmList = request.GET.get('filmList', '')
    print(filmList)
    return HttpResponse(filmList)