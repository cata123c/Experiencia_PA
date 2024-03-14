import random
import time
import os

lista_num=[]
a=0
def memoria():
    for i in range(4):
        lista_num.append(random.randint(1,9))
    print("Recuerda la siguiente sequencia de numeros:")
    print(lista_num)
    time.sleep(6)
    os.system("clear")
    print("Inserta los numeros de esta manera [1, 2, 3, 4, 5, 6, 7, 8]")
    a=input("¿Cual era la secuencia de numeros?: ")
    if a==str(lista_num):
        print("Correcto, tienes buena memoria")
    if not a==str(lista_num):
        print("Incorrecto, vuelve a intentarlo")

memoria()
