from django import forms

from .models import Record

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = (
            'recordType', 
            'ammount',
            'category',
            'entity',
            'datetime',
            'note'
        )