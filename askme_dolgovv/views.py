from django.shortcuts import render
from . import models
from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    return render(request, 'question.html')


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')
