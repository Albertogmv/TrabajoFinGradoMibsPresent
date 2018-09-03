import sys
from PyQt5 import uic, QtWidgets, QtCore
from Cifrado_MIBS import *
from Descifrado_MIBS import descifrado
from Cifrado_PRESENT import *
from Descifrado_PRESENT import descifradoPRESENT
from MIBS import *
from Present1 import *
from obtencionclavesMIBS import Ui_procesoSubclaves
from SBoxMIBS import Ui_SBoxMIBS
from PBoxMIBS import Ui_PBoxMIBS
from SBoxPRESENT import Ui_SBoxPRESENT
from PBoxPRESENT import Ui_PBoxPRESENT
from obtencionclavesPRESENT import Ui_procesoSubclavesPresent
from AlgoritmoMIBS import Ui_AlgoritmoMIBS
from AlgoritmoPRESENT import Ui_AlgoritmoPRESENT




qtCreatorFile = "/home/alberto/Escritorio/principaltab.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    #Cifrado de bloques MIBS

        #Cifrado/descifrado MIBS
        self.botoncifra.clicked.connect(self.cifradoMibs)
        self.botondescifra.clicked.connect(self.descifradoMibs)
 #       self.hexcifr.clicked.connect(self.convierteCifradoHex)
        #MIBS didáctico
        #Paso 1: convertir texto a binario
        self.botonConvertirBin.clicked.connect(self.convierteBinario)
        #Paso 2: dividir texto binario en bloques de 64 bits
        self.botontrozeardidactico.clicked.connect(self.bloques64)
        #Paso 3: convertimos clave a binario
        self.botonconvertirclave.clicked.connect(self.transformabinario)
        #Paso 4: generamos sublaves
        self.botonsubclaves.clicked.connect(self.generaSubclaves)
        #Ver algoritmo generación de claves
        self.botonalgoritmoclaves.clicked.connect(self.algoritmoclaves)
        #Paso 5:Cifrado MIBS a cada bloque
        self.botoncifrarbloques.clicked.connect(self.cifrabloques)
        #Ver algoritmo cifrado MIBS
        self.botonverprocesocifrado.clicked.connect(self.algoritmoMIBS)
        #Paso 6:Anidamos todos los bloques cifrados
        self.botontextocifrado.clicked.connect(self.cifratexto)
        self.hexadecimal.clicked.connect(self.textoHex)

        #Cifrado/descifrado PRESENT
        self.botoncifraPRES.clicked.connect(self.cifradoPresent)
        self.botondescifraPRES.clicked.connect(self.descifradoPresent)
        #PRESENT didáctico
        #Paso 1: convertir texto a binario
        self.botonConvertirBinPRES.clicked.connect(self.convierteBinarioPresent)
        #Paso 2: dividir texto binario en bloques de 64 bits
        self.botontrozeardidacticoPRES.clicked.connect(self.bloques64Present)
        #Paso 3: convertimos clave a binario
        self.botonconvertirclavePRES.clicked.connect(self.transformabinarioPRES)
        #Paso 4: generamos sublaves
        self.botonsubclavesPRES.clicked.connect(self.generaSubclavesPRES)
        #Ver algoritmo generación de claves
        self.botonalgoritmoclavesPRES.clicked.connect(self.algoritmoclavesPRES)
        #Paso 5:Cifrado PRESENT a cada bloque
        self.botoncifrarbloquesPRES.clicked.connect(self.cifrabloquesPRES)
        #Ver algoritmo cifradoPRESENT
        self.botonverprocesocifradoPRES.clicked.connect(self.algoritmoPRESENT)
        #Paso 6:Anidamos todos los bloques cifrados
        self.botontextocifradoPRES.clicked.connect(self.cifratextoPRES)
        self.hexadecimalPres.clicked.connect(self.textoHexPRES)


    
    #Cifrado/descifrado MIBS
    def cifradoMibs(self):
        textoclaro=self.textoc.toPlainText()
        if(self.boton_64.isChecked()):
            tamañoClave=64
        elif(self.boton_80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave_2.text()
        if(textoclave==""):
            res="Error: Introduzca una clave"
        else:
            res=cifrado(tamañoClave,textoclave,textoclaro)
        self.textoresultado_2.setText(res)
        self.statusBar().showMessage("Texto cifrado correctamente.")
        #self.hexcifr.setEnabled(True)
    # def convierteCifradoHex(self):
    #     textobinario=self.textoresultado_2.toPlainText()
    #     self.textoresultado_2.setText(hex(int(textobinario,2))[2:])
        


    def descifradoMibs(self):
        textocifrado=self.textoc.toPlainText()
        if(self.boton_64.isChecked()):
            tamañoClave=64
        elif(self.boton_80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave_2.text()
        if(textoclave==""):
            res="Error: Introduzca una clave"
        else:
            res=descifrado(tamañoClave,textoclave,textocifrado)
        self.textoresultado_2.setText(res)
        self.statusBar().showMessage("Texto descifrado correctamente.")


    #MIBS didáctico
    #Paso 1:
    def convierteBinario(self):
        textoclaro=self.textoclarodidactico.toPlainText()
        bloqueDatos = text_to_bits(textoclaro)
        self.textobinario.setText(bloqueDatos)  
        self.statusBar().clearMessage()
 
   
    #Paso 2:
    def bloques64(self):
        textoclaro=self.textoclarodidactico.toPlainText()
        bloques=bloqueDatos(textoclaro)
        res=str()
        for k,v in zip(bloques.keys(),bloques.values()):
            res= res + ("Bloque " + str(k) + ": " + str(v) + "\n")
        self.bloquesbinario.setText(res)
        self.statusBar().showMessage('Pulse en la pestaña MIBS didáctico (2) para continuar el algoritmo')

    #Paso 3:
    def transformabinario(self):
        claveBinario=text_to_bits(self.textoclavebin.text())
        self.textoclavebin.setText(claveBinario)
        self.statusBar().showMessage('Clave transformada a binario')
    
    #Paso 4:
    def generaSubclaves(self):
        self.statusBar().showMessage('Generando subclaves...')
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        claves=generaterondaKeys(claveBinario)
        res=""
        for clave in claves:
            res = res + "Clave para ronda "+str(claves.index(clave)+1)+": "+str(clave+"\n")

        self.textosubclaves.setText(res)
        self.statusBar().showMessage('Se han generado 32 claves de ronda de manera satisfactoria')
    

    #Algoritmo generación claves
    def algoritmoclaves(self):
        self.ventanaProceso=QtWidgets.QMainWindow()
        self.ui=Ui_procesoSubclaves()
        self.ui.setupUi(self.ventanaProceso)
        self.ventanaProceso.show()
        #Paso 1:
        self.ui.botonrotar.clicked.connect(self.rotar)
        #Paso 2:
        self.ui.botonsbox.clicked.connect(self.sust)
        #Ver SBox
        self.ui.botonverSBox2.clicked.connect(self.muestraSBoxMIBS)

        #Paso 3:
        self.ui.botonxor.clicked.connect(self.xor)

        #Paso 4:
        self.ui.botonsubclave.clicked.connect(self.subclave) 
  
    def rotar(self):
        state=self.ui.textoclaveinicial.text()
        self.ui.textorota.setText(rotationRight(state,15))
        self.ui.statusbar.showMessage('state (registro estado) rotado 15 bits a la derecha')
        self.ui.botonrotar.setEnabled(False)
        self.ui.botonsbox.setEnabled(True)

    def sust(self):
        state=self.ui.textorota.text()
        state2=Sbox(state[-64:-60],4)+state[-60:]
        self.ui.textosbox.setText(state2)
        self.ui.statusbar.showMessage('4 bits más a la izquierda actualizados correctamente')
        self.ui.botonsbox.setEnabled(False)
        self.ui.botonxor.setEnabled(True)
   
    def xor(self):
        state=self.ui.textosbox.text()
        ronda=self.ui.ronda.value()
        rondaCounter=addZeros(bin(ronda),5)
        xor=int(state[-16:-11],2)^int(rondaCounter,2)
        state=state[-64:-16]+addZeros(bin(xor),5)+state[-11:]
        self.ui.textoxor.setText(state)
        self.ui.statusbar.showMessage('Operación xor realizada correctamente.State actualizado.')
        self.ui.botonxor.setEnabled(False)
        self.ui.botonsubclave.setEnabled(True)

    def subclave(self):
        res=self.ui.textEdit.toPlainText()
        ronda=self.ui.ronda.value()
        state=self.ui.textoxor.text()
        clave=state[-64:-32]
        self.ui.textoclave.setText(clave)
        res += "Clave de ronda "+str(ronda)+": "+clave+"\n"
        self.ui.textEdit.setText(res)
        self.ui.textoclaveinicial.setText(state)
        if(ronda!=32):
            self.ui.statusbar.showMessage('Nueva clave de ronda generada. Volver al paso 1.')
            self.ui.botonsubclave.setEnabled(False)
            self.ui.botonrotar.setEnabled(True)
        else:
            self.ui.statusbar.showMessage('Fin del algoritmo. Se han generado 32 claves de ronda de manera satisfactoria')
            self.ui.botonsubclave.setEnabled(False)

    #Paso 5:
    def cifrabloques(self):
        self.statusBar().showMessage('Cifrando bloques...')
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        textoclaro=self.textoclarodidactico.toPlainText()
        datos=bloqueDatos(textoclaro)
        bloques=""
        for i in datos:
            cifrabloque=MIBS(64,claveBinario,datos[i])
            bloques= bloques + "Bloque "+str(i)+": "+cifrabloque+"\n"
        resultado=bloques
        self.textobloquescifrados.setText(resultado)
        self.statusBar().showMessage('152 bloques cifrados de manera satisfactoria')
        
    #Ver algoritmo cifrado MIBS

    def algoritmoMIBS(self):
        self.ventanaProceso2=QtWidgets.QMainWindow()
        self.ui2=Ui_AlgoritmoMIBS()
        self.ui2.setupUi(self.ventanaProceso2)
        self.ventanaProceso2.show()
        #Paso 0:Divide bloque inicial
        self.ui2.botondividir.clicked.connect(self.dividir)
        #Paso 1: Adición de clave:
        self.ui2.botonxor.clicked.connect(self.adicionClave)
        #Paso 2.Capa de sustitución:
        self.ui2.botonTrozear.clicked.connect(self.trozear)
        self.ui2.botontransformar.clicked.connect(self.transforma)
        #Ver SBox
        self.ui2.botonverSBox.clicked.connect(self.muestraSBoxMIBS)
        #Paso 3.Capa de mezcla:
        self.ui2.botonmezclar.clicked.connect(self.mezcla)
        #Paso 4.Capa de permutación.
        self.ui2.botonPermutar.clicked.connect(self.permuta)
        #Ver PBox
        self.ui2.botonverPBox.clicked.connect(self.muestraPBoxMIBS)
        #Paso 5.Obtención nuevo bloque de ronda Left
        self.ui2.botonxor_2.clicked.connect(self.nuevoleft)
        #Paso 6. Nueva Ronda.
        self.ui2.botonsiguienteronda.clicked.connect(self.nuevaRonda)
    
    def dividir(self):
        bloque=self.ui2.textoclaro.text()
        split = int(len(bloque)/2)
        self.ui2.leftinicial.setText(bloque[:split])
        self.ui2.rightinicial.setText(bloque[split:])
        self.ui2.botondividir.setEnabled(False)
        self.ui2.left.setText(self.ui2.leftinicial.text())
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        claves=generaterondaKeys(claveBinario)
        clave=claves[self.ui2.ronda.value()-1]
        self.ui2.claveronda.setText(clave)
        self.ui2.botonxor.setEnabled(True)
        self.ui2.statusbar.showMessage('Bloque inicial dividido correctamente. Comienza la ronda 1.')


    def adicionClave(self):
        left=self.ui2.left.text()
        clavei=self.ui2.claveronda.text()
        state=int(left,2)^int(clavei,2)
        self.ui2.resultadoxor.setText(addZeros(bin(state),32))
        self.ui2.botonxor.setEnabled(False)
        self.ui2.botonTrozear.setEnabled(True)
        self.ui2.statusbar.showMessage('Xor realizado con éxito. Nuevo state obtenido.')


    def trozear(self):
        state=self.ui2.resultadoxor.text()
        #le restamos 31, ya que state es una cadena y la posicion 0 en python comienza por la izquierda
        y1=state[31-(4*0+3)]+state[31-(4*0+2)]+state[31-(4*0+1)]+state[31-(4*0)]
        self.ui2.trozo1.setText(y1)
        y2=state[31-(4*1+3)]+state[31-(4*1+2)]+state[31-(4*1+1)]+state[31-(4*1)]
        self.ui2.trozo2.setText(y2)
        y3=state[31-(4*2+3)]+state[31-(4*2+2)]+state[31-(4*2+1)]+state[31-(4*2)]
        self.ui2.trozo3.setText(y3)
        y4=state[31-(4*3+3)]+state[31-(4*3+2)]+state[31-(4*3+1)]+state[31-(4*3)]
        self.ui2.trozo4.setText(y4)
        y5=state[31-(4*4+3)]+state[31-(4*4+2)]+state[31-(4*4+1)]+state[31-(4*4)]
        self.ui2.trozo5.setText(y5)
        y6=state[31-(4*5+3)]+state[31-(4*5+2)]+state[31-(4*5+1)]+state[31-(4*5)]
        self.ui2.trozo6.setText(y6)
        y7=state[31-(4*6+3)]+state[31-(4*6+2)]+state[31-(4*6+1)]+state[31-(4*6)]
        self.ui2.trozo7.setText(y7)
        y8=state[31-(4*7+3)]+state[31-(4*7+2)]+state[31-(4*7+1)]+state[31-(4*7)]
        self.ui2.trozo8.setText(y8)
        
        self.ui2.botonTrozear.setEnabled(False)
        self.ui2.botontransformar.setEnabled(True)
        self.ui2.statusbar.showMessage('state trozeado correctamente. Pulse botón "Transformar por SBox" para actualizar valores.')


    def transforma(self):
        y1=self.ui2.trozo1.text()
        y2=self.ui2.trozo2.text()
        y3=self.ui2.trozo3.text()
        y4=self.ui2.trozo4.text()
        y5=self.ui2.trozo5.text()
        y6=self.ui2.trozo6.text()
        y7=self.ui2.trozo7.text()
        y8=self.ui2.trozo8.text()
        #Sbox
        self.ui2.trozo1.setText(Sbox(y1,4))
        self.ui2.trozo2.setText(Sbox(y2,4))
        self.ui2.trozo3.setText(Sbox(y3,4))
        self.ui2.trozo4.setText(Sbox(y4,4))
        self.ui2.trozo5.setText(Sbox(y5,4))
        self.ui2.trozo6.setText(Sbox(y6,4))
        self.ui2.trozo7.setText(Sbox(y7,4))
        self.ui2.trozo8.setText(Sbox(y8,4))

        self.ui2.botontransformar.setEnabled(False)
        self.ui2.botonmezclar.setEnabled(True)
        self.ui2.statusbar.showMessage('Pulse el botón "Mezclar" para continuar el algoritmo.')

        
    def mezcla(self):
        y1=self.ui2.trozo1.text()
        y2=self.ui2.trozo2.text()
        y3=self.ui2.trozo3.text()
        y4=self.ui2.trozo4.text()
        y5=self.ui2.trozo5.text()
        y6=self.ui2.trozo6.text()
        y7=self.ui2.trozo7.text()
        y8=self.ui2.trozo8.text()

        nuevoy1=int(y2,2)^int(y3,2)^int(y4,2)^int(y5,2)^int(y6,2)^int(y7,2)
        nuevoy1=addZeros(bin(nuevoy1),4)#y1 actualizado
        self.ui2.trozo1_2.setText(nuevoy1)
        nuevoy2=int(y1,2)^int(y3,2)^int(y4,2)^int(y6,2)^int(y7,2)^int(y8,2)
        nuevoy2=addZeros(bin(nuevoy2),4)
        self.ui2.trozo2_2.setText(nuevoy2)
        nuevoy3=int(y1,2)^int(y2,2)^int(y4,2)^int(y5,2)^int(y7,2)^int(y8,2)
        nuevoy3=addZeros(bin(nuevoy3),4)
        self.ui2.trozo3_2.setText(nuevoy3)
        nuevoy4=int(y1,2)^int(y2,2)^int(y3,2)^int(y5,2)^int(y6,2)^int(y8,2)
        nuevoy4=addZeros(bin(nuevoy4),4)
        self.ui2.trozo4_2.setText(nuevoy4)
        nuevoy5=int(y1,2)^int(y2,2)^int(y4,2)^int(y5,2)^int(y6,2)
        nuevoy5=addZeros(bin(nuevoy5),4)
        self.ui2.trozo5_2.setText(nuevoy5)
        nuevoy6=int(y1,2)^int(y2,2)^int(y3,2)^int(y6,2)^int(y7,2)
        nuevoy6=addZeros(bin(nuevoy6),4)
        self.ui2.trozo6_2.setText(nuevoy6)
        nuevoy7=int(y2,2)^int(y3,2)^int(y4,2)^int(y7,2)^int(y8,2)
        nuevoy7=addZeros(bin(nuevoy7),4)
        self.ui2.trozo7_2.setText(nuevoy7)
        nuevoy8=int(y1,2)^int(y3,2)^int(y4,2)^int(y5,2)^int(y8,2)
        nuevoy8=addZeros(bin(nuevoy8),4)
        self.ui2.trozo8_2.setText(nuevoy8)

        self.ui2.botonmezclar.setEnabled(False)
        self.ui2.botonPermutar.setEnabled(True)
        self.ui2.statusbar.showMessage('Trozos mezclados correctamente. Pulse la pestaña inferior "Algoritmo MIBS (2)" para continuar el Algoritmo.')


    def permuta(self):
        self.ui2.labely1.setEnabled(True)
        self.ui2.labely2.setEnabled(True)
        self.ui2.labely3.setEnabled(True)
        self.ui2.labely4.setEnabled(True)
        self.ui2.labely5.setEnabled(True)
        self.ui2.labely6.setEnabled(True)
        self.ui2.labely7.setEnabled(True)
        self.ui2.labely8.setEnabled(True)
        y1=self.ui2.trozo1_2.text()
        y2=self.ui2.trozo2_2.text()
        y3=self.ui2.trozo3_2.text()
        y4=self.ui2.trozo4_2.text()
        y5=self.ui2.trozo5_2.text()
        y6=self.ui2.trozo6_2.text()
        y7=self.ui2.trozo7_2.text()
        y8=self.ui2.trozo8_2.text()
        self.ui2.trozo8_3.setText(y5)
        self.ui2.trozo7_3.setText(y4)
        self.ui2.trozo6_3.setText(y7)
        self.ui2.trozo5_3.setText(y6)
        self.ui2.trozo4_3.setText(y3)
        self.ui2.trozo3_3.setText(y1)
        self.ui2.trozo2_3.setText(y8)
        self.ui2.trozo1_3.setText(y2)
        self.ui2.salida.setText(y5+y4+y7+y6+y3+y1+y8+y2)
        self.ui2.right.setText(self.ui2.rightinicial.text())

        self.ui2.botonPermutar.setEnabled(False)
        self.ui2.botonxor_2.setEnabled(True)
        self.ui2.statusbar.showMessage('Trozos permutados correctamente. Salida función F de Feistel obtenida. ')


    def nuevoleft(self):
        state=self.ui2.salida.text()
        right=self.ui2.right.text()
        state=int(state,2)^int(right,2)
        left=addZeros(bin(state),32)
        self.ui2.resultadoxor_2.setText(left)
        self.ui2.lefti.setText(left)
        self.ui2.righti.setText(self.ui2.leftinicial.text())
        self.ui2.botonxor_2.setEnabled(False)
        self.ui2.botonsiguienteronda.setEnabled(True)
        self.ui2.statusbar.showMessage('Nuevos bloques de ronda left y right obtenidos correctamente. Pulse "Siguiente Ronda" para comenzar una nueva ronda.')


    def nuevaRonda(self):
        self.ui2.tabWidget.setCurrentWidget(self.ui2.AlgoritmoMIBS1)
        self.ui2.leftinicial.setText(self.ui2.lefti.text())
        self.ui2.rightinicial.setText(self.ui2.righti.text())
        self.ui2.ronda.stepUp()
        self.ui2.botonsiguienteronda.setEnabled(False)
        self.ui2.botonxor.setEnabled(True)

    #Paso 6:
    def cifratexto(self):
        self.statusBar().showMessage('Anidando bloques cifrados...')    
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        textoclaro=self.textoclarodidactico.toPlainText()
        datos=bloqueDatos(textoclaro)
        textocifrado=""
        for i in datos:
            cifrabloque=MIBS(64,claveBinario,datos[i])
            textocifrado+=cifrabloque
        resultado=textocifrado
        self.textofinalcifrado.setText(resultado)
        self.statusBar().showMessage('Texto cifrado correctamente.')    
        self.hexadecimal.setEnabled(True)
        
    def textoHex(self):
        textobinario=self.textofinalcifrado.toPlainText()
        self.textofinalcifrado.setText(hex(int(textobinario,2))[2:])

#Cifrado de bloques PRESENT

        

        #Cifrado/descifrado PRESENT
    def cifradoPresent(self):
        textoclaro=self.textocPRES.toPlainText()
        if(self.boton80.isChecked()):
            tamañoClave=80
        elif(self.boton128.isChecked()):
            tamañoClave=128
        textoclave=self.textoclavePRES.text()
        if(textoclave==""):
            res="Error: Introduzca una clave"
        else:
            res=cifradoPRESENT(tamañoClave,textoclave,textoclaro)
        self.textoresultadoPRES.setText(res)
        self.statusBar().showMessage("Texto cifrado correctamente.")


    def descifradoPresent(self):
        textocifrado=self.textocPRES.toPlainText()
        if(self.boton80.isChecked()):
            tamañoClave=80
        elif(self.boton128.isChecked()):
            tamañoClave=128
        textoclave=self.textoclavePRES.text()
        if(textoclave==""):
            res="Error: Introduzca una clave"
        else:
            res=descifradoPRESENT(tamañoClave,textoclave,textocifrado)
        self.textoresultadoPRES.setText(res)
        self.statusBar().showMessage("Texto descifrado correctamente.")


    #Paso 1
    def convierteBinarioPresent(self):
        textoclaro=self.textoclarodidacticoPRES.toPlainText()
        bloqueDatos = text_to_bits(textoclaro)
        self.textobinarioPRES.setText(bloqueDatos)   
        self.statusBar().clearMessage()

   
    #Paso 2:
    def bloques64Present(self):
        textoclaro=self.textoclarodidacticoPRES.toPlainText()
        bloques=bloqueDatos(textoclaro)
        res=str()
        for k,v in zip(bloques.keys(),bloques.values()):
            res= res + ("Bloque " + str(k) + ": " + str(v) + "\n")
        self.bloquesbinarioPRES.setText(res)
        self.statusBar().showMessage('Pulse en la pestaña PRESENT didáctico (2) para continuar el algoritmo')

    #Paso 3:
    def transformabinarioPRES(self):
        claveBinario=text_to_bits(self.textoclavebinPRES.text())
        self.textoclavebinPRES.setText(claveBinario)
        self.statusBar().showMessage('Clave transformada a binario')
    
    #Paso 4:
    def generaSubclavesPRES(self):
        self.statusBar().showMessage('Generando subclaves...')
        claveBinario="0b01100011011010010110011001010000010100100100010101010011010001010100111001010100"
        claves=generateRoundKeys(claveBinario)
        res=""
        for clave in claves:
            if(claves.index(clave)!=31):
                res = res + "Clave para ronda "+str(claves.index(clave)+1)+": "+str(clave+"\n")
            else:
                res = res + "Clave adicional post blanqueamiento "+": "+str(clave+"\n")


        self.textosubclavesPRES.setText(res)
        self.statusBar().showMessage('Se han generado 32 claves de manera satisfactoria')

    #Algoritmo generación claves
    def algoritmoclavesPRES(self):
        self.ventanaProcesoPRES=QtWidgets.QMainWindow()
        self.ui=Ui_procesoSubclavesPresent()
        self.ui.setupUi(self.ventanaProcesoPRES)
        self.ventanaProcesoPRES.show()
        #Paso 1:
        self.ui.botonsubclavePRES.clicked.connect(self.subclavePRES) 
        #Paso 2:
        self.ui.botonrotar.clicked.connect(self.rotarPRES)
        #Paso 3:
        self.ui.botonsbox.clicked.connect(self.sustPRES)
        #Ver SBox
        self.ui.botonverSBoxPRES2.clicked.connect(self.muestraSBoxPRESENT)
        #Paso 4:
        self.ui.botonxor.clicked.connect(self.xorPRES)

    def subclavePRES(self):
        state=addZeros("0b"+self.ui.textoclavePRES.text(),80)
        clave=state[-80:-16]
        self.ui.textoclavePRES_2.setText(clave)

        ronda=self.ui.rondaPRES.value()
        res=self.ui.textEditPRES.toPlainText()
        res += "Clave de ronda "+str(ronda)+": "+clave+"\n"
        self.ui.textEditPRES.setText(res)
        if(ronda!=32):
            self.ui.statusbar.showMessage('Nueva clave generada.')
            self.ui.botonsubclavePRES.setEnabled(False)
            self.ui.botonrotar.setEnabled(True)
        else:
            self.ui.statusbar.showMessage('Fin del algoritmo. Se han generado 32 claves de ronda de manera satisfactoria')
            self.ui.botonsubclavePRES.setEnabled(False)

    def rotarPRES(self):
        state=self.ui.textoclavePRES.text()
        self.ui.textorotaPRES.setText(rotationLeft(state,61))
        self.ui.statusbar.showMessage('state (registro estado) rotado 61 bits a la izquierda')
        self.ui.botonrotar.setEnabled(False)
        self.ui.botonsbox.setEnabled(True)

    def sustPRES(self):
        state=self.ui.textorotaPRES.text()
        state2=SBoxPRESENT(state[-80:-76],4)+state[-76:]
        self.ui.textosboxPRES.setText(state2)
        self.ui.statusbar.showMessage('4 bits más a la izquierda actualizados correctamente')
        self.ui.botonsbox.setEnabled(False)
        self.ui.botonxor.setEnabled(True)

    def xorPRES(self):
        state=self.ui.textosboxPRES.text()
        ronda=self.ui.rondaPRES.value()
        rondaCounter=addZeros(bin(ronda),5)
        xor=int(state[-20:-15],2)^int(rondaCounter,2)
        xor=addZeros(bin(xor),5)
        state=state[-80:-20]+xor+state[-15:]
        self.ui.textoxorPRES.setText(state)
        self.ui.textoclavePRES.setText(state)
        self.ui.statusbar.showMessage('Operación xor realizada correctamente.State actualizado. Volver al paso 1.')
        self.ui.botonxor.setEnabled(False)
        self.ui.botonsubclavePRES.setEnabled(True)

    #Paso 5:
    def cifrabloquesPRES(self):
        self.statusBar().showMessage('Cifrando bloques...')
        claveBinario="0b01100011011010010110011001010000010100100100010101010011010001010100111001010100"
        textoclaro=self.textoclarodidacticoPRES.toPlainText()
        datos=bloqueDatos(textoclaro)
        bloques=""
        for i in datos:
            cifrabloque=PRESENT(80,claveBinario,datos[i])
            bloques= bloques + "Bloque "+str(i)+": "+cifrabloque+"\n"
        resultado=bloques
        self.textobloquescifradosPRES.setText(resultado)
        self.statusBar().showMessage('152 bloques cifrados de manera satisfactoria')


    #Ver algoritmo cifrado MIBS
    def algoritmoPRESENT(self):
        self.ventanaProcesoPRES=QtWidgets.QMainWindow()
        self.uiPRES=Ui_AlgoritmoPRESENT()
        self.uiPRES.setupUi(self.ventanaProcesoPRES)
        self.ventanaProcesoPRES.show()

        #Paso 1: Adición de clave:
        self.uiPRES.botonxor.clicked.connect(self.adicionClavePRESENT)
        # #Paso 2.Capa de sustitución:
        self.uiPRES.botonTrozear.clicked.connect(self.trozearPRESENT)
        self.uiPRES.botontransformar.clicked.connect(self.transformaPRESENT)
        # #Ver SBox
        self.uiPRES.verSBoxPRES.clicked.connect(self.muestraSBoxPRESENT)
        # #Paso 3.Capa de permutación.
        self.uiPRES.botonPermutar.clicked.connect(self.permutaPRESENT)
        # #Ver PBox
        self.uiPRES.botonVerPBoxPRES.clicked.connect(self.muestraPBoxPRESENT)
        # #Paso 4. Nueva Ronda.
        self.uiPRES.botonNuevaRonda.clicked.connect(self.nuevaRondaPRESENT)
        # #Paso Adicional al finalizar las 31 rondas.
        self.uiPRES.botonxor_2.clicked.connect(self.adicionClaveAdicional)
        #convierte cifrado hexadecimal
        self.uiPRES.botonhex.clicked.connect(self.convertirHex)



    def adicionClavePRESENT(self):
        statei=self.uiPRES.state.text()
        clavei=self.uiPRES.claveronda.text()
        state=int(statei,2)^int(clavei,2)
        self.uiPRES.resultadoxor.setText(addZeros(bin(state),64))
        self.uiPRES.botonxor.setEnabled(False)
        self.uiPRES.botonTrozear.setEnabled(True)

    def trozearPRESENT(self):
        state=self.uiPRES.resultadoxor.text()
        #le restamos 63, ya que state es una cadena y la posicion 0 en python comienza por la izquierda
        w0=state[63-(4*0+3)]+state[63-(4*0+2)]+state[63-(4*0+1)]+state[63-(4*0)]
        self.uiPRES.trozo0.setText(w0)
        w1=state[63-(4*1+3)]+state[63-(4*1+2)]+state[63-(4*1+1)]+state[63-(4*1)]
        self.uiPRES.trozo1.setText(w1)
        w2=state[63-(4*2+3)]+state[63-(4*2+2)]+state[63-(4*2+1)]+state[63-(4*2)]
        self.uiPRES.trozo2.setText(w2)
        w3=state[63-(4*3+3)]+state[63-(4*3+2)]+state[63-(4*3+1)]+state[63-(4*3)]
        self.uiPRES.trozo3.setText(w3)
        w4=state[63-(4*4+3)]+state[63-(4*4+2)]+state[63-(4*4+1)]+state[63-(4*4)]
        self.uiPRES.trozo4.setText(w4)
        w5=state[63-(4*5+3)]+state[63-(4*5+2)]+state[63-(4*5+1)]+state[63-(4*5)]
        self.uiPRES.trozo5.setText(w5)
        w6=state[63-(4*6+3)]+state[63-(4*6+2)]+state[63-(4*6+1)]+state[63-(4*6)]
        self.uiPRES.trozo6.setText(w6)
        w7=state[63-(4*7+3)]+state[63-(4*7+2)]+state[63-(4*7+1)]+state[63-(4*7)]
        self.uiPRES.trozo7.setText(w7)
        w8=state[63-(4*8+3)]+state[63-(4*8+2)]+state[63-(4*8+1)]+state[63-(4*8)]
        self.uiPRES.trozo8.setText(w8)        
        w9=state[63-(4*9+3)]+state[63-(4*9+2)]+state[63-(4*9+1)]+state[63-(4*9)]
        self.uiPRES.trozo9.setText(w9)
        w10=state[63-(4*10+3)]+state[63-(4*10+2)]+state[63-(4*10+1)]+state[63-(4*10)]
        self.uiPRES.trozo10.setText(w10)
        w11=state[63-(4*11+3)]+state[63-(4*11+2)]+state[63-(4*11+1)]+state[63-(4*11)]
        self.uiPRES.trozo11.setText(w11)
        w12=state[63-(4*12+3)]+state[63-(4*12+2)]+state[63-(4*12+1)]+state[63-(4*12)]
        self.uiPRES.trozo12.setText(w12)
        w13=state[63-(4*13+3)]+state[63-(4*13+2)]+state[63-(4*13+1)]+state[63-(4*13)]
        self.uiPRES.trozo13.setText(w13)
        w14=state[63-(4*14+3)]+state[63-(4*14+2)]+state[63-(4*14+1)]+state[63-(4*14)]
        self.uiPRES.trozo14.setText(w14)
        w15=state[63-(4*15+3)]+state[63-(4*15+2)]+state[63-(4*15+1)]+state[63-(4*15)]
        self.uiPRES.trozo15.setText(w15)

        self.uiPRES.botonTrozear.setEnabled(False)
        self.uiPRES.botontransformar.setEnabled(True)

    def transformaPRESENT(self):
        #Sbox
        sw0=SBoxPRESENT(self.uiPRES.trozo0.text(),4)
        self.uiPRES.trozo0.setText(sw0)
        sw1=SBoxPRESENT(self.uiPRES.trozo1.text(),4)
        self.uiPRES.trozo1.setText(sw1)
        sw2=SBoxPRESENT(self.uiPRES.trozo2.text(),4)
        self.uiPRES.trozo2.setText(sw2)
        sw3=SBoxPRESENT(self.uiPRES.trozo3.text(),4)
        self.uiPRES.trozo3.setText(sw3)
        sw4=SBoxPRESENT(self.uiPRES.trozo4.text(),4)
        self.uiPRES.trozo4.setText(sw4)
        sw5=SBoxPRESENT(self.uiPRES.trozo5.text(),4)
        self.uiPRES.trozo5.setText(sw5)
        sw6=SBoxPRESENT(self.uiPRES.trozo6.text(),4)
        self.uiPRES.trozo6.setText(sw6)
        sw7=SBoxPRESENT(self.uiPRES.trozo7.text(),4)
        self.uiPRES.trozo7.setText(sw7)
        sw8=SBoxPRESENT(self.uiPRES.trozo8.text(),4)
        self.uiPRES.trozo8.setText(sw8)
        sw9=SBoxPRESENT(self.uiPRES.trozo9.text(),4)
        self.uiPRES.trozo9.setText(sw9)
        sw10=SBoxPRESENT(self.uiPRES.trozo10.text(),4)
        self.uiPRES.trozo10.setText(sw10)
        sw11=SBoxPRESENT(self.uiPRES.trozo11.text(),4)
        self.uiPRES.trozo11.setText(sw11)
        sw12=SBoxPRESENT(self.uiPRES.trozo12.text(),4)
        self.uiPRES.trozo12.setText(sw12)
        sw13=SBoxPRESENT(self.uiPRES.trozo13.text(),4)
        self.uiPRES.trozo13.setText(sw13)
        sw14=SBoxPRESENT(self.uiPRES.trozo14.text(),4)
        self.uiPRES.trozo14.setText(sw14)
        sw15=SBoxPRESENT(self.uiPRES.trozo15.text(),4)
        self.uiPRES.trozo15.setText(sw15)
        #Anidamos trozos
        self.uiPRES.statePaso2.setText(sw15+sw14+sw13+sw12+sw11+sw10+sw9+sw8+sw7+sw6+sw5+sw4+sw3+sw2+sw1+sw0)
        self.uiPRES.statePaso2_1.setText(sw15+sw14+sw13+sw12+sw11+sw10+sw9+sw8+sw7+sw6+sw5+sw4+sw3+sw2+sw1+sw0)        
        self.uiPRES.botontransformar.setEnabled(False)
        self.uiPRES.botonPermutar.setEnabled(True)



    def permutaPRESENT(self):
        statei=self.uiPRES.statePaso2_1.text()
        state=list(statei)[::-1]
        nueval=state.copy()
        for i in range(0,len(state)):
            nueval[PBoxPRESENT(i)]=state[i]
        self.uiPRES.resultadoPermutacion.setText("".join(nueval)[::-1])
        self.uiPRES.botonPermutar.setEnabled(False)
        if(self.uiPRES.ronda.value()==31):
            self.uiPRES.botonNuevaRonda.setEnabled(False)
        else:
            self.uiPRES.botonNuevaRonda.setEnabled(True)
            
        
        
    def nuevaRondaPRESENT(self):
        self.uiPRES.ronda.stepUp()
        state=self.uiPRES.resultadoPermutacion.text()
        self.uiPRES.state.setText(state)
        claveBinario="0b01100011011010010110011001010000010100100100010101010011010001010100111001010100"
        claves=generateRoundKeys(claveBinario)
        clave=claves[self.uiPRES.ronda.value()-1]
        self.uiPRES.claveronda.setText(clave)
        self.uiPRES.botonNuevaRonda.setEnabled(False)
        self.uiPRES.botonxor.setEnabled(True)
        self.uiPRES.tabWidget.setCurrentWidget(self.uiPRES.AlgoritmoPRESENT1)

    def adicionClaveAdicional(self):
        statei=self.uiPRES.stateadicionclave.text()
        clavei=self.uiPRES.clavepostblanq.text()
        state=int(statei,2)^int(clavei,2)
        self.uiPRES.resultadoxoradicional.setText(addZeros(bin(state),64))
        self.uiPRES.botonxor_2.setEnabled(False)
        self.uiPRES.botonhex.setEnabled(True)

    def convertirHex(self):
        cifrado=self.uiPRES.resultadoxoradicional.text()
        self.uiPRES.resultadoxoradicional.setText(hex(int(cifrado,2))[2:])



    #Paso 6:
    def cifratextoPRES(self):
        self.statusBar().showMessage('Anidando bloques cifrados...')    
        claveBinario="0b01100011011010010110011001010000010100100100010101010011010001010100111001010100"
        textoclaro=self.textoclarodidacticoPRES.toPlainText()
        datos=bloqueDatos(textoclaro)
        textocifrado=""
        for i in datos:
            cifrabloque=PRESENT(80,claveBinario,datos[i])
            textocifrado+=cifrabloque
        resultado=textocifrado
        self.textofinalcifradoPRES.setText(resultado)
        self.statusBar().showMessage('Texto cifrado correctamente.')
        self.hexadecimalPres.setEnabled(True)
    def textoHexPRES(self):
        textobinario=self.textofinalcifradoPRES.toPlainText()
        self.textofinalcifradoPRES.setText(hex(int(textobinario,2))[2:])




    def muestraSBoxMIBS(self):
        self.ventanaProceso4=QtWidgets.QMainWindow()
        self.ui4=Ui_SBoxMIBS()
        self.ui4.setupUi(self.ventanaProceso4)
        self.ventanaProceso4.show()

    def muestraPBoxMIBS(self):
        self.ventanaProceso5=QtWidgets.QMainWindow()
        self.ui5=Ui_PBoxMIBS()
        self.ui5.setupUi(self.ventanaProceso5)
        self.ventanaProceso5.show()

    def muestraSBoxPRESENT(self):
        self.ventanaProceso6=QtWidgets.QMainWindow()
        self.ui6=Ui_SBoxPRESENT()
        self.ui6.setupUi(self.ventanaProceso6)
        self.ventanaProceso6.show()

    def muestraPBoxPRESENT(self):
        self.ventanaProceso7=QtWidgets.QMainWindow()
        self.ui7=Ui_PBoxPRESENT()
        self.ui7.setupUi(self.ventanaProceso7)
        self.ventanaProceso7.show()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
