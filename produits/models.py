from django.db import models
from django.contrib.auth.models import User 

def get_user_name(self):
    if self.first_name or self.last_name:
        return self.first_name + " " + self.last_name
    return self.username

User.add_to_class("get_user_name",get_user_name)

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    reference = models.CharField(max_length=20)
    pointure = models.FloatField(default=0)
    photo = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.libelle}, {self.prix}, {self.reference}"