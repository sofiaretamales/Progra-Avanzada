from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

import parametros as p

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # COMPLETAR
        '''logo'''
        self.logo = QLabel(self)
        self.logo.setGeometry(50, 50, 300, 300)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(400, 400)
        '''Pedir el usuario'''
        pedir_usuario = QLabel("Ingrese su nombre de usuario:", self)
        self.usuario = QLineEdit('')
        '''Pedir la contraseña'''
        pedir_contrasena = QLabel("Ingrese su contraseña:")
        self.clave = QLineEdit('')
        self.clave.setEchoMode(QLineEdit.Password)
        '''boton'''
        self.boton_ingresar = QPushButton("Ingresar", self)
        '''layouts'''
        layout_usuario = QHBoxLayout()
        layout_usuario.addWidget(pedir_usuario)
        layout_usuario.addWidget(self.usuario)
        layout_clave = QHBoxLayout()
        layout_clave.addWidget(pedir_contrasena)
        layout_clave.addWidget(self.clave)
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.logo)
        layout_principal.addLayout(layout_usuario)
        layout_principal.addLayout(layout_clave)
        layout_principal.addWidget(self.boton_ingresar)
        self.setLayout(layout_principal)

        self.boton_ingresar.clicked.connect(self.enviar_login)

    def enviar_login(self):
        # COMPLETAR
        self.senal_enviar_login.emit(self.usuario.text(), self.clave.text())

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        else:
            if "usuario" in errores:
                self.clave.setText("")
                self.clave.setPlaceholderText("Usuario inválido!")
            if "contraseña" in errores:
                self.clave.setText("")
                self.clave.setPlaceholderText("Contraseña inválida!")