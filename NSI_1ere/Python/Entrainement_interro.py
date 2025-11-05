# Ex 3
mot = "Programmation"
#parcours par éléments
for c in mot:
    print(c)
  
#parcours par indices
for i in range(len(mot)):
    print(mot[i])

i = 0
while i < len(mot):
    print(mot[i])
    i = i + 1
    
#Exercice 4
    
def inverse(chaine):
    res = ""
    for i in range(len(chaine)):
        res += chaine[-i-1]
    return res
        
def inverse2(chaine):
    res = ""
    for i in range(len(chaine)):
        res = chaine[i] + res
    return res

#Exercice 5

def positions_lettre(chaine, lettre):
    res = []
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            res.append(i)
    return res