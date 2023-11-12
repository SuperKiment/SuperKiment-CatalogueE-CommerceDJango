from django.core.management.base import BaseCommand, CommandError
from produits.models import Produit, Categorie


class Command(BaseCommand):
    help = "Peuple la base de données avec des produits factices et des catégories factices"

    def handle(self, *args, **options):
        #Ajout des catégories (2 catégories en tout)
        categorie_nike = Categorie()
        categorie_nike.libelle = "Nike"
        categorie_nike.save()
        categorie_adidas = Categorie()
        categorie_adidas.libelle = "Adidas"
        categorie_adidas.save()
        #Ajout des produits (5 produits en tout)
        chaussure_nike_1 = Produit()
        chaussure_nike_1.libelle = "Baskets Nike Noir/Jaune"
        chaussure_nike_1.prix = 99.99
        chaussure_nike_1.reference = "N000001"
        chaussure_nike_1.pointure = 42
        chaussure_nike_1.categorie = categorie_nike
        chaussure_nike_1.photo = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F9%2F94%2FNike_Zoom_Air_Football_Boots.jpg&f=1&nofb=1&ipt=78e6424737b045ef1e129b89c41a0f9a9cf851a493c33563566019ba39c29fac&ipo=images"   
        chaussure_nike_1.save()
        
        chaussure_nike_2 = Produit()
        chaussure_nike_2.libelle = "Baskets Nike Grise"
        chaussure_nike_2.prix = 129.99
        chaussure_nike_2.reference = "N000002"
        chaussure_nike_2.pointure = 39
        chaussure_nike_2.categorie = categorie_nike
        chaussure_nike_2.photo = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fbleucameroun.fr%2Fcameroun%2Fnike%2Fbasket-nike-tn-pas-cher-homme-pirppvxc.jpg&f=1&nofb=1&ipt=9a001460891950ef8b226949f37dbc64149641aeff6730037c344720674752a0&ipo=images"   
        chaussure_nike_2.save()
        
        chaussure_nike_3 = Produit()
        chaussure_nike_3.libelle = "Baskets Nike Cyan"
        chaussure_nike_3.prix = 59.99
        chaussure_nike_3.reference = "N000003"
        chaussure_nike_3.pointure = 45
        chaussure_nike_3.categorie = categorie_nike
        chaussure_nike_3.photo = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffreepngimg.com%2Fthumb%2Frunning%2520shoes%2F29-nike-running-shoes-png-image.png&f=1&nofb=1&ipt=f60ab3113cf6b3fce85567c6d67089da2cc4b45a808813467919be6d0dadabd3&ipo=images"   
        chaussure_nike_3.save()

        chaussure_adidas_1 = Produit()
        chaussure_adidas_1.libelle = "Baskets Adidas Rouge"
        chaussure_adidas_1.prix = 89.99
        chaussure_adidas_1.reference = "A000001"
        chaussure_adidas_1.pointure = 45
        chaussure_adidas_1.categorie = categorie_adidas
        chaussure_adidas_1.photo = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Frunblogger.com%2Fimages%2F2012%2F08%2Fadidas-adipure-gazelle-review-very-impressive-natural-running-shoe.jpg&f=1&nofb=1&ipt=e1f8fa5b2fd6183024d2fab5e3601c90a5afe7730bdaf042d98a630b6992c43c&ipo=images"   
        chaussure_adidas_1.save()

        chaussure_adidas_2 = Produit()
        chaussure_adidas_2.libelle = "Baskets Adidas Gazelle (Femme)"
        chaussure_adidas_2.prix = 94.99
        chaussure_adidas_2.reference = "A000002"
        chaussure_adidas_2.pointure = 36
        chaussure_adidas_2.categorie = categorie_adidas
        chaussure_adidas_2.photo = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.bleucameroun.fr%2Fcameroun%2Fnike%2Fchaussure-adidas-gazelle-femme-pas-cher-jszui.jpg&f=1&nofb=1&ipt=e1cb71a2dd7e77c967acb629941f8e787f81badceb2da18af011eccb17a892c6&ipo=images"   
        chaussure_adidas_2.save()
        
        self.stdout.write(
            self.style.SUCCESS('Base de données remplie avec des produits et catégories factices')
        )