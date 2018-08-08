import sys
from PyQt5 import uic, QtWidgets, QtCore

from Cifrado_PRESENT import cifrado
from Descifrado_PRESENT import descifrado

qtCreatorFile = "/home/alberto/Escritorio/PRESENT.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Aqui va el botón
        self.botoncifrar.clicked.connect(self.cifradoPresent)
        self.botondescifrar.clicked.connect(self.descifradoPresent)

    
    #calculos
    def cifradoPresent(self):
        textoclaro=self.texto.toPlainText()
        if(self.boton80.isChecked()):
            tamañoClave=80
        elif(self.boton128.isChecked()):
            tamañoClave=128
        textoclave=self.textoclave.text()
        res=cifrado(tamañoClave,textoclave,textoclaro)
        self.textoresultado.setText(res)

    def descifradoPresent(self):
        textocifrado=self.texto.toPlainText()
        if(self.boton80.isChecked()):
            tamañoClave=80
        elif(self.boton128.isChecked()):
            tamañoClave=128
        textoclave=self.textoclave.text()
        res=descifrado(tamañoClave,textoclave,textocifrado)
        self.textoresultado.setText(res)

    
        
        
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())