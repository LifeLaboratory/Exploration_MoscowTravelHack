from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.get_filter, name='Получение списка фильтров'),
    path('posts/', views.get_places, name='Получение списка мест'),
    path('event/', views.get_event, name='Получение события'),
    path('recently_read/', views.recently_read, name='Недавно прочитанные посты'),
]
