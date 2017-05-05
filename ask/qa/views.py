from django.shortcuts import render

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK!!!1')


def login(request):
    return render(request, 'qa/login.html', {})


def index(request):
    return render(request, 'qa/index.html', {})