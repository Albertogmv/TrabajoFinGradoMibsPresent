import sys
from PyQt5 import uic, QtWidgets, QtCore
from Cifrado_MIBS import *
from Descifrado_MIBS import descifrado
from MIBS import *
from obtencionclavesMIBS import Ui_procesoSubclaves



qtCreatorFile = "/home/alberto/Escritorio/principaltab.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Cifrado/descifrado MIBS
        self.botoncifra.clicked.connect(self.cifradoMibs)
        self.botondescifra.clicked.connect(self.descifradoMibs)
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
        #Paso 6:Anidamos todos los bloques cifrados
        self.botontextocifrado.clicked.connect(self.cifratexto)



    
    #Cifrado/descifrado MIBS
    def cifradoMibs(self):
        textoclaro=self.textoc.toPlainText()
        if(self.boton_64.isChecked()):
            tamañoClave=64
        elif(self.boton_80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave_2.text()
        res=cifrado(tamañoClave,textoclave,textoclaro)
        self.textoresultado_2.setText(res)

    def descifradoMibs(self):
        textocifrado=self.textoc.toPlainText()
        if(self.boton_64.isChecked()):
            tamañoClave=64
        elif(self.boton_80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave_2.text()
        res=descifrado(tamañoClave,textoclave,textocifrado)
        self.textoresultado_2.setText(res)

    #MIBS didáctico
    #Paso 1:
    def convierteBinario(self):
        textoclaro=self.textoclarodidactico.toPlainText()
        bloqueDatos = text_to_bits(textoclaro)
        self.textobinario.setText(bloqueDatos)    
   
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
        #Paso 3:
        self.ui.botonxor.clicked.connect(self.xor)
        #Paso 4:
        self.ui.botonsubclave.clicked.connect(self.subclave)   

    def rotar(self):
        state=self.ui.textoclaveinicial.text()
        self.ui.textorota.setText(rotationRight(state,15))
        self.ui.statusbar.showMessage('state (registro estado) rotado 15 bits a la derecha')


    def sust(self):
        state=self.ui.textorota.text()
        state2=Sbox(state[-64:-60],4)+state[-60:]
        self.ui.textosbox.setText(state2)
        self.ui.statusbar.showMessage('4 bits más a la izquierda actualizados correctamente')


    def xor(self):
        state=self.ui.textosbox.text()
        ronda=self.ui.ronda.value()
        rondaCounter=addZeros(bin(ronda),5)
        xor=int(state[-16:-11],2)^int(rondaCounter,2)
        state=state[-64:-16]+addZeros(bin(xor),5)+state[-11:]
        self.ui.textoxor.setText(state)
        self.ui.statusbar.showMessage('Operación xor realizada correctamente.State actualizado.')

    
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
        


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())