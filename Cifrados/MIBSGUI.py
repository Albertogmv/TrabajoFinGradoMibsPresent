import sys
from PyQt5 import uic, QtWidgets, QtCore

from Cifrado_MIBS import cifrado
from Descifrado_MIBS import descifrado

qtCreatorFile = "/home/alberto/Escritorio/MIBS.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Aqui va el botón
        self.botoncifrar.clicked.connect(self.cifradoMibs)
        self.botondescifrar.clicked.connect(self.descifradoMibs)

    
    #calculos
    def cifradoMibs(self):
        textoclaro=self.texto.toPlainText()
        if(self.boton64.isChecked()):
            tamañoClave=64
        elif(self.boton80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave.text()
        res=cifrado(tamañoClave,textoclave,textoclaro)
        self.textoresultado.setText(res)

    def descifradoMibs(self):
        textocifrado=self.texto.toPlainText()
        if(self.boton64.isChecked()):
            tamañoClave=64
        elif(self.boton80.isChecked()):
            tamañoClave=80
        textoclave=self.textoclave.text()
        res=descifrado(tamañoClave,textoclave,textocifrado)
        self.textoresultado.setText(res)

    
        
        
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())