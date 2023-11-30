from django.urls import path
from index.views import *

urlpatterns = [
    path('', index),
    path('news/', news),
    path('inobat/', inobat),
    path('hello/',news)
]