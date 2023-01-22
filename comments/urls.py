from django.contrib import admin
from django.urls import path, include

from comments import views

urlpatterns = [
    path('', views.index, name='index'),
]
