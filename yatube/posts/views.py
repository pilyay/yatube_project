from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''Main page.'''
    return HttpResponse('Главная страница. 👋')

def group_posts(request, slug):
    '''Posts page.'''
    return HttpResponse('Скоро здесь будут посты.')
