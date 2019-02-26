from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Record
from .forms import ExpenseForm

def index(request):
    latest_records_list = Record.objects.order_by('datetime')[:5]
    expenseForm = ExpenseForm()

    context = {
        'latest_records_list': latest_records_list,
        'expenseForm': expenseForm
    }
    
    return render(request, 'webapp/index.html', context)

def records(request):
    # Record.objects.create(ammount=request.POST['ammount'])
    form = ExpenseForm(request.POST)
    if form.is_valid():
        record = form.save(commit=False)
        record.save()

    return redirect('index')