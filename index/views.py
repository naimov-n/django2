from django.shortcuts import render
from django.http import HttpResponse


def news(request):
    return HttpResponse('<h1>Hello news</h1>')
