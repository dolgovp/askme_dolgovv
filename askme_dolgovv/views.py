from django.shortcuts import render
from . import models
from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    context = {'question_item': question_item}
    return render(request, 'question.html', context=context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')


def tags(request, tag: str):
    questions_with_tag = list(filter(lambda question_t: question_t['tags'].count(tag) > 0, models.QUESTIONS))
    if len(questions_with_tag) != 0:
        context = {'questions_with_tag': questions_with_tag, "tag": tag}
        return render(request, 'tag_page.html', context=context)


def hot(request):
    sorted_questions = sorted(models.QUESTIONS, key=lambda it: it['likes'], reverse=True)
    if len(sorted_questions) != 0:
        context = {'sorted_questions': sorted_questions}
        return render(request, 'hot.html', context=context)


