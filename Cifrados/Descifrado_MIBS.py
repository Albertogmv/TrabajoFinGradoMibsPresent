# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros
from MIBSDecrypt import MIBSdecr
import codecs

#Recibe un texto de entrada y devuelve diccionario de bloques de 64 bits(el último 
#se rellena con ceros al principio si fuera necesario)
def bloqueCifrados(cifrado):
    bloques=dict()
    bloque=""
    #cont=1
    for e in cifrado:
        bloque=bloque + e
        if(len(bloque)==64):
            bloques[len(bloques)]=bloque
            #if(cont!=len(cifrado)):
            bloque=""
        #cont=cont+1

    print(bloques)
    return bloques

def descifrado(tamañoclave,key,cifrado):
    if(key==""):
        key="0"
    else:
        key="0b"+text_to_bits(key)
    if((tamañoclave==64 and (len(key)-2)>64) or (tamañoclave==80 and (len(key)-2)>80)):
        resultado="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueCifrados(cifrado)
        texto_descifrado=""
        for i in datos:
            descifrabloque=MIBSdecr(tamañoclave,key,datos[i])
            texto_descifrado=texto_descifrado+descifrabloque
        resultado=text_from_bits(texto_descifrado)
    return resultado
      

#print(descifrado(80,"hfjhf","51e4761dea38ca66c376e495b645c6de4250eb44775f6ecd47792324b3a41e22c6c12d78539b57a854e12bb7969d3cbf870b712896ac10d1"))
