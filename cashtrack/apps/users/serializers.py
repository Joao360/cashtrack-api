from django.contrib.auth.models import User
from rest_framework import serializers
from cashtrack.apps.records.models import Record

class UserSerializer(serializers.ModelSerializer):
    records = serializers.PrimaryKeyRelatedField(many=True, queryset=Record.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'records']