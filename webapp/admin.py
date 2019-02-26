from django.contrib import admin

from .models import Record, RecordType

admin.site.register(RecordType)
admin.site.register(Record)