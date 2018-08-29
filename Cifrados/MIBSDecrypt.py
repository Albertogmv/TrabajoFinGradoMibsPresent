from BitsFunctions1 import addZeros,rotationRight

def Sbox(entrada,cant):#4 bits de entrada,cant bits de salida
    entrada=int(entrada,2)
    s={0:4,1:15,2:3,3:8,4:13,5:10,6:12,7:0,8:11,9:5,10:7,11:14,12:2,13:6,14:1,15:9}
    return addZeros(bin(s[entrada]),cant)

def Pbox(i):#trozo i es movido a la posición P(i)
    p=[1,7,0,2,5,6,3,4]
    return p[i]#posición a la que tiene que ser movido el trozo de posición i
    
def generaterondaKeys(userKey):
    registerKey=addZeros(userKey,64)
    state=registerKey
    subkeys=list()
    for ronda in range(1,33):
        state=rotationRight(state,15)
        state=Sbox(state[-64:-60],4)+state[-60:]
        rondaCounter=addZeros(bin(ronda),5)
        #print(rondaCounter)
        xor=int(state[-16:-11],2)^int(rondaCounter,2)
        state=state[-64:-16]+addZeros(bin(xor),5)+state[-11:]
        rondaKey=state[-64:-32]
        subkeys.append(rondaKey)
    #print(subkeys,len(subkeys))
    return subkeys

def generaterondaKeys2(userKey):
    registerKey=addZeros(userKey,80)
    state=registerKey
    subkeys=list()
    for ronda in range(1,33):
        state=rotationRight(state,19)
        state=Sbox(state[-80:-76],4)+Sbox(state[-76:-72],4)+state[-72:]
        rondaCounter=addZeros(bin(ronda),5)
        xor=int(state[-19:-14],2)^int(rondaCounter,2)
        state=state[-80:-19]+addZeros(bin(xor),5)+state[-14:]
        rondaKey=state[-80:-48]
        subkeys.append(rondaKey)
    #print(subkeys,len(subkeys))
    return subkeys

def MIBSdecr(tamañoclave,key,dataBlock):
    def keyAddition(state,subkey):
        state=int(state,2)^int(subkey,2)
        return addZeros(bin(state),32)
    
    def substitutionLayer(state):
        nibbles={}
        for i in range(0,8):
            #le restamos 31, ya que state es una cadena y la posicion 0 en python comienza por la izquierda
            y=state[31-(4*i+3)]+state[31-(4*i+2)]+state[31-(4*i+1)]+state[31-(4*i)]
            sbox=Sbox(y,4)
            nibbles["y"+str(i+1)]=sbox
        return nibbles
    
    def mixingLayer(nibbles):
        y=list()
        y1=int(nibbles['y2'],2)^int(nibbles['y3'],2)^int(nibbles['y4'],2)^int(nibbles['y5'],2)^int(nibbles['y6'],2)^int(nibbles['y7'],2)
        y1=addZeros(bin(y1),4)#y1 actualizado
        y.insert(0,y1)
        #print("y1':",y1)
        y2=int(nibbles['y1'],2)^int(nibbles['y3'],2)^int(nibbles['y4'],2)^int(nibbles['y6'],2)^int(nibbles['y7'],2)^int(nibbles['y8'],2)
        y2=addZeros(bin(y2),4)
        y.insert(0,y2)
        #print("y2':",y2)
        y3=int(nibbles['y1'],2)^int(nibbles['y2'],2)^int(nibbles['y4'],2)^int(nibbles['y5'],2)^int(nibbles['y7'],2)^int(nibbles['y8'],2)
        y3=addZeros(bin(y3),4)
        y.insert(0,y3)
        #print("y3':",y3)        
        y4=int(nibbles['y1'],2)^int(nibbles['y2'],2)^int(nibbles['y3'],2)^int(nibbles['y5'],2)^int(nibbles['y6'],2)^int(nibbles['y8'],2)
        y4=addZeros(bin(y4),4)
        y.insert(0,y4)
        #print("y4':",y4) 
        y5=int(nibbles['y1'],2)^int(nibbles['y2'],2)^int(nibbles['y4'],2)^int(nibbles['y5'],2)^int(nibbles['y6'],2)
        y5=addZeros(bin(y5),4)
        y.insert(0,y5)
        #print("y5':",y5)
        y6=int(nibbles['y1'],2)^int(nibbles['y2'],2)^int(nibbles['y3'],2)^int(nibbles['y6'],2)^int(nibbles['y7'],2)
        y6=addZeros(bin(y6),4)
        y.insert(0,y6)
        #print("y6':",y6)
        y7=int(nibbles['y2'],2)^int(nibbles['y3'],2)^int(nibbles['y4'],2)^int(nibbles['y7'],2)^int(nibbles['y8'],2)
        y7=addZeros(bin(y7),4)
        y.insert(0,y7)
        #print("y7':",y7)
        y8=int(nibbles['y1'],2)^int(nibbles['y3'],2)^int(nibbles['y4'],2)^int(nibbles['y5'],2)^int(nibbles['y8'],2)
        y8=addZeros(bin(y8),4)
        y.insert(0,y8)
        #print("y8':",y8)

        return y

    def permutationLayer(nibbles):
        nibbles=nibbles[::-1]
        newl=nibbles.copy()
        for i in range(0,len(nibbles)):
            newl[Pbox(i)]=nibbles[i]
        newl=newl[::-1]
        #print(newl)
        return "".join(newl)

   # key = bin(int(key, 16))
    if(tamañoclave==64):
        subKeys=generaterondaKeys(key)#key-User de 80 bit
    elif(tamañoclave==80):
        subKeys=generaterondaKeys2(key)
    else:
        return "Error, introduzca tamaño de clave válida"
   
    #state = dataBlock  
    #dataBlock = bin(int(dataBlock, 16))
    #dataBlock=addZeros(dataBlock,64)

    split = int(len(dataBlock)/2)
    left = [None]*(32+1)
    right= [None]*(32+1)
    left[0]=dataBlock[:split]
    right[0]=dataBlock[split:]

    for ronda in range(1,33):
        #print("ronda:",ronda)
        temp=right[ronda-1]
        #Función F
        state=keyAddition(right[ronda-1],subKeys[32-ronda])
        #print("key addition:",state)
        
        nibbles=substitutionLayer(state)
        #print("substitutionLayer:",nibbles)

        nibbles=mixingLayer(nibbles)
        #print("mixingLayer:",nibbles)

        state=permutationLayer(nibbles)
        #print("permutationLayer:",state)

        state=int(state,2)^int(left[ronda-1],2)
        #print("XOR:",addZeros(bin(state),32))
        right[ronda]=addZeros(bin(state),32)
        left[ronda]=temp

    cipherText=left[ronda]+right[ronda]
    #cipherText=hex(int(cipherText,2))[2:]
    return cipherText

#print(MIBSdecr(80,"ffffffffffffffff","72ecac2a66ff2059"))
#print("Deberia salir: ffffffffffffffff")        
