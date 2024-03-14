import random

def juego_del_dado():
    jug1 = 0
    jug2 = 0
    sepuede = True
    while sepuede:
        print("Apreta Enter para lanzar el dado")
        input()
        lanzamiento = random.randint(1,6)
        print("El número obtenido fue "+str(lanzamiento))
        jug1 += lanzamiento
        if jug1 >= 30:
            ganador = 1
            sepuede = False
        elif jug1 < 30:
            print("Llevas "+str(jug1)+" puntos")
            lanzamiento2 = random.randint(1,6)
            print("Tu adversario saco "+str(lanzamiento2))
            jug2 += lanzamiento2
            if jug2 >= 30:
                ganador = 2
                sepuede = False
            elif jug2 < 30:
                print("Tu adversario lleva "+str(jug2)+" puntos")
    if ganador == 1:
        return "Has llegado primero a 30 puntos!!"
    elif ganador == 2:
        return "Tu adversario llego primero a 30 puntos"

         




n = juego_del_dado()
print(n)