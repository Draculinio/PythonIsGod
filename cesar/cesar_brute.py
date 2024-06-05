import sys
import time


start = time.time()
alfabeto = "abcdefghijklmnopqrstuvwxyz"
with open(sys.argv[1], 'r') as f:
    d = f.read()            
with open(sys.argv[1]+'BRUTE', 'w') as f:
    for c in range(27):
        f.write("\n\nIntento "+str(c)+"\n\n")
        for i in d:
            l = i.lower()
            if l in alfabeto:
                final = alfabeto[(alfabeto.find(l) - c) % 26]
                f.write(final.upper() if i.isupper() else final)
            else:
                f.write(i)
print("Todas las posibilidades escaneadas en: "+str(time.time()-start))
