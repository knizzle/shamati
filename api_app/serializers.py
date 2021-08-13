from rest_framework import serializers
from django.contrib.auth import get_user_model

from dictionary.models import Phonemes, HebWord

class DictionarySerializer(serializers.ModelSerializer):
    model = Phonemes
    fields = (
        'hebWord',
        'xliteration',
        'root',
        'partOfSpeech',
        'definition',
    )