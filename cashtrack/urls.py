"""cashtrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.views import obtain_auth_token

from cashtrack.apps.records.views import RecordList, RecordDetail, CategoryList, CategoryDetail
from cashtrack.apps.users.views import signin, UserDetail


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('api_token_auth', request=request, format=format),
        'records': reverse('record-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format)
    })

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
    path('signin', signin),
    path('admin/', admin.site.urls),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('records/', RecordList.as_view(), name='record-list'),
    path('records/<int:pk>/', RecordDetail.as_view(), name='record-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
