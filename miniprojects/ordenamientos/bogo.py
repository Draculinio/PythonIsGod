import time
import random

def generar_lista(t):
    l = []
    for i in range(t):
        l.append(random.randint(1,10000))
    return l

def verficar_orden(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True

def bogo(l):
    print(l)
    start = time.time()
    ordenado = False
    while not ordenado:
        random.shuffle(l)
        #print(l)
        ordenado = verficar_orden(l)
    end = time.time()
    return (l,end-start)


print(bogo(generar_lista(12)))