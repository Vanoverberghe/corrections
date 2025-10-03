class Cellule:
    
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
        
    def __repr__(self):
        return f"{self.valeur} -> {self.suivante}"
        
    


def longueur(liste_ch):
    if liste_ch is None:
        return 0
    else:
        return 1 + longueur(liste_ch.suivante)

## Exercice 2
def nieme_elt_ite(n, liste_ch):
    if liste_ch is None or n < 0:
        raise IndexError("indice invalide")
    cpt = n
    avance = liste_ch
    while cpt > 0:
        if not avance.suivante:
            raise IndexError("Indice trop grand")
        avance = avance.suivante
        cpt -= 1
    return avance.valeur

## Exercice 3

l_c1 = Cellule(9, Cellule(8, Cellule(7, None)))

l_c2 = Cellule(6, Cellule(5, Cellule(4, Cellule(3, None))))

l_c1.suivante.suivante.suivante = l_c2

print(nieme_elt_ite(3,l_c1))
print(nieme_elt_ite(6,l_c1))

l_c3 = Cellule(2, Cellule(1, None))

l_c2.suivante.suivante.suivante.suivante = l_c3

print(nieme_elt_ite(8,l_c1))

## Exercice 4

def affiche_liste(l_c):
    courant = l_c
    while courant.suivante:
        print(courant.valeur, end = " ")
        courant = courant.suivante
    print(courant.valeur)
    
def affiche_rec(l_c):
    if l_c is None:
        print()
    else:
        print(l_c.valeur, end = " ")
        affiche_rec(l_c.suivante)
        
## Exercice 5
        
def listeN(n):
    liste = None
    if n == 0:
        return liste
    else:
        for i in range(n, 0, -1):
            liste = Cellule(i, liste)
        return liste
    
## Exercice 6
    
def occurences_rec(x, l_c):
    if l_c is None:
        return 0
    else:
        if l_c.valeur == x:
            return 1 + occurences_rec(x, l_c.suivante)
        else:
            return occurences_rec(x, l_c.suivante)
        

            