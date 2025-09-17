from math import cos, acos

class Vecteur:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def set_composantes_xyz(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def set_composantes_AB(self, A, B):
        xA, yA, zA = A
        xB, yB, zB = B
        self.x = xB - xA
        self.y = yB - yA
        self.z = zB - zA
        
    def get_composantes(self):
        return self.x, self.y, self.z
    
    def addition(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
        
    def soustraction(self, v):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        
    def norme(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def angle(self, v):
        return acos((self.x*v.x+self.y*v.y+self.z*v.z)/(self.norme() * v.norme()))
    
    def scalaire(self, v):
        return self.norme() * v.norme() * cos(self.angle(v))
    
v1 = Vecteur(2,2,2)
v2 = Vecteur(2,4,6)