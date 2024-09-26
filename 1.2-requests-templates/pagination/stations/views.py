from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, newline='') as csvfile:
    file_reader = csv.DictReader(csvfile)
    CONTENT = [str(i) for i in file_reader]


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    paginator = Paginator(CONTENT, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page ,
        'page': page,
    }
    return render(request, 'stations/index.html', context)