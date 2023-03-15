from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        # COMPLETAR
        set_errores = set()
        if usuario.isalnum() and contrasena not in p.CONTRASENAS_PROHIBIDAS:
            self.senal_abrir_juego.emit(usuario)
            self.senal_respuesta_validacion.emit(True, set_errores)
        else:
            if not usuario.isalnum:
                set_errores.add(usuario)
            elif contrasena in p.CONTRASENAS_PROHIBIDAS:
                set_errores.add(contrasena)
            self.senal_respuesta_validacion.emit(False)
        