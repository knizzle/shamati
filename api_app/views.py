# from django.db.models import query
# from rest_framework import generics, viewsets

# from dictionary.models import HebWord, Phonemes, HebLetter
# from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer

# class DictionaryViewSet(viewsets.ModelViewSet):
#     queryset = HebWord.objects.all()
#     serializer_class = DictionarySerializer

# class SoundsViewSet(viewsets.ModelViewSet):
#     queryset = Phonemes.objects.all()
#     serializer_class = SoundsSerializer

# class LettersViewSet(viewsets.ModelViewSet):
#     queryset = HebLetter.objects.all()
#     serializer_class = LettersSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

import nltk

from dictionary.models import HebWord, Phonemes, HebLetter
from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer


class HebString(APIView):

    def get(self, request, soundlookup, format=None):
        all_phonemes = Phonemes.objects.get(text=soundlookup).hebletter.values()
        phoneme_output = ', '.join([str(item) for item in all_phonemes])
        return Response(all_phonemes)

