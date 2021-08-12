from django.urls import path

from .views import DictionaryViewSet

urlpatterns = [
    path('', DictionaryViewSet.as_view()),
]
