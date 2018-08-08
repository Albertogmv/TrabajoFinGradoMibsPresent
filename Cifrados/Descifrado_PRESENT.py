# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros
from PresentDecrypt1 import PRESENTDecr
import codecs

#Recibe un texto de entrada y devuelve diccionario de bloques de 64 bits(el último 
#se rellena con ceros al principio si fuera necesario)
def bloqueCifrados(cifrado):
    bloques=dict()
    bloque=""
    cont=1
    for e in cifrado:
        bloque=bloque + e
        if(len(bloque)==16):
            bloques[len(bloques)]=bloque
            if(cont!=len(cifrado)):
                bloque=""

        cont=cont+1
    return bloques

def descifrado(tamañoclave,key,cifrado):
    if(key==""):
        key="0b"
    else:
        key="0b"+text_to_bits(key)
    if((tamañoclave==80 and (len(key)-2)>80) or (tamañoclave==128 and (len(key)-2)>128)):
        resultado_texto="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueCifrados(cifrado)
        print(datos)
        texto_descifrado=""
        for i in datos:
            descifrabloque=PRESENTDecr(tamañoclave,key,datos[i])
            texto_descifrado=texto_descifrado+text_from_bits(descifrabloque)
            print(texto_descifrado)
        resultado_texto=texto_descifrado
    return resultado_texto
      

print(descifrado(128,"aeiouaeiou","167870c07847f9e199ea48344d348d2775bd68e376caea347db8e71988875e5b5dee4503d59cd775ecd39c8327fa17d746164ee8f4df734e"))