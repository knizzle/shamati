from rest_framework import serializers
from django.contrib.auth import get_user_model

from dictionary.models import Dictionary

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ()