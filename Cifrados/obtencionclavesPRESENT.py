# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obtencionclavesPRESENT.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_procesoSubclavesPresent(object):
    def setupUi(self, procesoSubclavesPresent):
        procesoSubclavesPresent.setObjectName("procesoSubclavesPresent")
        procesoSubclavesPresent.resize(947, 786)
        procesoSubclavesPresent.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(procesoSubclavesPresent)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.rondaPRES = QtWidgets.QSpinBox(self.centralwidget)
        self.rondaPRES.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rondaPRES.setInputMethodHints(QtCore.Qt.ImhNone)
        self.rondaPRES.setReadOnly(True)
        self.rondaPRES.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.rondaPRES.setMinimum(0)
        self.rondaPRES.setMaximum(32)
        self.rondaPRES.setSingleStep(1)
        self.rondaPRES.setProperty("value", 0)
        self.rondaPRES.setObjectName("rondaPRES")
        self.horizontalLayout_3.addWidget(self.rondaPRES)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.botonsubclavePRES = QtWidgets.QPushButton(self.centralwidget)
        self.botonsubclavePRES.setEnabled(True)
        self.botonsubclavePRES.setObjectName("botonsubclavePRES")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.botonsubclavePRES)
        self.botonrotar = QtWidgets.QPushButton(self.centralwidget)
        self.botonrotar.setEnabled(False)
        self.botonrotar.setObjectName("botonrotar")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.botonrotar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botonsbox = QtWidgets.QPushButton(self.centralwidget)
        self.botonsbox.setEnabled(False)
        self.botonsbox.setObjectName("botonsbox")
        self.horizontalLayout_2.addWidget(self.botonsbox)
        self.botonverSBoxPRES2 = QtWidgets.QPushButton(self.centralwidget)
        self.botonverSBoxPRES2.setObjectName("botonverSBoxPRES2")
        self.horizontalLayout_2.addWidget(self.botonverSBoxPRES2)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.botonxor = QtWidgets.QPushButton(self.centralwidget)
        self.botonxor.setEnabled(False)
        self.botonxor.setObjectName("botonxor")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.botonxor)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textoclavePRES = QtWidgets.QLineEdit(self.centralwidget)
        self.textoclavePRES.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textoclavePRES.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textoclavePRES.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.textoclavePRES.setReadOnly(True)
        self.textoclavePRES.setObjectName("textoclavePRES")
        self.horizontalLayout.addWidget(self.textoclavePRES)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.textoclavePRES_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textoclavePRES_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textoclavePRES_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textoclavePRES_2.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.textoclavePRES_2.setText("")
        self.textoclavePRES_2.setReadOnly(True)
        self.textoclavePRES_2.setObjectName("textoclavePRES_2")
        self.horizontalLayout_10.addWidget(self.textoclavePRES_2)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_10)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.formLayout_5)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setSpacing(0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.textEditPRES = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPRES.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEditPRES.setObjectName("textEditPRES")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textEditPRES)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.formLayout_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.formLayout_2.setSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.textorotaPRES = QtWidgets.QLineEdit(self.centralwidget)
        self.textorotaPRES.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textorotaPRES.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textorotaPRES.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.textorotaPRES.setText("")
        self.textorotaPRES.setReadOnly(True)
        self.textorotaPRES.setObjectName("textorotaPRES")
        self.horizontalLayout_6.addWidget(self.textorotaPRES)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_6)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.SpanningRole, self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 6, 0, -1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.textosboxPRES = QtWidgets.QLineEdit(self.centralwidget)
        self.textosboxPRES.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textosboxPRES.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textosboxPRES.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.textosboxPRES.setText("")
        self.textosboxPRES.setReadOnly(True)
        self.textosboxPRES.setObjectName("textosboxPRES")
        self.horizontalLayout_8.addWidget(self.textosboxPRES)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_8)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.SpanningRole, self.formLayout_3)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.formLayout_4.setSpacing(0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.textoxorPRES = QtWidgets.QLineEdit(self.centralwidget)
        self.textoxorPRES.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textoxorPRES.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textoxorPRES.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.textoxorPRES.setText("")
        self.textoxorPRES.setReadOnly(True)
        self.textoxorPRES.setObjectName("textoxorPRES")
        self.horizontalLayout_9.addWidget(self.textoxorPRES)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_9)
        self.formLayout.setLayout(11, QtWidgets.QFormLayout.SpanningRole, self.formLayout_4)
        self.label_3.raise_()
        self.label.raise_()
        self.botonrotar.raise_()
        self.botonxor.raise_()
        self.botonsubclavePRES.raise_()
        procesoSubclavesPresent.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(procesoSubclavesPresent)
        self.statusbar.setObjectName("statusbar")
        procesoSubclavesPresent.setStatusBar(self.statusbar)

        self.retranslateUi(procesoSubclavesPresent)
        self.botonsubclavePRES.clicked['bool'].connect(self.rondaPRES.stepUp)
        QtCore.QMetaObject.connectSlotsByName(procesoSubclavesPresent)

    def retranslateUi(self, procesoSubclavesPresent):
        _translate = QtCore.QCoreApplication.translate
        procesoSubclavesPresent.setWindowTitle(_translate("procesoSubclavesPresent", "Algoritmo de obtención de claves PRESENT"))
        self.label_3.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p><span style=\" font-weight:600;\">Algoritmo de generación de claves</span></p></body></html>"))
        self.label_5.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p><span style=\" font-weight:600;\">Ronda </span></p></body></html>"))
        self.rondaPRES.setToolTip(_translate("procesoSubclavesPresent", "Contador de ronda"))
        self.label.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Nota</span>: El estado inicial equivale a la clave (en binario) introducida por el usuario.</p></body></html>"))
        self.botonsubclavePRES.setText(_translate("procesoSubclavesPresent", "obtener subclave"))
        self.botonrotar.setText(_translate("procesoSubclavesPresent", "Rotar"))
        self.botonsbox.setText(_translate("procesoSubclavesPresent", "SBox"))
        self.botonverSBoxPRES2.setText(_translate("procesoSubclavesPresent", "Ver SBox"))
        self.botonxor.setText(_translate("procesoSubclavesPresent", "XOR"))
        self.label_2.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>state<span style=\" vertical-align:super;\">i: </span></p></body></html>"))
        self.textoclavePRES.setToolTip(_translate("procesoSubclavesPresent", "estado (80 bits)"))
        self.textoclavePRES.setText(_translate("procesoSubclavesPresent", "01100011011010010110011001010000010100100100010101010011010001010100111001010100"))
        self.label_16.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>1. La clave de ronda serán los 64 bits más a la izquierda del state<span style=\" vertical-align:super;\">i </span><br/></p></body></html>"))
        self.label_15.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>clave<span style=\" vertical-align:super;\">i</span>:<span style=\" vertical-align:super;\"/></p></body></html>"))
        self.textoclavePRES_2.setToolTip(_translate("procesoSubclavesPresent", "Clave (64 bits)"))
        self.textoclavePRES_2.setWhatsThis(_translate("procesoSubclavesPresent", "<html><head/><body><p><br/></p></body></html>"))
        self.label_17.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p><span style=\" font-weight:600;\">Claves de ronda:</span></p></body></html>"))
        self.label_9.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>2. state<span style=\" vertical-align:super;\">i </span>se rota 61 bits a la izquierda.<br/></p></body></html>"))
        self.label_8.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>state<span style=\" vertical-align:super;\">i</span>:<span style=\" vertical-align:super;\"/></p></body></html>"))
        self.label_11.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>state<span style=\" vertical-align:super;\">i</span>:<span style=\" vertical-align:super;\"/></p></body></html>"))
        self.label_12.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>3. Los 4 bits más a la izquierda de state<span style=\" vertical-align:super;\">i </span>se transforman a través de la SBox. </p></body></html>"))
        self.label_14.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>4. Se realiza una operación XOR entre los bits de state<span style=\" vertical-align:super;\">i </span>, situados entre la posición 19 a la 15, y el contador de ronda. El resto no varía.<br/></p></body></html>"))
        self.label_13.setText(_translate("procesoSubclavesPresent", "<html><head/><body><p>state<span style=\" vertical-align:super;\">i</span>:<span style=\" vertical-align:super;\"/></p></body></html>"))

