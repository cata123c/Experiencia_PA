import random
def cachipun():
    j=str(input("Elija piedra, papel o tijera"))
    lista=["tijera","piedra","papel"]
    r=random.randint(0,2)
    c=lista[r]
    print("La computadora elije:")
    print(c)
    if c==j:
        return "Empate"
    elif j=="piedra":
        if c=="tijera":
            return "Ganaste!"
        else: 
            return "Perdiste" 
    elif j=="tijera":
        if c=="papel":
            return "Ganaste!"
        else: 
            return "Perdiste"
    elif j=="papel":
        if c=="piedra":
            return "Ganaste!"
        else: 
            return "Perdiste"
    
n=cachipun()
print(n)
       
