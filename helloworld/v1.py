
def convertir_frase(frase):
    return [int(frase[i:i+8],2) for i in range(0, len(frase), 8)]

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None
    
    def apilar(self, dato):
        if self.superior is None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def desapilar(self):
        if self.superior is None:
            return None
        dato = chr(self.superior.dato)
        self.superior = self.superior.siguiente
        return dato
    
hola_mundo_pila = Pila()
for i in convertir_frase('0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100')[::-1]:
    hola_mundo_pila.apilar(i)
dato = True
output = ''
while dato == True:
    try:
        output += hola_mundo_pila.desapilar()
    except:
        dato = False
print(output)