from django.urls import path
from index.views import *

urlpatterns = [
    path('', index),
    path('news/<slug:id>', news),

]
