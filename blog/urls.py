# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 08:14:44 2021

@author: dev
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
