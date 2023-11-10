from django.urls import path
from django.urls import include
from produits import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('produit_individuel/<int:id_produit>', views.produit_individuel, name='produit_individuel'),
    path('panier', views.panier, name='panier'),
]