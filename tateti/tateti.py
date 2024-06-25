# 0 1 2
# 3 4 5
# 6 7 8

class Maquina():
    def __init__(self, ficha):
        self.ficha = ficha
        self.no_ficha = 'X' if ficha == 'O' else 'O'
    def mover(self,tablero):
        #1 intento ganar
        t = self.intentar_tateti(tablero,self.ficha)
        if t != None: return t
        #2 intento no perder
        t = self.intentar_tateti(tablero,self.no_ficha)
        if t != None: return t
        #3 intento jugar la mejor otra posible
        t = self.buscar_vacios(tablero, [4,0,2,6,8,1,3,5,7])
        if t != None: return t
    def intentar_tateti(self, tablero,ficha):
        for i in range(len(tablero)):
            if tablero[i]==' ':
                tablero_temp = tablero.copy()
                tablero_temp[i]=ficha
                if verificar(tablero_temp, ficha) == ficha:
                    tablero[i] = self.ficha
                    return tablero
        return None
    def buscar_vacios(self, tablero, orden):
        for i in orden:
            if tablero[i] == ' ':
                tablero[i] = self.ficha
                return tablero
        return None

def tablero_print(tablero):
    print(tablero[0]+'|'+tablero[1]+'|'+tablero[2])
    print('-----')
    print(tablero[3]+'|'+tablero[4]+'|'+tablero[5])
    print('-----')
    print(tablero[6]+'|'+tablero[7]+'|'+tablero[8])

def jugador(tablero, ficha):
    valido = False
    while valido == False:
        jugada = int(input('Ingrese su posicion: '))
        try:
            if tablero[jugada]==' ':
                tablero[jugada]=ficha
                valido = True
            else:
                print('Ese casillero ya esta ocupado')
        except:
            print('Solo puede elegir valores entre 0 y 9')
    return tablero

def verificar(tablero,ficha):
    if [ficha]*3 in [
        [tablero[0],tablero[1],tablero[2]],
        [tablero[3],tablero[4],tablero[5]],
        [tablero[6],tablero[7],tablero[8]],
        [tablero[0],tablero[3],tablero[6]],
        [tablero[1],tablero[4],tablero[7]],
        [tablero[2],tablero[5],tablero[8]],
        [tablero[0],tablero[4],tablero[8]],
        [tablero[2],tablero[4],tablero[6]]
    ]:
        return ficha
    if ' ' not in tablero:
        return 'Empate'
    return 'N'

tablero = [' ']*9
turno = 'X'
eog = 'N'
j = input('Elija su ficha (X/O): ')
maquinola = Maquina('X' if j == 'O' else 'O')
while eog == 'N':
    if j == turno:
        tablero = jugador(tablero, j)
    else:
        tablero = maquinola.mover(tablero)
    tablero_print(tablero)
    eog = verificar(tablero,turno)
    if eog != 'N':
        print(eog)
    else:    
        if turno=='X':
            turno='O'
        else:
            turno='X'