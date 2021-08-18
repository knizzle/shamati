from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from dictionary.models import Phonemes, HebWord, HebLetter

class NestedLettersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HebLetter
        fields = ('letter', )

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
    hebletter_detail = NestedLettersSerializer(source='hebletter', many=True)
    class Meta: 
        model = Phonemes
        fields = ('text', 'hebletter', 'hebletter_detail')

class LettersSerializer(serializers.ModelSerializer):
    phoneme_detail = NestedLettersSerializer
    class Meta: 
        model = HebLetter
        fields = ('letter', )