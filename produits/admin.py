from django.contrib import admin

from .models import Produit, Panier, Commande, Categorie
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(Commande)
admin.site.register(Categorie)
