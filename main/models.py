from django.db import models

# Create your models here.

class Preference(models.Model):
    nazwa = models.CharField(max_length=200,null=True)
    czas_pracy = models.FloatField()
    woda = models.FloatField()
    posilki = models.IntegerField()
    cwiczenia = models.BooleanField()
    przerwy_ilosc = models.IntegerField()
    przerwy_czas = models.IntegerField()