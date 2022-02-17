from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv

list_content = []
with open('C:\\Users\\myelu\\Desktop\\HWorks\\django_hw\\1_lesson\\dj-homeworks\\1.2-requests-templates\\pagination\\data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    content = csv.DictReader(csvfile)
    for row in content:
        list_content.append([row['Name'], row['Street'], row['District']])


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_content, 10)
    page = paginator.get_page(page_number)
    context = {
            'bus_stations': page.object_list,
            'page': page,
            }
    return render(request, 'stations/index.html', context)
