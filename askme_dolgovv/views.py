from django.shortcuts import render

from askme_dolgovv.settings import STATIC_ROOT, BASE_DIR


def index(request):
    return render(request, 'index.html')
