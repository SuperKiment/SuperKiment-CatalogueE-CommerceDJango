
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Produit, Categorie, Panier

@login_required(login_url='/accounts/login/')
def index(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/index.html.twig', context)

@login_required(login_url='/accounts/login/')    
def produit_individuel(request, id_produit):
    produit = Produit.objects.get(id=id_produit)
    if request.method == "POST": # Si on a commandé le produit
        article_deja_dans_panier = Panier.objects.get(produit=produit)
        quantite_produit = request.POST.get('quantite')
        if article_deja_dans_panier:
            article_deja_dans_panier.nbr += int(quantite_produit)
            article_deja_dans_panier.save()
            return redirect(panier)
        nouvel_article = Panier()
        nouvel_article.nbr = quantite_produit
        nouvel_article.produit = produit
        nouvel_article.user = request.user
        nouvel_article.save()
        return redirect(panier)

    context = {'produit': produit}
    return render(request, 'produits/produit_individuel.html.twig', context)

@login_required(login_url='/accounts/login/')
def panier(request):
    panier_user = Panier.objects.filter(user=request.user)
    context = {'panier': panier_user}
    return render(request, 'produits/panier.html.twig', context)

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