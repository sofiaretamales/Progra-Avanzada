from random import randint, choice, random
from fauna import Carnivoro, Herbivoro, Omnivoro
from parametros import MULTIPLICADOR_RECAUDACION, EVENTO_HERBIVOROS \
                        ,EVENTO_CARNIVOROS, FEROCIDAD, ADORABILIDAD \
                        ,PROBABILIDAD_EVENTO, VISITANTES
from abc import ABC, abstractmethod

class Atraccion(ABC):

    def __init__(self, numero):
        self.id = numero
        self.animales = []
        self.especies_disponibles = {"Carnivoro":[], "Herbivoro":[], "Omnivoro":[]}
        self.cargar_especies("especimenes.csv")

    def cargar_especies(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                tipo, especie = linea.strip("\n").split(",")
                self.especies_disponibles[tipo].append(especie)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentarse()

    @property
    def visitantes(self):
        n_visitantes = randint(VISITANTES[0], VISITANTES[1])
        return n_visitantes

    @property
    def recaudacion(self):
        dinero = 0
        for animal in self.animales:
            animal.exhibicion()
            dinero += animal.ganancia_actual
        rec = dinero*self.visitantes*MULTIPLICADOR_RECAUDACION
        probabilidad = random()
        if probabilidad > PROBABILIDAD_EVENTO:
            rec += self.evento()
        return rec

    @abstractmethod   
    def crear_animales(self):
        pass
      
    @abstractmethod 
    def __str__(self):
        pass

    @abstractmethod
    def evento(self):
        pass


class GranjaHerbivoros(Atraccion):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def crear_animales(self):
        tipo = choice(["Herbivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Herbivoro":
            animal = Herbivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    def __str__(self):
        texto = f"Granja de Herbivoros {self.id}"
        return texto
    
    def evento(self):
        print(f"\nEVENTO {self}: AVISTAMIENTO DE BRACHIOSAURUS\n ")
        return EVENTO_HERBIVOROS
        

class PaseoCarnivoros(Atraccion):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def crear_animales(self):
        tipo = choice(["Carnivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Carnivoro":
            animal = Carnivoro(especie=seleccionada, ferocidad=randint(*FEROCIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    def __str__(self):
        texto = f"Paseo de Carnivoros {self.id}"
        return texto
    
    def evento(self):
        print(f"\nEVENTO {self}: SE ALIMENTARA AL TYRANOSAURUS\n ")
        return EVENTO_CARNIVOROS
