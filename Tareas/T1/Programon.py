from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VELOCIDAD_AGUA \
                        , AUMENTAR_VIDA_PLANTA, MAX_AUMENTO_ENTRENAMIENTO \
                        , MIN_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA \
                        , MAX_AUMENTO_EXPERIENCIA

class Programon(ABC):

    def __init__(self, nombre, tipo, nivel, vida, ataque \
                , defensa, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__velocidad = velocidad
        self.__experiencia = 0

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, val):
        if val > 255:
            self.__vida = 255
        elif val < 1:
            self.__vida = 1
        else: 
            self.__vida = val

    @property
    def ataque(self):
        return  self.__ataque

    @ataque.setter
    def ataque(self, val):
        if val > 190:
            self.__ataque = 190
        elif val < 5:
            self.__ataque = 5
        else: 
            self.__ataque = val

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, val):
        if val > 250:
            self.__defensa = 250
        elif val < 5:
            self.__defensa = 5
        else: 
            self.__defensa = val

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, val):
        if val > 200:
            self.__velocidad = 100
        elif val < 0:
            self.__velocidad = 0
        else: 
            self.__velocidad = val

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, val):
        if val > 100:
            self.__experiencia = val - 100 
        elif val < 0:
            self.__experiencia = 0
        else: 
            self.__experiencia = val

    def entrenar(self, nombre):
        sum_exp = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        if self.experiencia + sum_exp >= 100:
            self.experiencia += sum_exp
            self.nivel += 1
            aumento_vida = randint(MIN_AUMENTO_ENTRENAMIENTO \
                                   , MAX_AUMENTO_ENTRENAMIENTO)
            aumento_ataque = randint(MIN_AUMENTO_ENTRENAMIENTO \
                                    , MAX_AUMENTO_ENTRENAMIENTO)
            aumento_defensa = randint(MIN_AUMENTO_ENTRENAMIENTO \
                                     , MAX_AUMENTO_ENTRENAMIENTO) 
            aumento_velocidad = randint(MIN_AUMENTO_ENTRENAMIENTO \
                                        , MAX_AUMENTO_ENTRENAMIENTO)
            self.vida += aumento_vida
            self.ataque += aumento_ataque
            self.defensa += aumento_defensa
            self.velocidad += aumento_velocidad
            print(f"La experiencia de {nombre} ha aumentado en {sum_exp}\n"
                  f"Su experiencia anterior era {100 + self.experiencia - sum_exp}"
                  f" y subió al nivel {self.nivel}\n"
                  f"Su nueva experiencia es es {self.experiencia}")
        else:
            self.experiencia += sum_exp
            print(f"La experiencia de {nombre} ha aumentado en {sum_exp}\n"
                  f"Su experiencia anterior era {self.experiencia - sum_exp}"
                  f" y ahora es {self.experiencia}")
    
    @abstractmethod
    def luchar(self, rival):
        pass

    @abstractmethod
    def ganar_batalla(self):
        pass


class Planta(Programon):

    def __init__(self, nombre, tipo, nivel, vida, ataque \
                , defensa, velocidad):
        super().__init__(nombre, tipo, nivel, vida, ataque \
                        , defensa, velocidad)
        self.ventaja = None

    def ventaja_de_tipo(self, tipo_rival):
        if tipo_rival == 'planta':
            self.ventaja = 0
        elif tipo_rival == 'fuego':
            self.ventaja = -1
        elif tipo_rival == 'agua':
            self.ventaja = 1

    def luchar(self, tipo_rival):
        self.ventaja_de_tipo(tipo_rival)
        puntaje = (self.vida*0.2 + self.nivel*0.3 + self.ataque*0.15 
                   + self.defensa*0.15 + self.velocidad*0.2 
                   + self.ventaja*40)
        return puntaje

    def ganar_batalla(self):
        self.vida += AUMENTAR_VIDA_PLANTA
        print(f"--- Se aumentó la vida de {self.nombre} ---")
        

class Fuego(Programon):

    def __init__(self, nombre, tipo, nivel, vida, ataque \
                , defensa, velocidad):
        super().__init__(nombre, tipo, nivel, vida, ataque \
                        , defensa, velocidad)
        self.ventaja = None

    def ventaja_de_tipo(self, tipo_rival):
        if tipo_rival == 'planta':
            self.ventaja = 1
        elif tipo_rival == 'fuego':
            self.ventaja = 0
        elif tipo_rival == 'agua':
            self.ventaja = -1

    def luchar(self, tipo_rival):
        self.ventaja_de_tipo(tipo_rival)
        puntaje = (self.vida*0.2 + self.nivel*0.3 + self.ataque*0.15 
                   + self.defensa*0.15 + self.velocidad*0.2 
                   + self.ventaja*40)
        return puntaje

    def ganar_batalla(self):
        self.ataque += AUMENTAR_ATAQUE_FUEGO
        print(f"--- Se aumentó el ataque de {self.nombre} ---")


class Agua(Programon):

    def __init__(self, nombre, tipo, nivel, vida, ataque \
                , defensa, velocidad):
        super().__init__(nombre, tipo, nivel, vida, ataque \
                        , defensa, velocidad)
        self.ventaja = None

    def ventaja_de_tipo(self, tipo_rival):
        if tipo_rival == 'planta':
            self.ventaja = -1
        elif tipo_rival == 'fuego':
            self.ventaja = 1
        elif tipo_rival == 'agua':
            self.ventaja = 0

    def luchar(self, tipo_rival):
        self.ventaja_de_tipo(tipo_rival)
        puntaje = (self.vida*0.2 + self.nivel*0.3 + self.ataque*0.15 
                   + self.defensa*0.15 + self.velocidad*0.2 
                   + self.ventaja*40)
        return puntaje

    def ganar_batalla(self):
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA
        print(f"--- Se aumentó la velocidad de {self.nombre} ---")
