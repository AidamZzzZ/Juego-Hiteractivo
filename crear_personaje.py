class Personaje:
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 1
        self.vida = 10
        self.daño = 8
        self.armadura = 5
    
    def __repr__(self):
        print(f"""Su personaje se llama: {self.nombre}
              vida: {self.vida}
              daño: {self.daño}
              armadura: {self.armadura}""")
    
    def __str__(self):
        return self.nombre

    def morir(self,enemigo):
        enemigo.vida = 0
        print(f"{enemigo.nombre} a muerto.")
    
    def esta_vivo(self):
        return self.vida >= 0 
    
    def golpe(self, enemigo):
        self.daño - enemigo.vida
        return enemigo.vida
    
    def atacar(self, enemigo):
        sangrado = self.golpe(enemigo)
        enemigo.vida = enemigo.vida - sangrado
        print(f"Haz hecho: {self.daño} de daño al {enemigo.nombre}")
        if enemigo.vida > 0:
            print("El enemigo sigue vivo.")
        else:
            enemigo.morir()
            self.subir_nivel()
        return self.nivel + 1
        print("------------------------------------------")
        
    def subir_nivel(self):
        nivel_maximo = 10
        if self.nivel < nivel_maximo:
            self.nivel = self.nivel + 1
            self.vida = self.vida + 15
            self.daño = self.daño + 6
            self.armadura = self.armadura + 5
        return print(f"""
            ¡Subes de nivel! las habilidades aumentadas son: 
             Nivel: {self.nivel}
             vida: {self.vida}
             daño: {self.daño}
             armadura: {self.armadura}""")
    
    def caracteristicas(self):
        print(f"""
              Nivel: {self.nivel}
              Vida: {self.vida}
              daño: {self.daño}
              Armadura: {self.armadura}""")

def crear_nombre():        
    while True:
        nombre = input("Ingrese un nombre: ")
        if len(nombre) > 6:
            print("Su nombre tiene que contener entre 6 caracteres")
        else:
            print(f"El nombre de su personaje es: {nombre} ")
            break
    return Personaje(nombre)
