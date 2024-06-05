import sys

def codifica(archivo, accion, c):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    with open(archivo, 'r') as f:
        d = f.read()
    with open(archivo+'result', 'w') as f:
        sign = {'c':1, 'd':-1}
        for i in d:
            l = i.lower()
            if l in alfabeto:
                final = alfabeto[(alfabeto.find(l) + sign[accion]*int(c)) % 26]
                f.write(final.upper() if i.isupper() else final)
            else:
                f.write(i)
                
codifica(sys.argv[2], sys.argv[1], sys.argv[3])