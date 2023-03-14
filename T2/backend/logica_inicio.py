from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_ventana_principal = pyqtSignal()
    senal_enviar_usuario_a_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario):
        es_alnum = usuario.isalnum()
        esta_en_rango = len(usuario) in range(p.MIN_CARACTERES, p.MAX_CARACTERES)
        no_es_vacio = usuario != ''
        if es_alnum and esta_en_rango and no_es_vacio:
            self.senal_abrir_ventana_principal.emit()
            self.senal_respuesta_validacion.emit(True)
            self.senal_enviar_usuario_a_juego.emit(usuario)
        else:
            self.senal_respuesta_validacion.emit(False)

