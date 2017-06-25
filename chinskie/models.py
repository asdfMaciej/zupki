from django.db import models

class Zupka(models.model):
    nazwa = models.CharField(max_length=256)
    opis = models.CharField(max_length=4096)
    data_created = models.DateTimeField('date published')  # szukalem w docsach i nie wiem czy moge zmienic ten tekst