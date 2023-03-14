from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QMessageBox,
                             QHBoxLayout, QPushButton, QRadioButton)
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from os.path import join

class VentanaPrincipal(QWidget):
    
    senal_verificar_eleccion = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        '''Geometría ventana'''
        self.setGeometry(600, 200, 600, 400)
        self.setWindowTitle('Ventana principal')
        foto_fondo = QImage(join('sprites', 'fondos', 'fondoMenu.png'))
        fondo = QPalette()
        fondo.setBrush(QPalette.Window, QBrush(foto_fondo))
        self.setPalette(fondo)
        self.crear_elementos()

    def crear_elementos(self):
        
        '''Indicación'''
        indicacion = QLabel('Elige el ambiente de juego', self)
        indicacion.setAlignment(Qt.AlignCenter)

        '''Jardín de la Abuela'''
        self.foto_jardin = QLabel(self)
        self.foto_jardin.setGeometry(50, 50, 300, 200)
        ruta_jardin = join('sprites', 'fondos', 'jardinAbuela.png')
        pixeles_jardin = QPixmap(ruta_jardin)
        self.foto_jardin.setPixmap(pixeles_jardin)
        self.foto_jardin.setScaledContents(True)
        self.foto_jardin.setMaximumSize(300, 200)
        self.boton_jardin = QRadioButton('Jardín de la abuela', self)
        layout_jardin = QVBoxLayout()
        layout_jardin.addWidget(self.foto_jardin)
        layout_jardin.addWidget(self.boton_jardin)

        '''Salida Nocturna'''
        self.foto_nocturna = QLabel(self)
        self.foto_nocturna.setGeometry(20, 20, 300, 200)
        ruta_nocturna = join('sprites', 'fondos', 'salidaNocturna.png')
        pixeles_nocturna = QPixmap(ruta_nocturna)
        self.foto_nocturna.setPixmap(pixeles_nocturna)
        self.foto_nocturna.setScaledContents(True)
        self.foto_nocturna.setMaximumSize(300, 200)
        self.boton_nocturna = QRadioButton('Salida nocturna', self)
        layout_nocturna = QVBoxLayout()
        layout_nocturna.addWidget(self.foto_nocturna)
        layout_nocturna.addWidget(self.boton_nocturna)

        '''Botón iniciar'''
        self.boton_iniciar = QPushButton("Iniciar", self)
        self.boton_iniciar.setStyleSheet("background-color:#9EF04B;")

        '''Layouts'''
        layout_ambientes = QHBoxLayout()
        layout_ambientes.addStretch(1)
        layout_ambientes.addLayout(layout_jardin)
        layout_ambientes.addLayout(layout_nocturna)
        layout_ambientes.addStretch(1)
        layout_principal = QVBoxLayout()
        layout_principal.addStretch(1)
        layout_principal.addWidget(indicacion)
        layout_principal.addLayout(layout_ambientes)
        layout_principal.addWidget(self.boton_iniciar)
        layout_principal.addStretch(1)
        self.setLayout(layout_principal)

        '''Conexión'''
        self.boton_iniciar.clicked.connect(self.verificar_eleccion)

    def verificar_eleccion(self):
        tupla_check = (self.boton_jardin.isChecked(), self.boton_nocturna.isChecked())
        self.senal_verificar_eleccion.emit(tupla_check)

    def recibir_verificacion(self, valido):
        if valido:
            self.ocultar()
        else:
            mensaje = QMessageBox.about(self, 'Error', 'Ningún ambiente fue seleccionado')

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

