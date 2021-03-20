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
        fields = ('title', 'text', 'image',
                  'created_date', 'published_date')

    #category_data = Category.objects.all()
  #  category_choice = {}
   # for category in category_data:
   #     category_choice[category] = category
   # category = forms.ChoiceField(
    #    label="カテゴリ", widget=forms.Select, choices=list(category_choice.items()))

   # title = forms.CharField(max_length=30, label='タイトル')
   # content = forms.CharField(label="内容", widget=forms.Textarea())
   # image = forms.ImageField(label="イメージ画像", required=False)
