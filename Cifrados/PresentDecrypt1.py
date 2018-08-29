# -*- coding: utf-8 -*-
from BitsFunctions1 import rotationLeft,addZeros
from text_binary import text_to_bits,text_from_bits


#Programación de clave de 80 bit---> Genera subclaves de 64 bit
def SBox(entrada,cant):#4 bits de entrada,cantidad de bits de salida
    entrada=int(entrada,2)
    s={0:12,1:5,2:6,3:11,4:9,5:0,6:10,7:13,8:3,9:14,10:15,11:8,12:4,13:7,14:1,15:2}
    return addZeros(bin(s[entrada]),cant)

def invSBox(entrada,cant):#4 bits de entrada,cantidad de bits de salida
    entrada=int(entrada,2)
    s={0:5,1:14,2:15,3:8,4:12,5:1,6:2,7:13,8:11,9:4,10:6,11:3,12:0,13:7,14:9,15:10}
    return addZeros(bin(s[entrada]),cant)

def invPBox(i):#bit i es movido a la posición P(i)
    p={0:0,16:1,32:2,48:3,1:4,17:5,33:6,49:7,2:8,18:9,34:10,50:11,3:12,19:13,35:14,51:15,4:16,
       20:17,36:18,52:19,5:20,21:21,37:22,53:23,6:24,22:25,38:26,54:27,7:28,23:29,39:30,55:31,8:32,
       24:33,40:34,56:35,9:36,25:37,41:38,57:39,10:40,26:41,42:42,58:43,11:44,27:45,43:46,59:47,
       12:48,28:49,44:50,60:51,13:52,29:53,45:54,61:55,14:56,30:57,46:58,62:59,15:60,31:61,47:62,63:63}
    return p[i]#posición a la que tiene que ser movido el bit de posición i
    
def generateRoundKeys(userKey):#Entrada en binario userKey80-bit
    registerKey=addZeros(userKey,80)
    keys=list()
    for round in range(1,33):#1<=i<=32
        roundKey = registerKey[-80:-16]#K[79:16]
        keys.append(roundKey)
        registerKey = rotationLeft(registerKey,61)
        sbox = SBox(registerKey[-80:-76],4)#S[k79..k76]
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
        sbox1 = SBox(registerKey[-128:-124],4)#S[k127..k124]
        sbox2 = SBox(registerKey[-124:-120],4)#S[k123..k120]
        round=addZeros(bin(round),5)
        xor = int(registerKey[-67:-62],2)^int(round,2)#k66..k62 ^ round_counter
        xor = addZeros(bin(xor),5)
        registerKey=sbox1+sbox2+registerKey[-120:-67]+xor+registerKey[-62:]
        
    return keys
   
#The Block Cipher
def PRESENTDecr(tamañoclave,key,dataBlock):
   # if(key==""):
    #    key="0"
    #else:
     #   key="0b"+text_to_bits(key)
    if(tamañoclave==80):
        subKeys=generateRoundKeys(key)#key-User de 80 bit
    elif(tamañoclave==128):
        subKeys=generateRoundKeys2(key)
    else:
        return "Error, introduzca tamaño de clave válida"
    #dataBlock = bin(int(dataBlock, 16))
    #dataBlock=addZeros(dataBlock,64)

    def pLayer(state):
        #dataBlock-->64 bits
        state=list(state)[::-1]
        nueval=state.copy()
        for i in range(0,len(state)):
            nueval[invPBox(i)]=state[i]
        return "".join(nueval)[::-1]



    def addRoundKey(state,subkey):#dada ki de 64 bits y estado actual
        xor=int(state,2)^int(subkey,2)#subkey k63...k0
        state=addZeros(bin(xor),64)
        return state #STATE b63...b0
    
    def sBoxLayer(state):
        trozos=list()
        for i in range(0,16):
            #le restamos 63, ya que state es una cadena y la posicion 0 en python comienza por la izquierda
            w=state[63-(4*i+3)]+state[63-(4*i+2)]+state[63-(4*i+1)]+state[63-(4*i)]
            sbox=invSBox(w,4)
            trozos.insert(0,sbox)#w15...w0
        return "".join(trozos)



    state=addRoundKey(dataBlock,subKeys[32-1])
    #Algoritmo present
    for i in range(31,0,-1):#31<=i<=1
        state=pLayer(state)
        state=sBoxLayer(state)
        state=addRoundKey(state,subKeys[i-1])
    #return hex(int(state,2))[2:]
    return state

#print(PRESENTDecr(80,"afgfdtdhyj","5cab6c050f4a6dc2"))
#print(text_from_bits(PRESENTDecr(80,"afgfdtdhyj","5cab6c050f4a6dc2")))


