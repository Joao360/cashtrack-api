from django.shortcuts import render
from django.http import HttpResponse

from .models import Record


def index(request):
    latest_records_list = Record.objects.order_by('date')[:5]
    context = {'latest_records_list': latest_records_list}
    return render(request, 'webapp/index.html', context)

def records(request):
    latest_records_list = Record.objects.order_by('date')[:5]
    context = {'latest_records_list': latest_records_list}
    return render(request, 'webapp/index.html', context)