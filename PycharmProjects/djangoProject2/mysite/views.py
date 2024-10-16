from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mysite/index.html')


def about(request):
    return render(request, 'mysite/about.html')
