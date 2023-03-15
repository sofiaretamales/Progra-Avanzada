from random import randint, choice
from parametros import RUTA_RONDAS

class LigaProgramon:

    def __init__(self, entrenadores, perdedores, ronda_actual):
        self.entrenadores = entrenadores
        self.perdedores = perdedores
        self.ronda_actual = ronda_actual
        self.campeon = None

    def resumen_campeonato(self):
        print("\n"+"="*50,"RESUMEN CAMPEONATO","="*50)
        nombre_participantes = []
        entrenadores_compitiendo = self.entrenadores.copy()
        for participante in self.entrenadores:
            nombre_participantes.append(participante.nombre)
        for perdedor in self.perdedores:
            entrenadores_compitiendo.remove(perdedor)
        nombre_en_competencia = []
        for entrenador in entrenadores_compitiendo:
            nombre_en_competencia.append(entrenador.nombre)
        print(f"\nParticipantes:\n{', '.join(nombre_participantes)}") 
        print(f"\nRonda actual: {self.ronda_actual}")
        print("\nEntrenadores que siguen en la competencia:\n"
              f"{', '.join(nombre_en_competencia)}")

    def simular_ronda(self, entrenadores_compitiendo, mi_entrenador \
                      , mi_programon, programones):
        print("\n"+"="*50,f"RONDA {self.ronda_actual}","="*50)
        n_entrenadores = len(entrenadores_compitiendo)
        lista_tuplas = [(mi_entrenador, mi_programon)]
        pos_usadas = []
        luchas = []
        ganadores = []
        #asociar entrenador a programon random
        for entrenador in entrenadores_compitiendo: 
            if entrenador != mi_entrenador:
                programon_a_ocupar = choice(entrenador.programones)
                for programon in programones:
                    if programon_a_ocupar == programon.nombre:
                        programon_a_ocupar = programon
                lista_tuplas.append((entrenador, programon_a_ocupar))
        #elegir qué parejas se enfrentan
        for parejas in range(int(n_entrenadores/2)):
            pareja = []
            for entrenador_en_pareja in range(2):
                pos_elegida = randint(0, n_entrenadores-1)
                while pos_elegida in pos_usadas:
                    pos_elegida = randint(0, n_entrenadores-1)
                pareja.append(lista_tuplas[pos_elegida])
                pos_usadas.append(pos_elegida)
            luchas.append(pareja)
        #batallas
        for lucha in luchas: 
            #lucha será algo así como [(entr0, pro0), (entr1, pro1)]
            print(f"\n{lucha[0][0].nombre} ({lucha[0][1].nombre}) "
            f"V/S {lucha[1][0].nombre} ({lucha[1][1].nombre})")
            puntaje1 = lucha[0][1].luchar(lucha[1][1].tipo)
            puntaje2 = lucha[1][1].luchar(lucha[0][1].tipo)
            if puntaje1 > puntaje2:
                print(f"{lucha[0][0].nombre} ha ganado la batalla")
                ganadores.append(lucha[0][0])
                self.perdedores.append(lucha[1][0])
                lucha[0][1].ganar_batalla()
            elif puntaje2 > puntaje1:
                print(f"{lucha[1][0].nombre} ha ganado la batalla")
                ganadores.append(lucha[1][0])
                self.perdedores.append(lucha[0][0])
                lucha[1][1].ganar_batalla()
        for entrenador in entrenadores_compitiendo:
            entrenador.energia = 100
        if mi_entrenador in self.perdedores and self.ronda_actual != 4:
            mi_entrenador.seguir = False
            print(f"\nLo siento {mi_entrenador.nombre}, has quedado fuera"
                  " del DCCampeonato:(")
        elif self.ronda_actual == 4:
            self.campeon = ganadores[0]
            if self.campeon == mi_entrenador:
                print(f"\nFELICIDADES {mi_entrenador.nombre}, has ganado"
                " el DCCampeonato!!!")
            else:
                print(f"\n{self.campeon.nombre} es el campeón"
                " del DCCampeonato")
            mi_entrenador.seguir = False
        else:
            with open(RUTA_RONDAS, 'w', encoding='utf-8') as info_ronda:
                ronda = (f"{ganadores}\n{self.perdedores}\n{self.ronda_actual + 1}")
                info_ronda.write(ronda)