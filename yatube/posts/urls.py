from django.urls import path
from . import views

urlpatterns = [
    path('group_list.html/', views.group_list),
    path('group/<slug:slug>/', views.group_posts),
    path('', views.index),
]
