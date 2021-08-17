import json

from django.core.management.base import BaseCommand

from ...models import HebLetter, Phonemes, HebWord

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Phonemes and HebWords
        Phonemes.objects.all().delete()
        HebLetter.objects.all().delete()
        HebWord.objects.all().delete()

        # Open phonemes JSON and load to list of dictionaries
        with open('phonemes.json', encoding='UTF-8') as p:
            hebletters = json.loads(p.read())
        
        # Loop through Phonemes to add to DB
        for hebletter in hebletters:            

           # Add Phonemes to DB
            hebletter_obj = HebLetter.objects.create(
                letter = hebletter
            )

            # Loop through HebWord list
            for phoneme in hebletters[hebletter]:
                phoneme_obj, created = Phonemes.objects.get_or_create(text=phoneme)
                phoneme_obj.hebletter.add(hebletter_obj)
