import random

def Combate():

    class Entidad:
        def __init__(self, Nombre, Clase, lvl, Fuerza, Vida, Mana, NombreM, lvlM, ClaseM, FuerzaM, VidaM, ManaM):
            self.Nombre = Nombre
            self.Clase = Clase
            self.lvl = lvl
            self.Fuerza = Fuerza
            self.Vida = Vida
            self.Mana = Mana
            self.Stats = [self.lvl, self.Fuerza, self.Vida, self.Mana]  
            self.NombreM = NombreM
            self.ClaseM = ClaseM
            self.lvlM = lvlM
            self.FuerzaM = FuerzaM
            self.VidaM = VidaM
            self.ManaM = ManaM
            self.StatsM = [self.lvl, self.FuerzaM, self.VidaM, self.ManaM]

        
        
            

    class Mob(Entidad):
        def __init__(self, NombreM, lvlM, ClaseM, FuerzaM, VidaM, ManaM, ConcentracionM):
            self.NombreM = NombreM
            self.ClaseM = ClaseM
            self.lvlM = lvlM
            self.FuerzaM = FuerzaM
            self.VidaM = VidaM
            self.ManaM = ManaM
            self.ConcentracionM = ConcentracionM
            self.StatsM = [self.lvlM, self.FuerzaM, self.VidaM, self.ManaM]

        def Aparece(self):
            print(f"Oh, no. Un {self.NombreM} salvaje apareción")
        
        def ActStatsM(self):
            print(f"Las estadísticas del {self.NombreM} enemigo son {self.StatsM}")

        def CurarseM(self):
            print(f"El {self.NombreM} enemigo ha usado un hechizo curativo, se ha curado 20Hp a cambio de perder 10 Mp")
            self.VidaM += 20
            self.ManaM -= 10            
            self.StatsM = [self.FuerzaM, self.VidaM, self.ManaM]
            print(f"Las estadísticas ahora son {self.StatsM}")
        
        def HuirM(self):
            print(f"{self.NombreM} escapó")
        
        def AtacarM(self):
            self.Vida -= self.FuerzaM; print(f"{self.Nombre} tiene ahora {self.Vida}hp")



    duende = Mob("Duende", "Humanoide", 1, 10, 50, 10, 1)
    #-------------------------------------------------------------#
    #-------------------------Héroes aquí-------------------------#
    #-------------------------------------------------------------#


    class Heroe(Entidad):
        def __init__(self, Nombre, Clase, lvl, Fuerza, Vida, Mana, Concentracion):
            self.Nombre = Nombre
            self.Clase = Clase
            self.lvl = lvl
            self.Fuerza = Fuerza
            self.Vida = Vida+lvl*5
            self.VidaIni=Vida+lvl*5
            self.Mana = Mana
            self.Concentracion = Concentracion
            self.Stats = [self.lvl, self.Fuerza, self.Vida, self.Mana, self.Concentracion, self.VidaIni]
            self.nombre_stats = ["Nivel:", "Fuerza:", "Vida:", "Maná:", "Concentración:"]
            self.accion = "Atacar"
            self.posibles = ["ActStats", "Mentalizarse", "Atacar", "Curarse", "Escapar"]

        def EntrarCombate(self, NombreM):
            print(f"{self.Nombre} ha atacado preventivamente a {NombreM} y le ha quitado {self.Fuerza}hp") 
            VidaM -= self.Fuerza; print(f"La vida de {NombreM} es {VidaM}hp") 


        def ActStats(self):
            print(f"Las estadísticas de {self.Nombre} son:")
            for _ in range(len(self.nombre_stats)):
                print(f"{self.nombre_stats[_]} = {self.Stats[_]}")

        
        def Mentalizarse(self):
            print(f"{self.Nombre} se concentra en su objetivo")            
            if self.Concentracion == 1:
                self.Concentracion += 1
                print(f"Ahora {self.Nombre} ha visto donde atacar y el golpe dolerá el doble")
            elif self.Concentracion == 2:
                self.Concentracion += 3
                print(f"Ahora {self.Nombre} está súper concentrado y asestará un golpe crítico")
            elif self.Concentracion == 5:
                self.Concentracion *= 10 
                print(f"Ahora {self.Nombre} ha descubierto como matar al rival. El siguiente golpe será extremadamente poderoso")
            elif self.Concentracion == 50:
                self.Concentracion *= 100 
                print(f"Ahora {self.Nombre} ha entrado en estado de gracia y pega 100 veces más fuerte")
            else:
                print(f"{self.Nombre} ya está mentalizado al máximo y no puede aumentar su concentración")


        def Atacar(self, Mob):                                               
            print(f"{self.Nombre} ataca a {self.NombreM}" )                               
            dam = random.uniform(0.75,1.25)*self.Fuerza*self.Concentracion; print(f"{dam}")             
            VidaM -= dam
            print(f"{self.Nombre} le ha quitado {dam}hp a {self.NombreM}")


        def Curarse(self):  
            print(f"{self.Nombre} bebe una poti")
            print(f"{self.Nombre} ha recibido 20Hp")
            if self.Vida == self.VidaIni:
                print(f"La vida ya estaba al máximo")
            elif self.Vida == 0:
                print(f"El personaje está muerto, como se va a curar")
            else:
                self.Vida += 20
                print(f"{self.Nombre} tiene {self.Vida}hp")

        def Escapar(self):
            print(f"{self.Nombre} escapa y ya no puede participar en el combate")

        def Accion(self):
            print(f"Cuál va a ser tu primera acción? {self.posibles}")  
            while self.accion in self.posibles:            
                self.accion = input()                       
                if self.accion == "ActStats":
                    Anxo.ActStats()
                    print(f"Qué hacer ahora? {self.posibles}")
                elif self.accion == "Mentalizarse":
                    Anxo.Mentalizarse()
                    print(f"Qué hacer ahora? {self.posibles}")  
                elif self.accion == "Atacar":
                    Anxo.Atacar("Duende")
                    print(f"Qué hacer ahora? {self.posibles}")  
                elif self.accion == "Curarse":
                    Anxo.Curarse()
                    print(f"Qué hacer ahora? {self.posibles}")  
                elif self.accion == "Escapar":
                    Anxo.Escapar()  
                    self.accion = ""
                else:
                    print(f"Esta acción no está en tus posibilidades, por favor decide cuál de las siguientes opciones hará {self.Nombre} a continuación:" )
                    print(f"{self.posibles}")
                    self.accion = "Atacar"



    Anxo = Heroe("Anxo", "Guerrero", 1, 50, 95, 50,1); 

    duende.Aparece()
    Anxo.Accion()





    if __name__ == "__Combate__":
            Combate()

    return  Nombre, Clase, lvl, Fuerza, Vida, Mana, Concentracion


   