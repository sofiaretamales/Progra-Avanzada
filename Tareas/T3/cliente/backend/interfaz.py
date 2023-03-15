from PyQt5.QtCore import pyqtSignal, QObject
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego

class Interfaz(QObject):

    senal_abrir_ventana_espera = pyqtSignal()
    senal_login_rechazado = pyqtSignal()
    senal_sala_espera_llena = pyqtSignal()
    senal_actualizar_usuarios_sala_espera = pyqtSignal(list)
    senal_comenzar_cuenta_regresiva = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.mostrar()

    def manejar_mensaje(self, mensaje: dict):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "resp_verificar_nombre":
            if mensaje["estado"] == "aceptado":
                self.mostrar_ventana_espera(mensaje["usuarios"], mensaje["nombre"])
            elif mensaje["estado"] == "rechazado":
                self.senal_login_rechazado.emit()
            elif mensaje["estado"] == "lleno":
                self.senal_sala_espera_llena.emit()
        elif comando == "respuesta_actualizar_usuarios":
            self.senal_actualizar_usuarios_sala_espera.emit(
                mensaje["usuarios"])
            if len(mensaje["usuarios"]) == 2:
                self.senal_comenzar_cuenta_regresiva.emit()
            
    def mostrar_ventana_espera(self, datos, nombre):
        self.ventana_inicio.ocultar()
        self.ventana_espera.mostrar()
        self.ventana_espera.usuario = nombre
        self.ventana_espera.set_datos(datos)

    def mostrar_ventana_juego(self):
        self.ventana_espera.ocultar()
        self.ventana_juego.mostrar()
