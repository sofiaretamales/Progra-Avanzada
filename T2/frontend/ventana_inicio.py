import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from os.path import join

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()

        '''Geometría ventana'''
        self.setGeometry(600, 200, 400, 400)
        self.setWindowTitle('Ventana de inicio')
        foto_fondo = QImage(join('sprites', 'fondos', 'fondoMenu.png'))
        fondo = QPalette()
        fondo.setBrush(QPalette.Window, QBrush(foto_fondo))
        self.setPalette(fondo)
        self.crear_elementos()
    
    def crear_elementos(self):

        '''Logo'''
        self.logo = QLabel(self)
        self.logo.setGeometry(50, 50, 300, 300)
        ruta = join('sprites', 'Elementos de juego', 'logo.png')
        pixeles = QPixmap(ruta)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(300, 300)

        '''Pedir el usuario'''
        self.usuario = QLineEdit('', self)
        self.usuario.setPlaceholderText("Ingrese su nombre de usuario")
        self.usuario.setStyleSheet("background-color:#DEF0D0;")

        '''Botones'''
        self.boton_jugar = QPushButton("Jugar", self)
        self.boton_jugar.setStyleSheet("background-color:#9EF04B;")
        self.boton_ranking = QPushButton("Ver ranking", self)
        self.boton_ranking.setStyleSheet("background-color:#9EF04B;")
        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.setStyleSheet("background-color:#9EF04B;")

        '''Layouts'''
        layout_logo = QHBoxLayout()
        layout_logo.addWidget(self.logo)
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_logo)
        layout_principal.addWidget(self.usuario)
        layout_principal.addWidget(self.boton_jugar)
        layout_principal.addWidget(self.boton_ranking)
        layout_principal.addWidget(self.boton_salir)
        self.setLayout(layout_principal)

        '''Conexiones'''
        self.boton_jugar.clicked.connect(self.enviar_login)
        self.boton_ranking.clicked.connect(self.ver_ranking)
        self.boton_salir.clicked.connect(self.salir)


    def enviar_login(self):
        self.senal_enviar_login.emit(self.usuario.text())

    def recibir_validacion(self, valido):
        if valido:
            self.ocultar()
        else:
            mensaje = QMessageBox.about(self, 'Error', 'Usuario inválido!')
            self.usuario.setText("")
            self.usuario.setPlaceholderText("Ingrese su nombre de usuario")

    def ver_ranking(self):
        self.senal_ver_ranking.emit()
        self.ocultar()

    def salir(self):
        sys.exit()

    def mostrar(self):
        self.show()
        self.usuario.setText("")
        self.usuario.setPlaceholderText("Ingrese su nombre de usuario")

    def ocultar(self):
        self.hide()
