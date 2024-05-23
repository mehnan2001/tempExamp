from django.urls import path, include
from webSite.views import *

urlpatterns = [
    path('', index, name='index'),
]
