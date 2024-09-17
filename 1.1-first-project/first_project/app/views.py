from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os 


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории':reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    offset = datetime.timezone(datetime.timedelta(hours=3))
    current_time = datetime.datetime.now(offset)
    msg = f'Текущее время: {current_time.strftime("%H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir(os.getcwd())
    msg = f'{files}'
    return HttpResponse(msg)
