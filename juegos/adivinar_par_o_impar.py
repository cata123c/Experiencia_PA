import random

def adivinar_par_o_impar():
    numero = random.randint (0,10000)
    elecc = str(input())
    se = True
    while se:
        if elecc == "par":
             se = False
        elif elecc == "impar":
             se = False
        else:
            print("Esa no es una elección")
            elecc = str(input())
    if elecc == "par":
        if numero%2 == 0:
            return str(numero)+ " si es par"
        else:
            return str(numero)+ " no es par"
    elif elecc == "impar":
        if numero%2 == 0:
               return str(numero)+ " no es impar"
        else:
              return str(numero)+ " si es impar"
        
n = adivinar_par_o_impar()
print(n)