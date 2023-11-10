from django.db import models

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    reference = models.CharField(max_length=20)
    pointure = models.FloatField(default=0)
    photo = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.libelle}, {self.prix}, {self.reference}"