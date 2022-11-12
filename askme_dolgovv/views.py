from django.shortcuts import render

from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    return render(request, 'index.html')


def question(request):
    return render(request, 'question.html')


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request, 'settings.html')
