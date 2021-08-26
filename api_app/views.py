from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from dictionary.models import HebWord, Phonemes, HebLetter
from .serializers import DictionarySerializer, SoundsSerializer, LettersSerializer

import itertools

# results = [['ד'], ['א', 'ה', 'ע', ''], ['ף']]
# results = [['ה', 'ח', 'כ', ''], ['ה', 'יי'], ['מ']]
# user_entry = ['sh', 'a', 'l', 'o', 'm']

class HebString(APIView):

    def get(self, request, input_word, format=None):
        # build up list of possible hebrew letters for each phoneme, see heb_keys func.
        # generate combinations of hebrew letters, see itertools example
        # check if each hebrew letter is in the database (check if its a real word)
        # return a list of hebrew words
        return Response()
        
    def post(self, request, format=None):
        heb_list = []
        input_word = request.data['phonemes']
        # print(input_word)
        for input_letter in input_word:
            # phoneme is something like 'a' or 'sh'
            # queryset_of_hebrew_letter__matches is something like 'א
            
            # fallback option: iterate over all the hebletters
            # check if each hebletter has a phoneme whose text is equal to our input letter
            # letter.phonemes_set.filter(text='a').exists()
            # letter.phonemes_set.filter(text__icontains='a').exists()

            phoneme = Phonemes.objects.filter(text=input_letter).first()
            if phoneme is None:
                print('phoneme not found')
                continue
            queryset_of_hebrew_letter__matches = phoneme.hebletter.all()
            heb_letters = []
            for hebletter in queryset_of_hebrew_letter__matches:
                heb_letters.append(hebletter.letter)
            heb_list.append(heb_letters)
        results_list = []
        # print(heb_list)
        results = list(itertools.product(*heb_list))
        # print(results)
        for result in results:
            result = ''.join(result)
            results_list.append(result)
            # print(result)
        return Response(results_list)
