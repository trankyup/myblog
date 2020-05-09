from django.urls import path

from . import  views

urlpatterns = [
    path('index/', views.index),#用^$约束空字符串
]
