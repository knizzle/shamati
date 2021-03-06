from rest_framework.views import APIView
from rest_framework.response import Response

from dictionary.models import HebWord, Phonemes

import itertools


class HebString(APIView):

    def get(self, request, format=None):
        return Response()
        
    def post(self, request, format=None):
        heb_list = []
        input_word = request.data['phonemes']
        print(input_word)
        for input_letter in input_word:
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
        print(heb_list)
        results = list(itertools.product(*heb_list))
        print(results)
        for result in results:
            result = ''.join(result)
            results_list.append(result)
            print(result)
        # start with another empty list
        dict_results = []
        # iterate over results_list
        for result in results_list:
            # for each word, get the record (.first())
            hebword = HebWord.objects.filter(word=result).first()
            if hebword is None:
                # if there isn't a record, add a dictionary to dict_results with 'valid': False
                dict_results.append({
                    'word': result,
                    'valid': False,
                    'root': '',
                    'partOfSpeech': '',
                    'definition': 'n/a'
                })
            # if there is a record, add a dictionary to dict_results with 'valid': True
            else:
                dict_results.append({
                    'word': result,
                    'valid': True,
                    'root': hebword.root,
                    'partOfSpeech': hebword.partOfSpeech,
                    'definition': hebword.definition
                })
        return Response(dict_results)
        
