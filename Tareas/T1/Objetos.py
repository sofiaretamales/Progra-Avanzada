from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTO_DEFENSA

class Objetos(ABC):

    def __init__(self, nombre, tipo, costo, prob_exito):
        self.nombre = nombre
        self.tipo = tipo
        self.costo = costo
        self.prob_exito = prob_exito

    @abstractmethod
    def aplicar_objeto(self, programon):
        pass

class Baya(Objetos):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento_vida = randint(1, 10)
        print(f"Aumento de vida: {aumento_vida}")
        programon.vida += aumento_vida
        print(f"La vida subió de {programon.vida-aumento_vida} a"
              f" {programon.vida}")

class Pocion(Objetos):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento_ataque = randint(1,7)
        print(f"Aumento de ataque: {aumento_ataque}")
        programon.ataque += aumento_ataque
        print(f"El ataque subió de {programon.ataque-aumento_ataque} a"
              f" {programon.ataque}")


class Caramelo(Baya, Pocion):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        programon.defensa += AUMENTO_DEFENSA
        print(f"Aumento de defensa: {AUMENTO_DEFENSA}\n"
              f"La defensa subió de {programon.defensa-AUMENTO_DEFENSA}"
              f" a {programon.defensa}")
