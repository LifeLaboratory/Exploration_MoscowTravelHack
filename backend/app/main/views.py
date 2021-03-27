from django.shortcuts import render, redirect, Http404
from django.http import JsonResponse
from main.base.provider import Provider
from backend.app.main.filter.provider import Provider as FilterProvider
import requests


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


def get_filter(request):
    """
    На вход принимаем какую страницу запрашиваем.
    На выходе фильтры для конкретного пользователя на основе его опыта
    :param request:
    :return:
    """
    # data = {
    #     'orders': [
    #         'category',
    #         'Вид туризма',
    #         'На расстоянии',
    #         'Избранные',
    #         'Сезонность',
    #         'Теги'
    #     ],
    #     'filters': {
    #         'category': [
    #             'Ресторан',
    #             'Памятник',
    #             'Площадь'
    #         ],
    #         'Вид туризма': [
    #             'Пеший',
    #             'На автомобиле'
    #         ],
    #         'На расстоянии': [
    #             'Пеший',
    #             'На автомобиле'
    #         ],
    #         'Избранные': True,
    #         'Теги': [
    #             'Горные лыжи',
    #             'Досуг',
    #             'Экстрим'
    #         ],
    #         'Сезонность': [
    #             'Зима',
    #             'Весна',
    #             'Лето',
    #             'Осень'
    #         ]
    #     },
    #     'default_filters': {
    #         'category': [
    #             'Памятник'
    #         ],
    #         'Теги': [
    #             'Экстрим'
    #         ]
    #     }
    # }
    return JsonResponse(FilterProvider().get_filter())


def get_places(request):
    """
    На вход принимаем какие фильтры выбрал пользователь.
    На выходе набор статей с учетом пользовательского опыта
    :param request:
    :return:
    """
    posts_data = Provider('main/sql').exec_by_file('get_places.sql', {})

    return JsonResponse({'posts': posts_data})


def get_trips(request):
    trips_data = Provider('main/sql').exec_by_file('get_trips.sql')
    return JsonResponse({'trips': trips_data})


def get_event(request):
    events_data = Provider('main/sql').exec_by_file('get_event.sql')
    return JsonResponse({'events': events_data})


def get_google_info():
    """Метод запрашивает рейтинги мест в google по координатам мест"""
    places = Provider('main/sql').exec_by_file('get_places.sql', {})
    google_key = ''
    for place in places:
        try:
            id_place = place['id']
            lat = place['latitude']
            long = place['longitude']
            r = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=100&key={google_key}')
            try:
                rating = r.json()['results'][0]['rating']
            except:
                rating = 0
            Provider('main/sql').exec_by_file('insert_ratings.sql', {
                'id': id_place,
                'rating': rating,
            })
        except:
            pass
