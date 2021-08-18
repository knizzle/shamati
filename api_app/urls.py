from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DictionaryViewSet, SoundsViewSet, LettersViewSet

router = DefaultRouter()
router.register('hebwords', DictionaryViewSet, basename='words')
router.register('phonemes', SoundsViewSet, basename='sounds')
router.register('hebletters', LettersViewSet, basename='letters')


urlpatterns = [
    path('', DictionaryViewSet.as_view()),
]
