import random
aleatorio=random.randint(1,10)
num=int(input("Ingresa un numero: "))

def adivinar_numero(x,y):
    if x==y:
        return "El numero escogido es correcto"
    else:
        return "El numero escogido no es correcto"
    
a=adivinar_numero(aleatorio,num)
print(a)



