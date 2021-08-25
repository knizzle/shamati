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

from dictionary.models import HebWord, Phonemes, HebLetter
from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer

import itertools

user_entry = [['ד'], ['א', 'ה', 'ע', ''], ['ף']]

results = list(itertools.product(*user_entry))
print(results)

for result in results:
    result = ''.join(result)
    print(result)


class HebString(APIView):

    def get(self, request, input_word, user_entry):
        # all_phonemes = Phonemes.objects.get(text=soundlookup).hebletter.values()
        # phoneme_output = ', '.join([str(item) for item in all_phonemes])

        # build up list of possible hebrew letters for each phoneme
        # generate combinations of hewbrew letters
        # check if each hebrew letter is in the database (check if its a real word)
        # return a list of hebrew words

        print(input_word)
        return Response(hebrew_words)
        
    def post(self, request):
        print(request.data)
        return Response(request.data)
