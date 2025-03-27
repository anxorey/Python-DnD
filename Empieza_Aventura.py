def Empieza_Aventura():

    import numpy as np
    import random
    import time

    # Constants
    INTRO_TO_GO_NEXT = "(Intro para avanzar)"
    SHOW_BASE_STATS = "Tus estadísticas base son las siguientes:"

    print("Buenas aventurero. Veo que estás ansioso por entrar en la mazmorra pero, por qué no me dices tu nombre primero?")
    print("(Introduce tu nombre)")
    nombre= ""
    while nombre == "":
        nombre = input()
        if nombre == "":
            print("Sabes que soy el narrador de la historia y no puedes ocultarme nada, verdad? Venga, prueba otra vez, cuál es tu nombre?")


    print(f"Fantásitco {nombre}, encantado de conocerte. Para empezar tu aventura, debes elegir antes qué clase de personaje quieres ser")
    print(INTRO_TO_GO_NEXT); input()
    print("Elige sabiamente, cada tipo de personaje determina sus fortalezas y sus debilidades, no todos los personajes emplean las mismas estrategias")
    print(INTRO_TO_GO_NEXT); input()
    clases = ["Guerrero", "Asesino", "Mago", "Explorador", "Ladron"]

    clase = ""
    nombre_stats = ["Hp", "Fuerza", "Mp", "Inteligencia", "Velocidad"]
    stats = np.full(5,0)   
    habilidades = []       
    while clase not in clases:
        print(f"Puedes elegir entre: {clases}")
        clase = input()
        if clase == "Guerrero":
            print("Oh, la robusta clase de Guerrero. Me gusta, este tipo de personaje se caracteriza por su gran capacidad para recibir daño. Tus peleas serán largas, pero confio en que te las arreglarás en tu aventura")
            stats = [150, 30, 0, 10, 5]
            print(SHOW_BASE_STATS)
            for i in range(len(stats)):
                print(f"{nombre_stats[i]} = {stats[i]}")
            habilidades=["Escudo Divino","Armadura Celestial","Carga Hercúlea"]
            descripciones = ["", "", ""]
        elif clase == "Asesino":
            print("La despiadada clase de Asesino. Que los Dioses se apiaden de tus enemigos, con su formidable ataque los combates prometen ser cortos e intensos pero cuidado, es una clase frágil. Te deseo suerte en tu aventura, joven aventurero")
            stats = [50, 50, 5, 20, 15]
            print(SHOW_BASE_STATS)
            for i in range(len(stats)):
                print(f"{nombre_stats[i]} = {stats[i]}")
            habilidades=["Sorpresa", "Golpe Letal", "Muerte Instantánea"]
            descripciones = ["", "", ""]
        elif clase == "Mago":
            print("Asique un mago, eh. Suelen ser combatientes inteligentes y no se exponen al peligro. Con su gran capacidad mágica tienen grandes ataques a distancia. Que tu camino sea llevadero, joven")
            stats = [50, 5, 100, 30, 10]
            print(SHOW_BASE_STATS)
            for i in range(len(stats)):
                print(f"{nombre_stats[i]} = {stats[i]}")
            habilidades=["Aura Divina", "Multimagia", "MagiaElemental"]
            descripciones = ["", "", ""]
        elif clase == "Explorador":
            print("Conque un Explorador. Esta clase suele ser muy versátil y se ayuda mucho de su inteligencia para combatir y aprovechar sus ventajas y debilidades. Te deseo suerte en tu travesía, aunque no la necesitarás")
            stats = [75, 20, 40, 75, 20]
            print(SHOW_BASE_STATS)
            for i in range(len(stats)):
                print(f"{nombre_stats[i]} = {stats[i]}")
            habilidades=["Pies Ligeros", "Mapa Mundi", "Cautela Sigilosa"]
            descripciones = ["", "", ""]
        elif clase == "Ladron":
            print("Una clase perfecta para tí. El Ladrón se caracteriza por su gran velocidad y su capacidad de tomar prestadas cosas que no son suyas. Los Dioses no te miran con buenos ojos, pero confiemos en que estén de tu lado")
            stats = [60, 15, 20, 50, 50]
            print(SHOW_BASE_STATS)
            for i in range(len(stats)):
                print(f"{nombre_stats[i]} = {stats[i]}")
            habilidades=["Desarme", "Encontrador", "Manos Hábiles"]
            descripciones = ["", "", ""]
        else:
            print("Cómo dices? Creo que no te he escuchado bien. Por favor, repíteme tu clase.")
            clase=""

    print(INTRO_TO_GO_NEXT); input()
    print("Se me olvidaba, los dioses bendicen a sus hijos y les otorgan habilidades y un posible aumento de sus estadísticas")
    print(INTRO_TO_GO_NEXT); input()
    print("Veamos qué habilidad obtenemos")
    print(INTRO_TO_GO_NEXT); input()
    roll = random.randint(0,2); 
    habilidad = habilidades[roll] 
    descripcion = descripciones[roll]

    cadena = '-' * 50
    caracter = '#'
    b=0
    print("Los Dioses están tirando los dados para elegir tu habilidad sabiamente, un momento")
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
    print('\n')
    print(f"Los dioses te han dado la habilidad: {habilidad}" )
    print(INTRO_TO_GO_NEXT); input()
    print(f'Esta habilidad {descripcion} (descripción genérica de habilidad)')
    print(INTRO_TO_GO_NEXT); input()
    print("Los dioses quieren darte una pequeña bendición. Tirarán los dados para elegir aumentos en tus estadisticas")
    print("Cuando estés listo, presiona intro para comenzar tu ceremonia de bendición")
    print(INTRO_TO_GO_NEXT); input()
    print("Celebrando ceremonia de bendición, un segundo (están volviendo a tirar dados)")

    for i in range(100):
        if(i % 2 == 0):
            x=list(cadena)
            x[b]= caracter
            cadena="".join(x)
            b += 1

        print(f'[{cadena}]{i+1}%', end='\r')
        time.sleep(0.02)
    print('\n')
    print('\n')
    b=0
    cadena = '-' * 50
    caracter = '#'

    from random import randint
    dados=[randint(1,20) for _ in range(len(stats))] 
    for i in range(len(stats)):
        if dados[i] <= 5:
            print(f"Oh dichosa fortuna, que has decidido un +{dados[i]} en {nombre_stats[i]} para el joven {nombre}")
            stats[i] += dados[i]
            print(f"Ahora, {nombre_stats[i]} = {stats[i]}")
            print(INTRO_TO_GO_NEXT); input()
            print("\n")
        elif 5 < dados[i] <= 10:
            print(f"Bueno, tampoco está tan mal, has obtenido un +{dados[i]} en {nombre_stats[i]}")
            stats[i] += dados[i]
            print(f"Ahora, {nombre_stats[i]} = {stats[i]}")
            print(INTRO_TO_GO_NEXT); input()
            print("\n")
        elif 10 < dados[i] <= 15:
            print(f"Hei, que suerte, has obtenido un +{dados[i]} en {nombre_stats[i]}")
            stats[i] += dados[i]
            print(f"Ahora, {nombre_stats[i]} = {stats[i]}")
            print(INTRO_TO_GO_NEXT); input()
            print("\n")
        elif 15 < dados[i]< 20:
            print(f"No lo creen mis ojos, has obtenido un +{dados[i]} en {nombre_stats[i]}")
            stats[i] += dados[i]
            print(f"Ahora, {nombre_stats[i]} = {stats[i]}")
            print(INTRO_TO_GO_NEXT); input()
            print("\n")
        else:
            print(f"Tira la lotería en el casino de la ciudad, jove, has obtenido un +{dados[i]} en {nombre_stats[i]}")
            stats[i] += dados[i]
            print(f"Ahora, {nombre_stats[i]} = {stats[i]}")
            print(INTRO_TO_GO_NEXT); input()
            print("\n")

    print("Tras la ceremonia de bendición, estas son tus nuevas estadísticas:")
    for i in range(len(nombre_stats)):
        print(f'{nombre_stats[i]} = {stats[i]}')
    
    print(INTRO_TO_GO_NEXT); input()


    return nombre, nombre_stats, stats, habilidad
