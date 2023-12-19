from django.shortcuts import render
from django.http import HttpResponse
from index.models import *

def index(request):
    return render(request, 'index/index.html')


def news(request):

    return render(request, 'index/simple.html')


def inobat(request):
    return HttpResponse('<h1>Hello</h1>')


def contact(request):
    return HttpResponse('<h1>Contacts here</h1>')