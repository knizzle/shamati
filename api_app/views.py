from rest_framework import generics

from dictionary.models import HebWord, Phonemes
from .serializers import DictionarySerializer

class DictionaryViewSet(generics.ListAPIView):
    queryset = Phonemes.objects.all()
    serializer_class = DictionarySerializer
