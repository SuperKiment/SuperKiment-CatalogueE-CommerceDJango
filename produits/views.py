
from django.http import HttpResponse
from django.shortcuts import render
from .models import Produit, Categorie
from django.contrib.auth.decorators import login_required

    
@login_required(login_url='/accounts/login/')
def index(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/index.html.twig', context)
    
@login_required(login_url='/accounts/login/')
def produit_individuel(request, id_produit):
    produit = Produit.objects.get(id=id_produit)
    context = {'produit': produit}
    return render(request, 'produits/produit_individuel.html.twig', context)

@login_required(login_url='/accounts/login/')
def panier(request, number):
    text = "lez goooo %d"%number
    return HttpResponse(text)

@login_required(login_url='/accounts/login/')
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