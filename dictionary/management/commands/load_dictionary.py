  
# import json

# from django.core.management.base import BaseCommand

# from ...models import Phonemes, HebWord

# class Command(BaseCommand):

#     def handle(self, *args, **options):
        
#         # Clear existing Pokemon and Types
#         Phonemes.objects.all().delete()
#         HebWord.objects.all().delete()

#         # Open Pokemon JSON and load to list of dictionaries
#         with open('phonemes.json') as p:
#             phonemes = json.loads(p.read())
        
#         # Loop through Pokemon to add to DB
#         for phoneme in phonemes:

#             # Convert units to m and kg
#             pokemon['height'] /= 10
#             pokemon['weight'] /= 10

#             # Add Pokemon to DB
#             poke_obj = Pokemon.objects.create(
#                 number=pokemon['number'],
#                 name=pokemon['name'],
#                 height=pokemon['height'],
#                 weight=pokemon['weight'],
#                 image_front=pokemon['image_front'],
#                 image_back=pokemon['image_back']
#             )

#             # Loop through types list
#             # For each type, create type if it doesn't exist yet, than add that type to current Pokemon
#             for type in pokemon['types']:
#                 type_obj, created = Type.objects.get_or_create(type=type)
#                 type_obj.pokemon.add(poke_obj)


# add data to your DB (you have dummy data, but you want all the sounds/phenomes data too)
# with above step: confirm your models look good -- modify any fields, re-makemigrations, migrate if needed
# once your DB looks good... work on api_app serializers.py and views.py...
# ... until the automatic REST /api/v1/ interface looks correct
# then get stuff displayed in Vue on front end