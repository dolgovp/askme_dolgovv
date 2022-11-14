from django.shortcuts import render
from . import models
from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    context = {'question_item': question_item}
    return render(request, 'question.html',context=context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')
