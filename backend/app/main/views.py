from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, get_user
from account.processor import is_authenticated_decorator
from django.http import JsonResponse


def get_filter(request):
    """
    На вход принимаем какую страницу запрашиваем.
    На выходе фильтры для конкретного пользователя на основе его опыта
    :param request:
    :return:
    """
    data = {
        'orders': [
            'Категория',
            'Вид туризма',
            'На расстоянии',
            'Избранные',
            'Сезонность',
            'Теги'
        ],
        'filters': {
            'Категория': [
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
            'Категория': [
                'Памятник'
            ],
            'Теги': [
                'Экстрим'
            ]
        }
    }
    return JsonResponse(data)


def get_places(request):
    """
    На вход принимаем какие фильтры выбрал пользователь.
    На выходе набор статей с учетом пользовательского опыта
    :param request:
    :return:
    """
    data = {
        'posts': [
            {
                'Фото': 'data',
                'Название': 'text',
                'Категория': 'text',
                'Оценка': 'text',
                'Избрано': True
            },
            {
                'Фото': 'data',
                'Название': 'text',
                'Категория': 'text',
                'Оценка': 'text',
                'Избрано': False
            },

            {
                'Фото': 'data',
                'Название': 'text',
                'Категория': 'text',
                'Оценка': 'text',
                'Избрано': False
            },

            {
                'Фото': 'data',
                'Название': 'text',
                'Категория': 'text',
                'Оценка': 'text',
                'Избрано': False
            },

            {
                'Фото': 'data',
                'Название': 'text',
                'Категория': 'text',
                'Оценка': 'text',
                'Избрано': True
            }
        ]
    }
    return JsonResponse(data)


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')
