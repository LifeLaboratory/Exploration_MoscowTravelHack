from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.get_filter, name='Получение списка фильтров'),
    path('posts/', views.get_places, name='Получение списка мест'),
    path('posts/<int:post_id>', views.get_current_places, name='Получение конкретного места'),
    path('statistics/', views.insert_statistics, name='Записать статистику'),
    path('user/', views.insert_user, name='Записать пользователя'),
    path('favorites/', views.favorites, name='Записать в избранное'),
    path('favorites/delete', views.delete_favorite, name='удалить запись из избранного'),
    path('event/', views.get_event, name='Получение события'),
    path('recently_read/', views.recently_read, name='Недавно прочитанные посты'),
    path('user_tags/', views.get_tags_by_user, name='Текущие интересы пользователя'),
]
