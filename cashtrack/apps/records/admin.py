from django.contrib import admin

from .models import Record, Category


class RecordAdmin(admin.ModelAdmin):
    class Meta:
        model = Record

    list_display = ["created_at", "money_deposit", "recordType", "category", "ammount", "datetime"]

admin.site.register(Category)
admin.site.register(Record, RecordAdmin)
