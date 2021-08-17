import json

from django.core.management.base import BaseCommand

from ...models import HebLetter, Phonemes, HebWord

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Phonemes and HebWords
        Phonemes.objects.all().delete()
        HebWord.objects.all().delete()

        # Open phonemes JSON and load to list of dictionaries
        with open('phonemes.json', encoding='UTF-8') as p:
            phonemes = json.loads(p.read())
        
        # Loop through Phonemes to add to DB
        for phoneme in phonemes:

            # Convert phonemes to Heb letter
            print(phoneme)

           # Add Phonemes to DB
            phoneme_obj = Phonemes.objects.create(
                text = phoneme
                hebletter = 
            )

            # Loop through HebWord list
            # for phoneme in hebletter['phonemes']:
            #     hebword_obj, created = HebWord.objects.get_or_create(hebletter=hebletter)
            #     hebword_obj.phoneme.add(phoneme_obj)
