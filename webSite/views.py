from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'phon1': '0913-333-3333',
        'phon2': '0913-222-2222',
        'email': 'mehnan2001@gmail.com'
    }
    return render(request, 'index.html', context)
