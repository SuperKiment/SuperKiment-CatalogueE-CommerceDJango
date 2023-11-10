
from django.http import HttpResponse
from django.shortcuts import render
from .models import Produit, Categorie


def index(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/index.html.twig', context)
    
def produit_individuel(request, id_produit):
    text = "<h1>Hello world</h1><p>Benjoueuuuuur</p>"
    return HttpResponse(text)

def panier(request, number):
    text = "lez goooo %d"%number
    return HttpResponse(text)

def categories(request, libelle = None):
    if (libelle == None):
        return render(request, 'produits/categories.html.twig', {
            'categories': Categorie.objects.all()
        })
    else :
        categorie = Categorie.objects.get(libelle=libelle)
        produits = Produit.objects.filter(categorie=categorie)
        print(produits)
        return render(request, 'produits/categorie.html.twig', {
            'categorie': categorie,
            'produits' : produits
        })