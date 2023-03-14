from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaRanking(QObject):

    senal_enviar_datos = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def ordenar_ranking(self, tupla):
        '''se utiliza como key en método crear_ranking()'''
        return int(tupla[1])

    def crear_ranking(self):
        lista_puntajes = []
        with open(p.RUTA_PUNTAJES, 'r', encoding='utf-8') as puntajes:
            for puntaje in puntajes:
                nombre_puntaje = puntaje.strip().split(',')
                nombre = nombre_puntaje[0]
                puntaje = nombre_puntaje[1]
                lista_puntajes.append((nombre, puntaje))
    
        lista_puntajes.sort(key=self.ordenar_ranking, reverse=True)
        lista_top_5 = lista_puntajes[:5]
        self.senal_enviar_datos.emit(lista_top_5)
                
