from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello Page home page</h1>')


def news(request):
    return HttpResponse('<h1>Hello Page News</h1>')


def inobat(request):
    return HttpResponse('<h1>Hello</h1>')
