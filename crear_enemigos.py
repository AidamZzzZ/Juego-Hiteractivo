class Enemigo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 8
        self.daño = 5
        self.armadura = 5
    
    
    def __str__(self):
        return self.nombre

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} a muerto.")
    
    def esta_vivo(self):
        return self.vida > 0 
    
    def golpe(self, enemigo):
        return self.daño - enemigo.armadura


class Duende(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre)

class Sapo(Enemigo):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.nombre = "Sapo"
        self.vida = 10
        self.daño = 8
        self.armadura = 9
    
class Ligre(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = "Ligre"
        self.vida = 15
        self.daño = 12
        self.armadura = 12

        
        
    
    
    