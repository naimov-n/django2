from django.shortcuts import render
from django.http import HttpResponse
from index.models import *

def index(request):
    social = Social.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    news = News.objects.filter(status=True)
    return render(request, 'index/index.html', {'social': social, 'category': category, 'news': news})


def news(request, id):
    social = Social.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    news = News.objects.get(pk=id)
    return render(request, 'index/simple.html', {'social': social, 'category': category, 'news': news})


def inobat(request):
    return HttpResponse('<h1>Hello</h1>')


def contact(request):
    return HttpResponse('<h1>Contacts here</h1>')