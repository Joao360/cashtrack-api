from datetime import datetime

from django import forms

from .models import Record

class DateTimeLocalField(forms.Field):
    def to_python(self, value):
        if not value:
            return datetime.now()
        return datetime.strptime(value, "%Y-%m-%dT%H:%M")

    def validate(self, value):
        super().validate(value)

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
