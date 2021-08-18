from django.db import models

class HebWord(models.Model):
    word = models.CharField(max_length=20, blank=True, null=True)
    transliteration = models.CharField(max_length=20, blank=True, null=True)
    root = models.CharField(max_length=20, blank=True, null=True)
    partOfSpeech = models.CharField(max_length=50, blank=True, null=True)
    definition = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.word

class HebLetter(models.Model):
    letter = models.CharField(max_length=5)
    # five final letters different from original form (ם‎, ן‎, ץ‎, ף‎, ך), not in JSON
    # hebfinal = models.ForeignKey( ,  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.letter

class Phonemes(models.Model):
    text = models.CharField(max_length=3, )
    hebletter = models.ManyToManyField(HebLetter, blank=True, null=True)
    
    def __str__(self):
        return self.text



# class LatinScript(models.Model):
#     text = models.CharField(max_length=20)
#     hebWord = models.ForeignKey(HebWord, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text
