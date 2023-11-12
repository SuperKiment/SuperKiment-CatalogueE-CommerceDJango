from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Produit, Categorie, Panier, Commande

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request):
    produits = Produit.objects.all()
    context = {
        'produits': produits,
        'badgepanier' : getNombrePanier()
    }
    return render(request, 'produits/index.html.twig', context)

@login_required(login_url='/accounts/login/')    
def produit_individuel(request, id_produit):
    produit = Produit.objects.get(id=id_produit)
    if request.method == "POST": # Si on a commandé le produit
        try : # On vérifie si le produit est déjà dans le panier
            article_deja_dans_panier = Panier.objects.get(produit=produit)
        except Panier.DoesNotExist: 
            article_deja_dans_panier = None
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

    context = {'produit': produit, 'badgepanier' : getNombrePanier()}
    return render(request, 'produits/produit_individuel.html.twig', context)

@login_required(login_url='/accounts/login/')
def panier(request):
    if request.method == "POST": # Si on a envoyé un formulaire
        action = request.POST.get('action')
        match(action) :
            case 'supprimer':
                entree_panier_id = request.POST.get('entree_panier_supprimer')
                entree_panier = Panier.objects.get(id=entree_panier_id)
                entree_panier.delete()
            case 'editer':
                entree_panier_id = request.POST.get('entree_panier_editer')
                entree_panier_nv_quantite = request.POST.get('quantite')
                entree_panier = Panier.objects.get(id=entree_panier_id)
                entree_panier.nbr = entree_panier_nv_quantite
                entree_panier.save()
            case 'commander':
                panier_user = Panier.objects.filter(user=request.user)
                for panier in panier_user:
                    nouvelle_commande = Commande()
                    nouvelle_commande.nbr = panier.nbr
                    nouvelle_commande.produit = panier.produit
                    nouvelle_commande.user = panier.user
                    nouvelle_commande.prixTotal = panier.produit.prix * panier.nbr
                    nouvelle_commande.save()
                    print(panier)
                    panier.delete()
                message = "Votre commande a bien été prise en compte !"
                context = {'message': message,'badgepanier' : getNombrePanier()}
                return render(request, 'produits/panier.html.twig', context)
                
    try :
        panier_user = Panier.objects.filter(user=request.user)
        context = {'panier': panier_user,'badgepanier' : getNombrePanier()}
    except Panier.DoesNotExist:
        panier_user = None
        context = {'badgepanier' : getNombrePanier()}

    return render(request, 'produits/panier.html.twig', context)
    
@login_required(login_url='/accounts/login/')
def categories(request, libelle = None):
    if (libelle == None):
        return render(request, 'produits/categories.html.twig', {
            'categories': Categorie.objects.all(),
            'badgepanier' : getNombrePanier()
        })
    else :
        categorie = Categorie.objects.get(libelle=libelle)
        produits = Produit.objects.filter(categorie=categorie)
        print(produits)
        return render(request, 'produits/categorie.html.twig', {
            'categorie': categorie,
            'produits' : produits,
            'badgepanier' : getNombrePanier()
        })
    

def getNombrePanier():
    return len(Panier.objects.all())


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="produits/register.html.twig", context={"register_form":form})