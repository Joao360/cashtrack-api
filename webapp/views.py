import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from .forms import RecordForm
from .models import Record, RecordType

def index(request):
    latest_records_list = Record.objects.order_by('-datetime')[:5]
    form = RecordForm()

    context = {
        'latest_records_list': latest_records_list,
        'form': form
    }
    
    return render(request, 'webapp/index.html', context)

""" 
    In case of success returns the created record in html format
"""
def records(request):
    data = json.loads(request.body)
    form = RecordForm(data)
    if form.is_valid():
        try:
            record = form.save(commit=False)
            record.recordType = RecordType.objects.get(pk=data['recordType'])
            record.save()
            return render(request, 'webapp/record.html', { 'record': record })
        except:
            return HttpResponseBadRequest('No record type with the name {name} was found'.format(name=data['recordType']))
    else:
        return HttpResponseBadRequest(form.errors)
