from rest_framework import serializers
from cashtrack.apps.records.models import Record
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='record-detail')
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'password', 'first_name', 'last_name', 'records']
        
class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)