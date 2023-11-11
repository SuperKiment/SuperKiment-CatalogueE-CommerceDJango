print("lez go ?")
from produits.models import Produit, Categorie
print("lez go !")
valeurs = {
    "Categorie": [
        ["Chaussures de sport"],
        ["Chaussures décontractées"],
        ["Chaussures élégantes"],
    ],
    "Produit": [
        ["Air Max", 120, "AM001", 42, "Chaussures de sport"],
        ["Classic Sneaker", 80, "CS002", 38, "Chaussures décontractées"],
        ["Formal Oxford", 150, "FO003", 44, "Chaussures élégantes"],
        ["Running Pro", 90, "RP004", 39, "Chaussures de sport"],
        ["Casual Slip-On", 60, "CSO005", 37, "Chaussures décontractées"],
    ],
    "Utilisateur": [
        ["user123"],
        ["shoeLover87"],
    ],
}

for categorie in valeurs["Categorie"]:
    cat = Categorie(libelle=categorie[0])
    cat.save()
    print("ajout : "+cat)

for produit in valeurs["Produit"]:
    prod = Produit(
        libelle=produit[0],
        prix=produit[1], 
        reference=produit[2], 
        pointure=produit[3],
        categorie=Categorie.objects.get(libelle=produit[4]),
        photo="https://girotti.fr/media/catalog/product/cache/2/image/833x/9df78eab33525d08d6e5fb8d27136e95/5/6/5657-6-0_1_1.jpg"
    )
    prod.save()
    print("ajout : "+prod)