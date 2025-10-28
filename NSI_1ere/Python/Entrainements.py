# Exercice 1
#1
nom = "Mousseron"
age = 157
ville = "Denain"

#2
nombre1 = 6
nombre2 = 2
somme = nombre1 + nombre2

#3
a = 12
b = "Bonjour"
a,b = b,a

# Exercice 2

#1
demande = int(input("Quel age avez-vous?"))
if demande >=18:
    print("Majeur")
else:
    print("Mineur")
    
#2
nombre = int(input("Donnez un nombre"))
if nombre > 0:
    print("Positif")
elif nombre == 0 :
    print("Zero")
else:
    print("Negatif")
    
# Exercice 3

#1
for n in range(1,11):
    print(n)
    
#2
somme = 0
for n in range(101):
    somme+=n
    
#3
chaine = "Python"
for c in chaine:
    print(c)
    
# Exercice 4
#1
i = 1
while i <= 10:
    print(i)
    i += 1
    
#2
mdp = "Python123"
test = input("Entrer un mdp")
while test != mdp:
    test = input("Entrer un mdp")
    
#3
cpt = 100
while cpt>0:
    print(cpt)
    cpt-=1
    
# Exercice 5

#1
def bonjour():
    print("Bonjour !")

#2
def carre(x):
    return x**2

#3
def maximum(a, b):
    if a >b:
        return a
    else:
        return b

#4
def factorielle(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
