from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecordList, RecordDetail

urlpatterns = [
    path('records/', RecordList.as_view()),
    path('records/<int:pk>/', RecordDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
