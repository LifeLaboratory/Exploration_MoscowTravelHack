from django.shortcuts import render, redirect, Http404
from django.http import JsonResponse
from main.base.provider import Provider
from django.views.decorators.csrf import csrf_exempt
from main.filter.provider import Provider as FilterProvider
from main.recently_read.provider import Provider as RecentlyReadProvider
import requests


def get_filter(request):
    """
    На вход принимаем какую страницу запрашиваем.
    На выходе фильтры для конкретного пользователя на основе его опыта
    :param request:
    :return:
    """
    return JsonResponse(FilterProvider().get_filter())


def get_user(request):
    """
    Метод по Hash пользователя возвращает его ID
    :param request:
    :return:
    """
    posts_data = Provider('main/sql').exec_by_file('get_user.sql', {
        'sign_hash': request.META.get('HTTP_SESSION')
    })
    return posts_data[0]


def get_places(request):
    """
    На вход принимаем какие фильтры выбрал пользователь.
    И идентификатор пользователя
    На выходе набор статей с учетом пользовательского опыта
    """
    id_user = get_user(request).get('id')

    cities_filter = request.GET.get('Город')
    cities_condition = ''
    if cities_filter:
        cities_condition = f"and cities.title = '{cities_filter}'"

    category_filter = request.GET.get('Категории')
    category_condition = ''
    if category_filter:
        category_condition = f"and place_categories.title = '{category_filter}'"

    tourism_filter = request.GET.get('Вид туризма')
    tourism_condition = ''
    if tourism_filter:
        tourism_condition = f"and tourism_types.title = '{tourism_filter}'"

    season_filter = request.GET.get('Сезонность')
    season_condition = ''
    if season_filter:
        season_condition = f"and tourism_types.title = '{season_filter}'"



    posts_data = Provider('main/sql').exec_by_file('get_places.sql', {
        'id_user': id_user,
        'cities_condition': cities_condition,
        'category_condition': cities_condition,
        'tourism_condition': tourism_condition
    })

    return JsonResponse({'posts': posts_data})


def get_trips(request):
    """
    На вход принимаем какие фильтры выбрал пользователь.
    И идентификатор пользователя
    На выходе набор маршрутов с учетом пользовательского опыта
    """
    trips_data = Provider('main/sql').exec_by_file('get_trips.sql')
    return JsonResponse({'trips': trips_data})


def get_event(request):
    """
    На вход принимаем какие фильтры выбрал пользователь.
    И идентификатор пользователя
    На выходе набор афиш с учетом пользовательского опыта
    """
    events_data = Provider('main/sql').exec_by_file('get_event.sql')
    return JsonResponse({'events': events_data})


@csrf_exempt
def insert_statistics(request):
    if request.method == 'POST':
        id_user = get_user(request).get('id')

        exists = Provider('main/sql').exec_by_file('select_statistics.sql', {
            'id_user': id_user,
            'id_post': request.POST.get('id_post'),
        })
        if exists:
            Provider('main/sql').exec_by_file('update_statistics.sql', {
                'id_user': id_user,
                'id_post': request.POST.get('id_post'),
                'percent': request.POST.get('percent'),
                'type': request.POST.get('type') or 'place',
                'id_history': exists[0]['id']
            })
        else:
            Provider('main/sql').exec_by_file('insert_statistics.sql', {
                'id_user': id_user,
                'id_post': request.POST.get('id_post'),
                'percent': request.POST.get('percent'),
                'type': request.POST.get('type') or 'place',
            })
    return JsonResponse({'result': 'ok'})


@csrf_exempt
def insert_user(request):
    if request.method == 'POST':
        Provider('main/sql').exec_by_file('insert_user.sql', {
            'sign_hash': request.META.get('HTTP_SESSION')
        })
    return JsonResponse({'result': 'ok'})


def recently_read(request):
    return JsonResponse(RecentlyReadProvider().get_recently_read(), safe=False)


@csrf_exempt
def delete_favorite(request):
    if request.method == 'POST':
        id_user = get_user(request).get('id')
        Provider('main/sql').exec_by_file('delete_favorites.sql', {
            'id_user': id_user,
            'favoritable_id': request.POST.get('id_post')
        })
    return JsonResponse({'result': 'ok'})

@csrf_exempt
def favorites(request):
    if request.method == 'POST':
        id_user = get_user(request).get('id')
        exist = Provider('main/sql').exec_by_file('get_favorites_favoritable_id.sql', {
            'id_user': id_user,
            'favoritable_id': request.POST.get('id_post'),
        })
        if not exist:
            Provider('main/sql').exec_by_file('insert_favorites.sql', {
                'id_user': id_user,
                'id_post': request.POST.get('id_post'),
                'type': request.POST.get('type') or 'place',
            })
    elif request.method == "GET":
        id_user = get_user(request).get('id')
        favorites = Provider('main/sql').exec_by_file('get_favorites_posts.sql', {
            'id_user': id_user
        })
        return JsonResponse({'posts': favorites})

    return JsonResponse({'result': 'ok'})


@csrf_exempt
def get_favorites(request):
    Provider('main/sql').exec_by_file('get_favorites.sql', {
        'sign_hash': request.META.get('HTTP_SESSION')
    })
    return JsonResponse({'result': 'ok'})

