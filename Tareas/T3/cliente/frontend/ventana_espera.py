from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5 import uic
from os.path import join
from funciones_utiles import data_json

window_name, base_class = uic.loadUiType(join(*data_json(
                                                        "RUTA_VENTANA_ESPERA")))

class VentanaEspera(window_name, base_class):

    senal_abrir_sala_inicio = pyqtSignal()
    senal_abrir_sala_juego = pyqtSignal()
    senal_borrar_jugador = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.usuario = '' 
        self.boton_volver.clicked.connect(self.volver_sala_inicio)

    def set_datos(self, datos):
        if len(datos) == 1:
            self.jugador_1.setText(datos[0])
            self.jugador_2.setText("Esperando jugador...")
        elif len(datos) == 2:
            self.jugador_1.setText(datos[0])
            self.jugador_2.setText(datos[1])

    def comenzar_cuenta_regresiva(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.conteo)
        self.timer.setInterval(1000)
        self.tiempo_cuenta = data_json("CUENTA_REGRESIVA_INICIO")
        self.timer.start()

    def conteo(self):
        self.tiempo.setText(str(self.tiempo_cuenta))
        self.tiempo_cuenta -= 1
        if self.tiempo_cuenta < 0:
            self.timer.stop()
            self.senal_abrir_sala_juego.emit()

    def volver_sala_inicio(self):
        self.close()
        self.senal_abrir_sala_inicio.emit()
        diccionario = {"comando": "borrar jugador", 
                        "jugador": self.usuario}
        self.senal_borrar_jugador.emit(diccionario)

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()