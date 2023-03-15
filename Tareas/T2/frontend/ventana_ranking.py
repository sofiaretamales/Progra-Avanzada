from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_RANKING)

class VentanaRanking(window_name, base_class):

    senal_crear_ranking = pyqtSignal()
    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)

    def actualizar_datos(self, datos):
        self.setear_dato(self.numero_1, datos[0][0])
        self.setear_dato(self.puntaje_1, datos[0][1])
        self.setear_dato(self.numero_2, datos[1][0])
        self.setear_dato(self.puntaje_2, datos[1][1])
        self.setear_dato(self.numero_3, datos[2][0])
        self.setear_dato(self.puntaje_3, datos[2][1])
        self.setear_dato(self.numero_4, datos[3][0])
        self.setear_dato(self.puntaje_4, datos[3][1])
        self.setear_dato(self.numero_5, datos[4][0])
        self.setear_dato(self.puntaje_5, datos[4][1])

    def setear_dato(self, label, dato):
        label.setText(dato)
        label.repaint()

    def volver(self):
        self.senal_volver.emit()
        self.hide()

    def mostrar(self):
        self.show()
        self.senal_crear_ranking.emit()