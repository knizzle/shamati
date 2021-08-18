from django.db.models import query
from rest_framework import generics

from dictionary.models import HebWord, Phonemes, HebLetter
from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer

class DictionaryViewSet(generics.ListAPIView):
    queryset = HebWord.objects.all()
    serializer_class = DictionarySerializer


class SoundsViewSet(generics.ListAPIView):
    queryset = Phonemes.objects.all()
    serializer_class = SoundsSerializer

class LettersViewSet(generics.ListAPIView):
    queryset = HebLetter.objects.all()
    serializer_class = LettersSerializer