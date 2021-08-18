from django.db.models import query
from rest_framework import generics, viewsets

from dictionary.models import HebWord, Phonemes, HebLetter
from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer

class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = HebWord.objects.all()
    serializer_class = DictionarySerializer


class SoundsViewSet(viewsets.ModelViewSet):
    queryset = Phonemes.objects.all()
    serializer_class = SoundsSerializer

class LettersViewSet(viewsets.ModelViewSet):
    queryset = HebLetter.objects.all()
    serializer_class = LettersSerializer