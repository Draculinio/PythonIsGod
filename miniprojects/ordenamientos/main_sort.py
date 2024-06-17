import time
import random

def generar_lista(t):
    l = []
    for i in range(t):
        l.append(random.randint(1,100000000))
    return l


l = generar_lista(5000000)

start = time.time()
l.sort()
end = time.time()

#print(l)
print (end-start)