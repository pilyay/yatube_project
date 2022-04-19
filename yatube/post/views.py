'''В разработке.'''
# from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    '''Главная страница.'''
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    '''В разработке.'''
    return HttpResponse('Page 2')
