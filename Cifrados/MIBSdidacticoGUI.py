import sys
from PyQt5 import uic, QtWidgets, QtCore
from Cifrado_MIBS import *
from segunda import Ui_segunda
from obtencionclavesMIBS import Ui_procesoSubclaves
from MIBS import *
qtCreatorFile = "/home/alberto/Escritorio/MIBSdidáctico.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.botonsiguiente.clicked.connect(self.abrir)
        #Aqui va el botón
        self.botonConvertirBin.clicked.connect(self.convierteBinario)
        self.botontrozear.clicked.connect(self.bloques64)

    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.ui.botonGeneraSubclaves.clicked.connect(self.generaSubclaves)
        self.ui.botonverproceso.clicked.connect(self.abrirProceso)
        self.ui.botonconvertir.clicked.connect(self.transformabinario)
        self.ui.botoncifrarbloques.clicked.connect(self.cifrabloques)
        self.ui.botontextocifrado.clicked.connect(self.cifratexto)

    def abrirProceso(self):
        self.ventanaProceso=QtWidgets.QMainWindow()
        self.ui2=Ui_procesoSubclaves()
        self.ui2.setupUi(self.ventanaProceso)
        self.ventanaProceso.show()   
        """Ronda actual"""

        self.ui2.botonrotar.clicked.connect(self.rotar)
        self.ui2.botonsbox.clicked.connect(self.sust)
        self.ui2.botonxor.clicked.connect(self.xor)
        self.ui2.botonsubclave.clicked.connect(self.subclave)

    def rotar(self):
        state=self.ui2.textoclaveinicial.text()
        self.ui2.textorota.setText(rotationRight(state,15))

    def sust(self):
        state=self.ui2.textorota.text()
        state2=Sbox(state[-64:-60],4)+state[-60:]
        self.ui2.textosbox.setText(state2)

    def xor(self):
        state=self.ui2.textosbox.text()
        ronda=self.ui2.ronda.value()
        rondaCounter=addZeros(bin(ronda),5)
        xor=int(state[-16:-11],2)^int(rondaCounter,2)
        state=state[-64:-16]+addZeros(bin(xor),5)+state[-11:]
        self.ui2.textoxor.setText(state)
    
    def subclave(self):
        res=self.ui2.textEdit.toPlainText()
        ronda=self.ui2.ronda.value()
        state=self.ui2.textoxor.text()
        clave=state[-64:-32]
        self.ui2.textoclave.setText(clave)
        res += "Clave de ronda "+str(ronda-1)+": "+clave+"\n"
        self.ui2.textEdit.setText(res)
        self.ui2.textoclaveinicial.setText(state)
        if(ronda!=32):
            self.statusBar().showMessage('Nueva clave de ronda generada. Volver al paso 1.')
        else:
            self.statusBar().showMessage('Fin del algoritmo. Se han generado 32 claves de ronda de manera satisfactoria')





    






    def convierteBinario(self):
        textoclaro=self.texto.toPlainText()
        bloqueDatos = text_to_bits(textoclaro)
        self.resultado.setText(bloqueDatos)    

    def bloques64(self):
        textoclaro=self.texto.toPlainText()
        bloques=bloqueDatos(textoclaro)
        res=str()
        for k,v in zip(bloques.keys(),bloques.values()):
            res= res + ("Bloque " + str(k) + ": " + str(v) + "\n")
        self.resultado_2.setText(res)
        self.statusBar().showMessage('Luego se necesitarán cifrar 152 bloques de 64 bits.')

    def transformabinario(self):
        claveBinario="0b"+text_to_bits(self.ui.textoclave.text())
        self.ui.textoclave.setText(claveBinario)
        self.statusBar().showMessage('Clave transformada a binario')


    def generaSubclaves(self):
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        claves=generaterondaKeys(claveBinario)
        res=""
        for clave in claves:
            res = res + "Clave para ronda "+str(claves.index(clave)+1)+": "+str(clave+"\n")

        self.ui.texto.setText(res)
        self.statusBar().showMessage('Se han generado 32 claves de ronda de manera satisfactoria')


    def cifrabloques(self):
        claveBinario="0b0110001101101001011001100111001001001101010010010100001001010011"
        textoclaro=self.texto.toPlainText()
        datos=bloqueDatos(textoclaro)
        bloques=""
        for i in datos:
            cifrabloque=MIBS(64,claveBinario,datos[i])
            bloques= bloques + "Bloque "+str(i)+": "+cifrabloque+"\n"
        resultado=bloques
        self.ui.texto_2.setText(resultado)
        self.statusBar().showMessage('152 bloques cifrados de manera satisfactoria')

    
    def cifratexto(self):
        clave="cifrMIBS"
        resultado=cifrado(64,clave,self.texto.toPlainText())
        self.ui.texto_3.setText(resultado)
        self.statusBar().showMessage('Texto cifrado correctamente.')



    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())