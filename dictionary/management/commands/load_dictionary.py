  
import json

from django.core.management.base import BaseCommand

from ...models import Phonemes, HebWord

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Phonemes and HebWords
        Phonemes.objects.all().delete()
        HebWord.objects.all().delete()

        # Open phonemes JSON and load to list of dictionaries
        with open('phonemes.json') as p:
            phonemes = json.loads(p.read())
        
        # Loop through Phonemes to add to DB
        for phoneme in phonemes:

#             # Convert units to m and kg
#             pokemon['height'] /= 10
#             pokemon['weight'] /= 10

#             # Add Phonemes to DB
#             poke_obj = Pokemon.objects.create(
#                 number=pokemon['number'],
#                 name=pokemon['name'],
#                 height=pokemon['height'],
#                 weight=pokemon['weight'],
#                 image_front=pokemon['image_front'],
#                 image_back=pokemon['image_back']
#             )

#             # Loop through HebWord list
#                 type_obj.pokemon.add(poke_obj)


# add data to your DB (you have dummy data, but you want all the sounds/phenomes data too)
# with above step: confirm your models look good -- modify any fields, re-makemigrations, migrate if needed
# once your DB looks good... work on api_app serializers.py and views.py...
# ... until the automatic REST /api/v1/ interface looks correct
# then get stuff displayed in Vue on front-end