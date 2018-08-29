# -*- coding: utf-8 -*-
from BitsFunctions1 import rotationLeft,addZeros

#Programación de clave de 80 bit---> Genera subclaves de 64 bit
def SBoxPRESENT(entrada,cant):#4 bits de entrada,cantidad de bits de salida
    entrada=int(entrada,2)
    s={0:12,1:5,2:6,3:11,4:9,5:0,6:10,7:13,8:3,9:14,10:15,11:8,12:4,13:7,14:1,15:2}
    return addZeros(bin(s[entrada]),cant)

def PBoxPRESENT(i):#bit i es movido a la posición P(i)
    p={0:0,1:16,2:32,3:48,4:1,5:17,6:33,7:49,8:2,9:18,10:34,11:50,12:3,13:19,14:35,15:51,16:4,
       17:20,18:36,19:52,20:5,21:21,22:37,23:53,24:6,25:22,26:38,27:54,28:7,29:23,30:39,31:55,32:8,
       33:24,34:40,35:56,36:9,37:25,38:41,39:57,40:10,41:26,42:42,43:58,44:11,45:27,46:43,47:59,
       48:12,49:28,50:44,51:60,52:13,53:29,54:45,55:61,56:14,57:30,58:46,59:62,60:15,61:31,62:47,63:63}
    return p[i]#posición a la que tiene que ser movido el bit de posición i
    


def generateRoundKeys(userKey):#Entrada en binario userKey80-bit
    registerKey=addZeros(userKey,80)
    keys=list()
    for round in range(1,33):#1<=i<=32
        roundKey = registerKey[-80:-16]#K[79:16]
        keys.append(roundKey)
        registerKey = rotationLeft(registerKey,61)
        sbox = SBoxPRESENT(registerKey[-80:-76],4)#S[k79..k76]
        round=addZeros(bin(round),5)
        xor = int(registerKey[-20:-15],2)^int(round,2)#k19..k15 ^ round_counter
        xor = addZeros(bin(xor),5)
        registerKey=sbox+registerKey[-76:-20]+xor+registerKey[-15:]
        
    return keys

def generateRoundKeys2(userKey):#Entrada en binario userKey 128-bit
    registerKey=addZeros(userKey,128)
    keys=list()
    for round in range(1,33):#1<=i<=32
        roundKey = registerKey[-128:-64]#K[127:64]
        keys.append(roundKey)
        registerKey = rotationLeft(registerKey,61)
        sbox1 = SBoxPRESENT(registerKey[-128:-124],4)#S[k127..k124]
        sbox2 = SBoxPRESENT(registerKey[-124:-120],4)#S[k123..k120]
        round=addZeros(bin(round),5)
        xor = int(registerKey[-67:-62],2)^int(round,2)#k66..k62 ^ round_counter
        xor = addZeros(bin(xor),5)
        registerKey=sbox1+sbox2+registerKey[-120:-67]+xor+registerKey[-62:]
        
    return keys
   
#The Block Cipher
def PRESENT(tamañoclave,key,dataBlock):#si la clave es 80-->80 bit, si es 128-->128 bits.
    #key = bin(int(key, 16))
    if(tamañoclave==80):
        subKeys=generateRoundKeys(key)#key-User de 80 bit
    elif(tamañoclave==128):
        subKeys=generateRoundKeys2(key)
    else:
        return "Error, introduzca tamaño de clave válida"
   
    state = dataBlock  
    #dataBlock = bin(int(dataBlock, 16))
    #state=addZeros(dataBlock,64)

    def addRoundKey(state,subkey):#dada ki de 64 bits y estado actual
        xor=int(state,2)^int(subkey,2)#subkey k63...k0
        state=addZeros(bin(xor),64)
        return state #STATE b63...b0
    
    def sBoxLayer(state):
        trozos=list()
        for i in range(0,16):
            #le restamos 63, ya que state es una cadena y la posicion 0 en python comienza por la izquierda
            w=state[63-(4*i+3)]+state[63-(4*i+2)]+state[63-(4*i+1)]+state[63-(4*i)]
            sbox=SBoxPRESENT(w,4)
            trozos.insert(0,sbox)#w15...w0
        return "".join(trozos)

    def pLayer(state):
        #dataBlock-->64 bits
        state=list(state)[::-1]
        nueval=state.copy()
        for i in range(0,len(state)):
            nueval[PBoxPRESENT(i)]=state[i]
        return "".join(nueval)[::-1]


    #Algoritmo present
    for i in range(1,32):#1<=i<=31
        state=addRoundKey(state,subKeys[i-1])
        state=sBoxLayer(state)
        state=pLayer(state)

    cipherText=addRoundKey(state,subKeys[32-1])
    return cipherText

#print(PRESENT(80,"ffffffffffffffffffff","ffffffffffffffff"))

