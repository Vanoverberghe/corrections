#Ex 1

VOYELLES = "aeiouy"

def compter_voyelles(chaine):
    if chaine == "":
        return 0
    else:
        if chaine[0] in VOYELLES:
            return 1 + compter_voyelles(chaine[1:])
        else:
            return compter_voyelles(chaine[1:])
        
#Ex 2

def maximum(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        if liste[0] > maximum(liste[1:]):
            return liste[0]
        else:
            return maximum(liste[1:])
        
#Ex 3
    
def pair(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return pair(n-2)
    

#Ex 4
    
VALEURS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
    ]

def romain(n):
    if n == 0:
        return ""
    
    for valeur, symbole in VALEURS:
        if n>= valeur:
            return symbole + romain(n - valeur)