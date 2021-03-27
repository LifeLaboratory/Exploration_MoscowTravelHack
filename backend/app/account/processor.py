"""TODO"""
from django.shortcuts import redirect
from django.contrib.auth import get_user

__author__ = 'Крылосов А.А.'


def is_authenticated_user(request):
    return get_user(request).is_authenticated


def is_authenticated_decorator(function):
    """Декоратор, чтобы не пускать неавторизованных пользователей"""
    def wrapper(request, *args, **kwargs):
        """Если пользователь авторизован -> вернем функцию, иначе переведем на страницу логина"""
        if is_authenticated_user(request):
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper
