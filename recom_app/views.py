from django.shortcuts import render
from .scripts.mc_basic_retrieval_tr import runall
from django.http import HttpResponse
import tensorflow as tf
from .forms import TextForm
from rest_framework.decorators import api_view
from .scripts.cover import get_cover
import json

def index(request):
    return HttpResponse("Hello, world. Look at urls py and views for other links.")

@api_view(['GET', 'POST'])
def onerial(request):

    """ 
    filmList = [
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
    """
    filmList = request.GET.get('filmList', '')
    filmList = json.loads(filmList)
    yeni_girdi_list = []

    for film in filmList:
        yeni_girdi_list.append(
            {"movie_title": film,"user_id": "12345678"})


    oneriler=runall(yeni_girdi_list)
    oneriler_decoded=[]
    for x in range(10):
        #print(oneriler[0,x])
        oneriler_decoded.append(oneriler[0,x].numpy().decode("utf-8") )
    return results(request,oneriler_decoded)
    return HttpResponse(oneriler_decoded)
    

def filmler(request):
    form = TextForm()
    return render(request, 'recom_app/home.html', {'form': form})

def printLikes(request):
    filmList = request.GET.get('filmList', '')
    print(filmList)
    return HttpResponse(filmList)

def results(request,films):
    print("Downloading images. This can take some time")
    for film in films:
        get_cover(film)
    #films = ["lorem1","The Dark Knight"]
    films = [film+".jpg" for film in films ]
    return render(request, 'recom_app/results.html', {'films': films})

def results_mock(request):
    films =['Sphere (1998)', 'Titanic (1997)', 'Anastasia (1997)', 'Blues Brothers 2000 (1998)', 'For Richer or Poorer (1997)', 'Spice World (1997)', 'Good Will Hunting (1997)', 'Half Baked (1998)', 'Fallen (1998)', 'Dark City (1998)']
    films = [film+".jpg" for film in films ]
    return render(request, 'recom_app/results.html', {'films': films})