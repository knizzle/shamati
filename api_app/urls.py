from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HebString, HebWord

router = DefaultRouter()

urlpatterns = [
    path('hebstring/lookup/', HebString.as_view()),
    path('hebstring/<str:input_word>/', HebString.as_view()),
]

