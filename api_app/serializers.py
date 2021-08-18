from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from dictionary.models import Phonemes, HebWord, HebLetter

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HebWord
        fields = (
            'word',
            'transliteration',
            'root',
            'partOfSpeech',
            'definition',
        )

class SoundsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Phonemes
        fields = ('text', 'hebletter')

class LettersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HebLetter
        fields = ('letter', )