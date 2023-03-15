from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, especie, **kwargs):
        self.especie = especie
        self.ganancia_actual = 0

    @abstractmethod
    def alimentarse(self):
        pass

    @abstractmethod
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


class Carnivoro(Animal):

    def __init__(self, ferocidad, **kwargs):
        super().__init__(**kwargs)
        self.ferocidad = ferocidad
        self.ganancia_actual += GAN_CARNIVORO

    def alimentarse(self):
        super().alimentarse()
        self.ferocidad += INCREMENTO_FEROCIDAD
        print(f"Animal {self.especie} se come un kilogramo de Carne")

    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_CARNIVORO, MAX_EX_CARNIVORO)
        self.ganancia_actual += self.ferocidad*ponderador


class Herbivoro(Animal):

    def __init__(self, adorabilidad, **kwargs):
        super().__init__(**kwargs)
        self.adorabilidad = adorabilidad
        self.ganancia_actual += GAN_HERBIVORO

    def alimentarse(self):
        super().alimentarse()
        self.adorabilidad += INCREMENTO_ADORABILIDAD
        print(f"Animal {self.especie} se come un kilogramo de vegetales")

    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_HERVIBORO, MAX_EX_HERVIBORO)
        self.ganancia_actual += self.adorabilidad*ponderador 


class Omnivoro(Carnivoro, Herbivoro):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def alimentarse(self):
        super().alimentarse()

    def exhibicion(self):
        super().exhibicion()

