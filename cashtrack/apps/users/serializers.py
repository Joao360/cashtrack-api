from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from cashtrack.apps.records.models import Record

class UserSerializer(HyperlinkedModelSerializer):
    records = HyperlinkedRelatedField(many=True, view_name='record-detail', queryset=Record.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'records']
        