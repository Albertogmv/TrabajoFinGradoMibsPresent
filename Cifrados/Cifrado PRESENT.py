# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros
from Present1 import PRESENT
import codecs

#Recibe un texto de entrada y devuelve diccionario de bloques de 64 bits(el último 
#se rellena con ceros al principio si fuera necesario)
def bloqueDatos(text):
    bloqueDatos = text_to_bits(text)
    bloques=dict()
    if(len(bloqueDatos)<=64):
        bloques[0]=addZerosBloqueDatos(bloqueDatos)
    else:
        bloque=""
        cont=1
        for e in bloqueDatos:
            bloque=bloque + e
            if(len(bloque)==64):
                bloques[len(bloques)]=bloque
                if(cont!=len(bloqueDatos)):
                    bloque=""
                elif(cont==len(bloqueDatos)):
                    bloques[len(bloques)]=bloque
            cont=cont+1
        bloques[len(bloques)]=addZerosBloqueDatos(bloque)
    return bloques

def cifrado(tamañoclave,key,texto):
    key="0b"+text_to_bits(key)
    if((tamañoclave==80 and (len(key)-2)>80) or (tamañoclave==128 and (len(key)-2)>128)):
        resultado="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueDatos(texto)
        texto_cifrado=""
        for i in datos:
            cifrabloque=PRESENT(tamañoclave,key,datos[i])
            texto_cifrado=texto_cifrado+cifrabloque
            print(texto_cifrado)
        resultado=texto_cifrado
    return resultado
         
         
print(cifrado(80,"hfjhf","Hola mi nombre es Alberto y esto es un cifrado PRESENT"))
