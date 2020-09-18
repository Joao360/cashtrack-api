from rest_framework import serializers
from cashtrack.apps.records.models import Record
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True, view_name='record-detail', queryset=Record.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'records']
        
class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)