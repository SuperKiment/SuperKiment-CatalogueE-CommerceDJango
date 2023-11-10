
from django.http import HttpResponse
from django.shortcuts import render
from .models import Produit


def index(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/index.html.twig', context)
    
def produit_individuel(request):
    text = "<h1>Hello world</h1><p>Benjoueuuuuur</p>"
    return HttpResponse(text)

def panier(request, number):
    text = "lez goooo %d"%number
    return HttpResponse(text)

