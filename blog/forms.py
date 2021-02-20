# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:15:44 2021

@author: dev
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)