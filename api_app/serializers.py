from rest_framework import serializers
from django.contrib.auth import get_user_model

from dictionary.models import LatinScript, HebWord

class DictionarySerializer(serializers.ModelSerializer):
    model = HebWord
    fields = (
        'hebWord',
        'xliteration',
        'root',
        'partOfSpeech',
        'definition',
    )