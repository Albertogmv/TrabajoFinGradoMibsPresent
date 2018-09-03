# -*- coding: utf-8 -*-
from text_binary import text_to_bits,text_from_bits
from BitsFunctions1 import addZerosBloqueDatos,addZeros,addZerosHex
from MIBS import MIBS
import codecs

#Recibe un texto de entrada y devuelve diccionario de bloques de 64 bits(el último 
#se rellena con ceros al principio si fuera necesario)
def bloqueDatos(text):
    bloqueDatos = text_to_bits(text)
    #print(bloqueDatos,len(bloqueDatos))
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
    if((tamañoclave==64 and (len(key)-2)>64) or (tamañoclave==80 and (len(key)-2)>80)):
        resultado="Error: la clave supera los "+str(tamañoclave)+" bits."
    else:
        datos=bloqueDatos(texto)
        texto_cifrado=""
        for i in datos:
            print(datos[i])
            cifrabloque=MIBS(tamañoclave,key,datos[i])
            texto_cifrado=texto_cifrado+addZerosHex(hex(int(cifrabloque,2))[2:])
        resultado=texto_cifrado
    return resultado
         
         
#print(cifrado(64,"cifrMIBS","n un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo, los días de entre semana se honraba con su vellori de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años, era de complexión recia, seco de carnes, enjuto de rostro; gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los autores que deste caso escriben), aunque por conjeturas verosímiles se deja entender que se llama Quijana; pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad. "))
