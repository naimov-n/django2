from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello Page home page</h1>')


def news(request):
    return HttpResponse('<h1>Hello Page News</h1>')

def hello(request):
    return HttpResponse('<h1>Hello Page hello</h1>')