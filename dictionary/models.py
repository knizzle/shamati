from django.db import models

class HebWord(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

class HebLetter(models.Model):
    letter = models.CharField(max_length=5)

    def __str__(self):
        return self.letter

class Phonemes(models.Model):
    text = models.CharField(max_length=3)
    HebLetter = models.ForeignKey(HebLetter, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text



# class LatinScript(models.Model):
#     text = models.CharField(max_length=20)
#     hebWord = models.ForeignKey(HebWord, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text
