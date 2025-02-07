from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        file_reader = csv.DictReader(csvfile)
        content = list(file_reader)

    paginator = Paginator(content, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page ,
        'page': page,
    }
    return render(request, 'stations/index.html', context)