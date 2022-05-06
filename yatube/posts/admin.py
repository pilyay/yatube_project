'''Добавил из урока.'''
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    '''Настройка отображения модели в интерфейсе админки.'''
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
