from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import parametros as p

class VentanaPostRonda(QMainWindow):

    senal_comenzar_otra_ronda = pyqtSignal()
    senal_abrir_ventana_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mostrar_ventana(self, resultados):
        if resultados['ganador']:
            uic.loadUi(p.RUTA_VENTANA_POSTRONDA_GANADOR, self) 
            self.boton_siguiente.clicked.connect(self.avanzar_ronda)
        elif not resultados['ganador']:
            uic.loadUi(p.RUTA_VENTANA_POSTRONDA_PERDEDOR, self) 
        self.show()
        self.setear_resultados(resultados)
        if resultados['ganador'] and int(self.n_ronda.text()) < 15:
            self.boton_siguiente.clicked.connect(self.avanzar_ronda)
        self.boton_salir.clicked.connect(self.salir)

    def setear_resultados(self, resultados):
        self.setear_label(self.n_ronda, resultados['ronda'])
        self.setear_label(self.n_soles, resultados['soles'])
        self.setear_label(self.n_zombies, resultados['zombies'])
        self.setear_label(self.ptje_ronda, resultados['puntaje ronda'])
        self.setear_label(self.ptje_total, resultados['puntaje total'])

    def setear_label(self, label, texto):
        label.setText(texto)
        label.repaint()

    def avanzar_ronda(self):
        self.senal_comenzar_otra_ronda.emit()
        self.hide()

    def salir(self):
        self.senal_abrir_ventana_inicio.emit()
        self.close()
