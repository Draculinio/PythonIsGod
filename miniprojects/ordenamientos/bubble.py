import time
import random

def generar_lista(t):
    l = []
    for i in range(t):
        l.append(random.randint(1,100000000))
    return l

def burbuja(l):
    start = time.time()
    t = len(l)
    for i in range(t-1):
        for j in range(t-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    end = time.time()
    return (l,end-start)


print(burbuja(generar_lista(10000)))