from django.urls import path
from index.views import *

urlpatterns = [
    path('news/', news),
]