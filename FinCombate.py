#def FinCombate():

def RecibeExp(self, NombreM, expM):
        print(f"El monstruo {NombreM} ha sido derrotado. {self.NombreP} ha recibido {expM}")
        self.exp += expM
        if self.exp == self.exp_lvl_up:
            self.lvl += 1
            self.exp = 0
            self.exp_lvl_up += 1000+self.lvl*10000
            print(f"{self.NombreP} ha subido al nivel {self.lvl}")
        elif self.exp > self.exp_lvl_up:
            self.exp =self.exp_lvl_up-self.exp
            self.lvl += 1
            self.exp_lvl_up += 1000+self.lvl*10000
            print(f"{self.NombreP} ha subido al nivel {self.lvl}")
        else:
            self.exp += expM

        print(f"{self.NombreP} tiene {self.exp} de {self.exp_lvl_up} necesarios para subir de nivel")
    

Anxo = Personaje("Anxo", "Guerrero", 1); NombreP="Anxo"



    #return