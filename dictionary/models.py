from django.db import models

class HebWord(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

class LatinScript(models.Model):
    text = models.CharField(max_length=20)
    hebWord = models.ForeignKey(HebWord, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



