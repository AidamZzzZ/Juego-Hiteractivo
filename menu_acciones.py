from crear_personaje import Personaje,crear_nombre
from crear_enemigos import Duende,Sapo,Ligre
from crear_espadas import Espada_madera,espadita,espaditap

class Inicio(Personaje):
    def Bienvenida(self):
        print("--------------------------------------------------------------------------------------------------")
        print("¡¡Bienvenido al juego!!,Espero te guste y que disfrutes este proyecto hecho por: Adrian Gomez ")
        print("el 27 de noviembre de 2023...Diviertete ¡Saludos!")
        print("--------------------------------------------------------------------------------------------------")
    
    def principio(self):
        print("Estas en un lugar lleno de armoles....")
    
    def menu(self):
        while True:
            opcion = int(input("presiona 1 para caminar:"))
            if opcion == 1:
                print("caminando....")
                print("------------------------------------------")
                print("Te encuentras un duente...")
                opcion2 = "s"
                while True:
                    opcion2 = input("Presione 'si' para golear al duende: ").lower()
                    if opcion2 == "si":
                        print("------------------------------------------")
                        personaje.atacar(duende)
                        print("------------------------------------------")
                        opcion3 = "0"
                        print(f"Haz desbloqueado una espada de Madera!")
                        opcion3 = int(input("Ingrese 1 para ver los atributos de la espada: "))
                        if opcion3 == 1:
                            print("------------------------------------------")
                            espadita.atributos_espada()
                            print("------------------------------------------")
                            print("¡Preparate para esta pequeña pero gran aventura!")

                        else:
                            print("¡Preparate para esta pequeña pero gran aventura!")
                        break
                    else:
                        print("Vamos,mata al maldito duende")
                print("------------------------------------------")
                if not duende.esta_vivo():
                    break
            else:
                print("ingrese 1.....")
    
    def caracteristicas_personaje(self):
        while True:
            print("------------------------------------------")
            print(f"""Opciones: 
                1- Ver caracteristicas del personaje
                2.- Pelear contra Mounstros
                3- Salir""")
            print("------------------------------------------")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                personaje.caracteristicas()
            elif opcion == 2:
                print("------------------------------------------")
                seleccion = int(input("""Seleciona contra quien queires pelear:
                                1- Duende
                                2- Sapo
                                3- Ligre
                                    """))
                print("------------------------------------------")
                if seleccion == 1:
                    personaje.atacar(duende)
                    print("------------------------------------------")
                elif seleccion == 2:
                    personaje.atacar(sapo)
                    print("------------------------------------------")
                elif seleccion == 3:
                    personaje.atacar(ligre)
                    print("------------------------------------------")
            if self.nivel == 5:
                    print(f"""Felicidades te haz ganado una Espada de piedra!
                          {espaditap.atributos_espada()}""""")
            elif opcion == 3:
                print("Espero hayas disfrutado este pequeño juego interactivo,¡Hasta Luego!")
                break


personaje = Personaje(crear_nombre())            
ligre = Ligre("Ligre maton") 
sapo = Sapo("Grompo")            
duende = Duende("duende") 
inicio = Inicio(personaje)
inicio.Bienvenida()
inicio.principio()
inicio.menu()
inicio.caracteristicas_personaje()

