#Q1

class Voiture:
    
    def __init__(self, param_moteur, param_couleur, param_puissance, param_portes, param_masse, param_boite, param_vide, param_ptac):
        self.moteur = param_moteur
        self.couleur = param_couleur
        self.puissance = param_puissance
        #Q8
        self.portes = param_portes
        self.masse = param_masse
        self.boite = param_boite
        self.vide = param_vide
        self.ptac = param_ptac
        
    def caracteristiques(self):
        return {"moteur": self.moteur, "couleur": self.couleur, "puissance": self.puissance, "Nombre de portes": self.portes, "masse" : self.masse, "Nombre de vitesses": self.boite, "Masse a vide": self.vide, "Masse maximale autorisée": self.ptac}
    
    def modifie_couleur(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
        
    #Q7
        
    def modifie_moteur(self, nouveau_moteur):
        self.moteur = nouveau_moteur
        
    def modifie_puissance(self, nouvelle_puissance):
        self.puissance = nouvelle_puissance
        

    #Q13
    def affiche(self):
        print("Les caractéristiques du véhicule sont :")
        for k,v in self.caracteristiques():
            print(k, ":", v)
            
    #Q14
    def charge(self, ajout):
        if ajout + self.masse < self.ptac:
            self.masse += ajout
            return True
        return False
    
    #Q15
    def decharge(self, retrait):
        if self.masse - retrait > self.vide:
            self.masse -= ajout
            return True
        return False
        
    
    def __del__(self):
        print("un dernier calcul avant de mourir :", 2+2)
        print("je meurs ......")
    

#Q2
        
voiture_1 = Voiture("diesel", "rouge", 90, 3, 750, 5, 600, 1000)
voiture_2 = Voiture("essence", "bleu", 140, 5, 900, 6, 750, 1300)

#print affiche  <__main__.Voiture object at 0x.....>

#Q3
# acces a l'attribut moteur de voiture_1:
# print(voiture_1.moteur)
# acces a l'attribut couleur de voiture_2:
# print(voiture_2.couleur)

#Q4

voiture_2.couleur = "gris"

# la couleur de voiture_2 est maintenant gris

voiture_1.moteur = "Hybride"

# le moteur de voiture_1 est maintenant Hybride

#Q5

print(voiture_1.caracteristiques())
# J'appelle ma méthode pour avoir son résultat. pas oublier les parenthèses !!!
# Ce type de méthode est un accesseur ( getter )

#Q6

voiture_2.modifie_couleur("bleu")
# La couleur de voiture_2 est modifiée est redevient bleu
# Ce type de méthode est un modificateur ( setter )

#Q10
# Un dictionnaire est une structure de données qui à un ensemble de clés, associe un ensemble de valeurs
# Les clés sont uniques mais plusieurs clés peuvent avoir la meme valeur

#Q11

# d.keys() renvoie l'ensemble des clés du dictionnaire d
# d.values() renvoie l'ensemble des clés du dictionnaire d
# d.items() renvoie l'ensemble des couples (clés, valeurs) du dictionnaire d

#Q12

mon_dict = voiture_2.caracteristiques()
# affiche toutes les clés 
for k in mon_dict.keys():
    print(k)
    
# affiche toutes les valeurs
for v in mon_dict.values():
    print(v)
    
# affiche les couples clés,valeurs
for k,v in mon_dict.items():
    print(k, v)