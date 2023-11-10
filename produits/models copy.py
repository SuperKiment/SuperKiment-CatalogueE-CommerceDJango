from django.db import models
from django.contrib.auth.models import User 

def get_user_name(self):
    if self.first_name or self.last_name:
        return self.first_name + " " + self.last_name
    return self.username

User.add_to_class("get_user_name",get_user_name)

class Categorie(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.libelle

class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    reference = models.CharField(max_length=20)
    pointure = models.FloatField(default=0)
    photo = models.CharField(max_length=500)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.libelle}, {self.prix}, {self.reference}"

class Panier(models.Model):
    nbr = models.IntegerField(default=1)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.produit}, {self.user}, {self.nbr}"

class Commande(models.Model):
    nbr = models.IntegerField(default=1)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prixTotal = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.produit}, {self.user}, {self.nbr}, {self.prixTotal}"