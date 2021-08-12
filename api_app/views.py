from rest_framework import generics

from dictionary.models import LatinScript, HebWord
from .serializers import DictionarySerializer

class DictionaryViewSet(generics.ListAPIView):
    queryset = LatinScript.objects.all()
    serializer_class = DictionarySerializer
