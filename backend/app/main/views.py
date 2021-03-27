from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, get_user
from account.processor import is_authenticated_decorator


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')
