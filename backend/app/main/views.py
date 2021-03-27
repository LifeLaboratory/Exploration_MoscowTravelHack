from django.shortcuts import render, redirect, Http404
from django.http import JsonResponse
from main.base.provider import Provider
from django.views.decorators.csrf import csrf_exempt


def get_filter(request):
    """
    На вход принимаем какую страницу запрашиваем.
    На выходе фильтры для конкретного пользователя на основе его опыта
    :param request:
    :return:
    """
    data = {
        'orders': [
            'category',
            'Вид туризма',
            'На расстоянии',
            'Избранные',
            'Сезонность',
            'Теги'
        ],
        'filters': {
            'category': [
                'Ресторан',
                'Памятник',
                'Площадь'
            ],
            'Вид туризма': [
                'Пеший',
                'На автомобиле'
            ],
            'На расстоянии': [
                'Пеший',
                'На автомобиле'
            ],
            'Избранные': True,
            'Теги': [
                'Горные лыжи',
                'Досуг',
                'Экстрим'
            ],
            'Сезонность': [
                'Зима',
                'Весна',
                'Лето',
                'Осень'
            ]
        },
        'default_filters': {
            'category': [
                'Памятник'
            ],
            'Теги': [
                'Экстрим'
            ]
        }
    }
    return JsonResponse(data)


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
    На выходе набор статей с учетом пользовательского опыта
    :param request:
    :return:
    """
    posts_data = Provider('main/sql').exec_by_file('get_places.sql', {})

    return JsonResponse({'posts': posts_data})


def get_trips(request):
    trips_data = Provider('main/sql').exec_by_file('get_trips.sql')
    return JsonResponse({'trips': trips_data})


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


@csrf_exempt
def insert_statistics(request):
    if request.method == 'POST':
        id_user = get_user(request).get('id')
        Provider('main/sql').exec_by_file('insert_statistics.sql', {
            'id_user': id_user,
            'id_posts': request.GET.get('id_posts'),
            'percent': request.GET.get('percent'),
            'type': request.GET.get('type') or 'place',
        })
    return JsonResponse({'result': 'ok'})


@csrf_exempt
def insert_user(request):
    if request.method == 'POST':
        Provider('main/sql').exec_by_file('insert_user.sql', {
            'sign_hash': request.META.get('HTTP_SESSION')
        })
    return JsonResponse({'result': 'ok'})
