class Arma:
    def __init__(self,tipo,daño,velocidad):
        self.tipo = tipo
        self.daño = daño
        self.velocidad = velocidad
        
    def ataque(self):
        ataque = self.daño + self.velocidad
        return ataque   

    def atributos_espada(self):
        print(f"""Las caracteristicas de la espada son:
              Tipo: {self.tipo}
              Daño: {self.daño}
              Velocidad: {self.velocidad}""")
    
    def __str__(self):
        return self.tipo,self.daño,self.velocidad
    
class Espada_madera(Arma):
    def __init__(self):
        self.tipo = "Espada de madera"
        self.daño = 15
        self.velocidad = 12
    
    def __str__(self):
        return (f"""Las caracteristica de la espada son:
              Tipo: {self.tipo}
              Daño: {self.daño}
              Velocidad: {self.velocidad}
              """)
    
class Espada_Piedra(Espada_madera):
    def __init__(self):
        super().__init__()
        self.__tipo = "Espada de piedra"
        self.__daño = 20
        self.__velocidad = 14.5
        self.critico = 5

espadita = Espada_madera()
espaditap = Espada_Piedra()
        