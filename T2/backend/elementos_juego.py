from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import parametros as p
from abc import ABC

class MetaClass(type(ABC), type(QObject)):
    pass

class Plantas(ABC, QObject, metaclass=MetaClass):

    def __init__(self, vida_inicial, pos):
        super().__init__()
        self.__vida = vida_inicial
        self.pos = pos
        self.x = pos.x()
        self.y = pos.y()
        self.frame = 1
        self.intervalo_disparo = p.INTERVALO_DISPARO

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.__vida = 0
        else:
            self.__vida = valor

class PlantaClasica(Plantas):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.costo = p.COSTO_LANZAGUISANTE
        self.guisantes = []
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_LANZAGUISANTES_1)
        self.pixmap_2 = QPixmap(p.RUTA_LANZAGUISANTES_2)
        self.pixmap_3 = QPixmap(p.RUTA_LANZAGUISANTES_3)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PLANTA, p.ALTO_PLANTA)
        self.label.move(self.x, self.y)


class PlantaAzul(Plantas):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.costo = p.COSTO_LANZAGUISANTE_HIELO
        self.ralentizar_zombie = p.RALENTIZAR_ZOMBIE
        self.guisantes = []
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_LANZAGUISANTESHIELO_1)
        self.pixmap_2 = QPixmap(p.RUTA_LANZAGUISANTESHIELO_2)
        self.pixmap_3 = QPixmap(p.RUTA_LANZAGUISANTESHIELO_3)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PLANTA, p.ALTO_PLANTA)
        self.label.move(self.x, self.y)

class Girasol(Plantas):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.costo = p.COSTO_GIRASOL
        self.intervalo_soles = p.INTERVALO_SOLES_GIRASOL
        self.genera_soles = p.CANTIDAD_SOLES
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_GIRASOL_1)
        self.pixmap_2 = QPixmap(p.RUTA_GIRASOL_2)
        self.pixmap_3 = QPixmap(p.RUTA_GIRASOL_1)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PLANTA, p.ALTO_PLANTA)
        self.label.move(self.x, self.y)

class PlantaPatata(Plantas):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.costo = p.COSTO_PAPA
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_PAPA_1)
        self.pixmap_2 = QPixmap(p.RUTA_PAPA_2)
        self.pixmap_3 = QPixmap(p.RUTA_PAPA_3)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PLANTA, p.ALTO_PLANTA)
        self.label.move(self.x, self.y)

class Zombies(ABC, QObject, metaclass=MetaClass):
    
    def __init__(self, velocidad, pos):
        super().__init__()
        self.__vida = p.VIDA_ZOMBIE
        self.velocidad_inicial = velocidad
        self.velocidad = velocidad
        self.frame_caminando = 1
        self.__frame_comiendo = 0
        self.__x = pos.x()
        self.y = pos.y()

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.__vida = 0 
        else:
            self.__vida = valor

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if p.POS_CASA_X <= valor < p.ANCHO_VENTANA:
            self.__x = int(valor)

    @property
    def frame_comiendo(self):
        return self.__frame_comiendo

    @frame_comiendo.setter
    def frame_comiendo(self, valor):
        if valor >= 2:
            self.__frame_comiendo = 2
        else:
            self.__frame_comiendo = valor

class ZombieClasico(Zombies):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = QLabel('')
        self.pixmap_caminando_1 = QPixmap(p.RUTA_ZOMBIE_CLASICO_CAMINANDO_1)
        self.pixmap_caminando_2 = QPixmap(p.RUTA_ZOMBIE_CLASICO_CAMINANDO_2)
        self.pixmap_comiendo_1 = QPixmap(p.RUTA_ZOMBIE_CLASICO_COMIENDO_1)
        self.pixmap_comiendo_2 = QPixmap(p.RUTA_ZOMBIE_CLASICO_COMIENDO_2)
        self.pixmap_comiendo_3 = QPixmap(p.RUTA_ZOMBIE_CLASICO_COMIENDO_3)
        self.label.setPixmap(self.pixmap_comiendo_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_ZOMBIE, p.ALTO_ZOMBIE)
        self.label.move(self.x, self.y)

class ZombieRapido(Zombies):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = QLabel('')
        self.pixmap_caminando_1 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_CAMINANDO_1)
        self.pixmap_caminando_2 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_CAMINANDO_2)
        self.pixmap_comiendo_1 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_1)
        self.pixmap_comiendo_2 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_2)
        self.pixmap_comiendo_3 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_3)
        self.label.setPixmap(self.pixmap_comiendo_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_ZOMBIE, p.ALTO_ZOMBIE)
        self.label.move(self.x, self.y)

class Guisantes(ABC, QObject, metaclass=MetaClass):

    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.__x = pos.x()
        self.y = pos.y()
        self.velocidad = p.VELOCIDAD_PROYECTIL
        self.dano = p.DANO_PROYECTIL
        self.frame = 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if  valor < p.ANCHO_VENTANA:
            self.__x = int(valor)
            
class GuisanteClasico(Guisantes):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_GUISANTE_1)
        self.pixmap_2 = QPixmap(p.RUTA_GUISANTE_2)
        self.pixmap_3 = QPixmap(p.RUTA_GUISANTE_3)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PROYECTIL, p.ALTO_PROYECTIL)
        self.label.move(self.x, self.y)

class GuisanteHielo(Guisantes):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = QLabel('')
        self.pixmap_1 = QPixmap(p.RUTA_GUISANTEHIELO_1)
        self.pixmap_2 = QPixmap(p.RUTA_GUISANTEHIELO_2)
        self.pixmap_3 = QPixmap(p.RUTA_GUISANTEHIELO_3)
        self.label.setPixmap(self.pixmap_1)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_PROYECTIL, p.ALTO_PROYECTIL)
        self.label.move(self.x, self.y)

class Soles(QObject):

    def __init__(self, pos):
        self.x = pos.x()
        self.y = pos.y()
        self.label = QLabel('')
        self.pixmap = QPixmap(p.RUTA_SOL)
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(p.ANCHO_SOL, p.ALTO_SOL)
        self.label.move(self.x, self.y)
