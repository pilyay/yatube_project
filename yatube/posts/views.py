from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''Main page.'''
    return HttpResponse('Главная страница. 👋')

def group_posts(request, slug):
    '''Posts page.'''
    return HttpResponse(
        '<!-- Вася! Здесь ничего не трогай, а то сломается! -->'
        '<h1>Заголовок страницы</h1>'
        '<h2>Заголовок подраздела страницы</h2>'
        '<h3>Заголовок подраздела подраздела страницы</h3>'
        '<a href="https://praktikum.yandex.ru/profile/backend-developer/">'
        'Начать учиться'
        '</a>'
        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br>'
        'если у тебя нет правильных <s>вопросов</s> запросов.'
        '<div class="alert alert-success">'
        '👍 👍 Правильно, как ты думаешь, с чем это связано?'
        '</div>'
        '<img src="https://2.downloader.disk.yandex.ru/preview/'
        'b0dd3567ec6b6076bf93e62b2db46b573f23ac1d603087bf7ad431'
        'bdd069894b/inf/zL7SMMzVbntySJ4KM8TC5tJDT45cfpirqJds04b'
        '4_Zk6XIyQOpegM82l0sLkgD-N3TVsjBJ1GS7WtV3-MSN5aw%3D%3D?'
        'uid=205113803&filename=Screenshot_25.png&disposition=i'
        'nline&hash=&limit=0&content_type=image%2Fpng&owner_uid'
        '=205113803&tknv=v2&size=1920x1096">'
        )
