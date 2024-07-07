#[20, 10, 15, 7, 8] [10, 20, 15, 7, 8] [10, 15, 20, 7, 8] [7, 10, 15, 20, 8] [7, 8, 10, 15, 20]
import random
import time

def generar_lista(t):
    return [random.randint(1, 100000000) for _ in range(t)]

def insertion(l):
    print(l)
    start = time.time()
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while key < l[j] and j>=0:
            l[j+1] = l[j]
            j -=1
        l[j+1] = key
    end = time.time()
    return (l,end-start)

print(insertion(generar_lista(10)))


