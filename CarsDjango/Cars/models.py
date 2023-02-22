from django.db import models


# Create your models here.
class Car(models.Model):
    modele = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    creation = models.DateField('date creation')
    cylindre = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def __str__(self):
        return self.modele
