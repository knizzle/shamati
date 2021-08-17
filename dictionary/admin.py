from django.contrib import admin
from .models import HebWord, Phonemes, HebLetter

admin.site.register(HebWord)
admin.site.register(Phonemes)
admin.site.register(HebLetter)