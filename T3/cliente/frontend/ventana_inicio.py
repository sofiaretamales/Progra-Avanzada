from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from os.path import join
from funciones_utiles import data_json
import sys

window_name, base_class = uic.loadUiType(join(*data_json(
                                                        "RUTA_VENTANA_INICIO")))

class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.boton_puerta.setStyleSheet("QPushButton"
                                        "{"
                                        "background : transparent;"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        "border-image: url(sprites/background/door.png)"
                                        "}")
        self.boton_puerta.clicked.connect(self.enviar_login)

    def enviar_login(self):
        nombre = self.label_usuario.text()
        diccionario = {'comando': 'validar nombre', 
                        'nombre': nombre}
        self.senal_enviar_login.emit(diccionario)
        self.label_usuario.setText("")
        
    def mostrar_error_usuario_invalido(self):
        QMessageBox.about(self, 'Error', 'Usuario inválido!')
        self.label_usuario.setText("")

    def mostrar_error_sala_llena(self):
        mensaje = 'Lo siento, la sala de espera está llena:('
        QMessageBox.about(self, 'Error', mensaje)

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.mostrar()
    sys.exit(app.exec())