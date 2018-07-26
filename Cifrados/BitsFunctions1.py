def rotationRight(number,cant):#number tiene que ser un string,cant--->veces a rotar
    for _ in range(0,cant):
        number=number[len(number)-1]+number[0:len(number)-1]
    return number

def rotationLeft(number,cant):#number tiene que ser un string,cant--->veces a rotar
    for _ in range(0,cant):
        number=number[1:] + number[0]
    return number

#Con esta función garantizo que tenga siempre la cadena bits adecuados
def addZeros(binario,longi):
    strnumero=str(binario)[2:]
    if(len(strnumero)<longi):
        ceros=longi-len(strnumero)
        for _ in range(0,ceros):
            strnumero='0'+strnumero
    return strnumero



def addZerosBloqueDatos(binario):
    if(len(binario)<64):
        ceros=64-len(binario)
        for _ in range(0,ceros):
            binario=binario + '0'
    return binario