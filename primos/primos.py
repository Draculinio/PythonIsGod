import time
import math
import sys

def es_primo(num):
    primo = True
    if num%2 == 0:
        return False
    limite = int(math.sqrt(num))+1
    for i in range(3, limite, 2):
        if num% i == 0:
            primo = False
            break
    return primo

def guardar_numero(nro):
    with open('primo.txt', 'w') as f:
        f.write(str(nro))

def cargar_numero():
    with open('primo.txt','r') as f:
        return int(f.read())

args = sys.argv
print(args)
num = 3
if len(args)>1:
    if args[1] == 'l':
        num = cargar_numero()
try:
    while True:
        comienzo = time.time()
        primo = es_primo(num)
        if primo:
            tiempo = time.time() - comienzo
            #print(f'{num} ({tiempo})')
            guardar_numero(num)
        num+=1
except KeyboardInterrupt:
    guardar_numero(num)
    print('Gracias, vuelva prontos')