from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    questions = models.QUESTIONS
    return paginate(questions, request, 5)


def paginate(objects_list, request, per_page, info=''):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    print(request)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    if str(request).find('hot') > 0:
        return render(request, 'hot.html', {'page': page})
    elif str(request).find('tag') > 0:
        return render(request, 'tag_page.html', {'page': page, 'tag': info})
    else:
        return render(request, 'index.html', {'page': page})


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
        return paginate(questions_with_tag, request, 3, tag)


def hot(request):
    sorted_questions = sorted(models.QUESTIONS, key=lambda it: it['likes'], reverse=True)
    if len(sorted_questions) != 0:
        return paginate(sorted_questions, request, 3)
