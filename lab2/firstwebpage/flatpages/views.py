# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'static_handler.html')
def hello(request):
    title = 'Мой сайт'
    heading = 'Добро пожаловать на мой сайт!'
    content = 'Привет, Мир!'
    return render(request, 'home.html', {'title': title, 'heading': heading, 'content': content})



