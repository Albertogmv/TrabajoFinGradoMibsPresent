# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros,addZerosHex
from Present1 import PRESENT
import codecs

#Recibe un texto de entrada y devuelve diccionario de bloques de 64 bits(el último 
#se rellena con ceros al principio si fuera necesario)
def bloqueDatosPRESENT(text):
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

def cifradoPRESENT(tamañoclave,key,texto):
    key="0b"+text_to_bits(key)
    if((tamañoclave==80 and (len(key)-2)>80) or (tamañoclave==128 and (len(key)-2)>128)):
        resultado="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueDatosPRESENT(texto)
        print(datos)
        texto_cifrado=""
        for i in datos:
            cifrabloque=PRESENT(tamañoclave,key,datos[i])
            texto_cifrado=texto_cifrado+addZerosHex(hex(int(cifrabloque,2))[2:])
        resultado=texto_cifrado
    return resultado
         
         
#print(cifradoPRESENT(128,"aeiouaeiou","Esto es un cifrado PRESENT y, funciona a la perfección"))
