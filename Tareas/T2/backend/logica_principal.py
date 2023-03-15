from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaPrincipal(QObject):

    senal_devolver_verificacion = pyqtSignal(bool)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_seleccion(self, tupla_boton_check):
        if tupla_boton_check[0] or tupla_boton_check[1]:
            self.senal_devolver_verificacion.emit(True)
            if tupla_boton_check[0]:
                self.senal_abrir_juego.emit('abuela')
            elif tupla_boton_check[1]:
                self.senal_abrir_juego.emit('nocturno')
        else:
            self.senal_devolver_verificacion.emit(False)

