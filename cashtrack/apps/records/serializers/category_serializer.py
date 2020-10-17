from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Category


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']
