import json

from django.core.management.base import BaseCommand

from ...models import HebLetter, Phonemes, HebWord

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Phonemes, HebWords, and HebLetter
        Phonemes.objects.all().delete()
        HebLetter.objects.all().delete()
        HebWord.objects.all().delete()

        # Open phonemes JSON and load to list of dictionaries
        with open('phonemes.json', encoding='UTF-8') as p:
            hebletters = json.loads(p.read())
        
        # Loop through hebletters to add to DB
        for hebletter in hebletters:            

           # Add hebletters to DB
            hebletter_obj = HebLetter.objects.create(
                letter = hebletter
            )

            # Loop through hebletter list
            # For each letter, create letter if it doesn't exist yet, than add that letter to current Phoneme
            for phoneme in hebletters[hebletter]:
                phoneme_obj, created = Phonemes.objects.get_or_create(text=phoneme)
                phoneme_obj.hebletter.add(hebletter_obj)
