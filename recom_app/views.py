from django.shortcuts import render
from .scripts.mc_basic_retrieval_tr import runall
# Create your views here.
from django.http import HttpResponse
import tensorflow as tf


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def run(request):
    oneriler=runall()
    oneriler_string=""
    for x in range(10):
        #print(oneriler[0,x])
        oneriler_string += tf.compat.as_str_any(oneriler[0,x])
    return HttpResponse(oneriler_string)
