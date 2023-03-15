from PyQt5 import uic
from os.path import join
from funciones_utiles import data_json

window_name, base_class = uic.loadUiType(join(*data_json(
                                                        "RUTA_VENTANA_JUEGO")))

class VentanaJuego(window_name, base_class):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        #self.boton_volver.clicked.connect(self.volver_sala_principal)

    def mostrar(self):
        self.show()