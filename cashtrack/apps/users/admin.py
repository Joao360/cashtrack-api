from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    list_display = ["date_joined", "email", "first_name", "last_name", "is_staff"]


admin.site.register(User, UserAdmin)
