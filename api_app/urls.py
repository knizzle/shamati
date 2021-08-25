from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HebString

# from .views import DictionaryViewSet, SoundsViewSet, LettersViewSet

router = DefaultRouter()
# router.register('hebwords', DictionaryViewSet, basename='words')
# router.register('phonemes', SoundsViewSet, basename='sounds')
# router.register('hebletters', LettersViewSet, basename='letters')

# urlpatterns = router.urls

urlpatterns = [
    # path('hebstring/', HebString.as_view()),
    path('hebstring/<str:input_word>/', HebString.as_view()),
    # path('api_app/', HebString.as_view(), name='home.html')
]
