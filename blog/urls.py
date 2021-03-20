# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 08:14:44 2021

@author: dev
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
