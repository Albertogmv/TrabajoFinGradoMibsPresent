# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros
from Present2 import PRESENT
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
        key="0"
    else:
        key="0b"+text_to_bits(key)
    if((tamañoclave==80 and (len(key)-2)>80) or (tamañoclave==128 and (len(key)-2)>128)):
        resultado_texto="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueCifrados(cifrado)
        texto_descifrado=""
        for i in datos:
            descifrabloque=PRESENTDecr(tamañoclave,key,datos[i])
            texto_descifrado=texto_descifrado+descifrabloque
        resultado=texto_descifrado
        resultado_texto=text_from_bits(resultado)
    return resultado_texto
      

print(descifrado(80,"hfjhf","d234faf8d9474ce997d34a1934d7a8ff4094e592cacf4c5c4ce98166d7740fe99419c40bd6e50f4b23689832140b92a6c9562478d0864ef1"))
