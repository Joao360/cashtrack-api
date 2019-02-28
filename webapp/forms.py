from datetime import datetime

from django import forms

from .models import Record

"""
    It will serialize a string to datetime
"""
class DateTimeLocalField(forms.Field):
    def to_python(self, value):
        if not value:
            return datetime.now()
        return datetime.strptime(value, "%Y-%m-%dT%H:%M")

class RecordForm(forms.ModelForm):
    datetime = DateTimeLocalField()
    
    class Meta:
        model = Record
        fields = (
            'ammount',
            'category',
            'entity',
            'datetime',
            'note'
        )
