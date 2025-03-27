
import time
from Empieza_Aventura import Empieza_Aventura
from Combate import Combate

def main():
    print("Estás naciendo, por favor, no cierres la consola o puede que mueras en el parto")
    cadena = '-' * 50
    caracter = '#'
    b=0
    for i in range(100):
        if(i % 2 == 0):
            x=list(cadena)
            x[b]= caracter
            cadena="".join(x)
            b += 1

        print(f'[{cadena}]{i+1}%', end='\r')
        time.sleep(0.02)
    b=0
    cadena = '-' * 50
    caracter = '#'

    Empieza_Aventura()


    Combate()




if __name__ == "__main__":
        main()




  