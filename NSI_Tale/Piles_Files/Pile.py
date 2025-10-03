class Pile:
    
    def __init__(self):
        self.elems = []
        
    def est_vide(self):
        return self.elems == []
    
    def empiler(self, x):
        self.elems.append(x)
        
    def depiler(self):
        if self.est_vide():
            raise ValueError("la pile est deja vide")
        return self.elems.pop()
        
    def sommet(self):
        return self.elems[-1]
    
    def affiche_pile(self):
        for i in range(len(self.elems)-1, -1, -1):
            print("--------")
            print("|      |")
            print(f"|   {self.elems[i]}   |")
            print("|      |")
        print("--------")