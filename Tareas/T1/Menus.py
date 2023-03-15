from sys import exit
from parametros import ENERGIA_ENTRENAMIENTO, RUTA_RONDAS
from LigaProgramon import LigaProgramon
from funciones_utiles import abrir_archivo_ronda, abrir_entrenadores \
                            , abrir_objetos, abrir_programones, pedir_input \
                            , elegir_programon

class FlujoMenus:

    def __init__(self):
        self.entrenadores = None
        self.programones = None
        self.objetos = None

    def menu_inicio(self):
        while True:
            self.entrenadores = abrir_entrenadores()
            self.programones = abrir_programones()
            self.objetos = abrir_objetos()
            print("\n"+"="*48,"MENÚ DE INICIO","="*48)
            print("\nEscoja el entrenador que desea utilizar en el DCCampeonato\n")
            contador = 0
            for entrenador in self.entrenadores:
                contador += 1
                print(f"[{contador}] {entrenador.nombre}: "
                    f"{', '.join(entrenador.programones)}")
            print("[0] Salir")
            opcion = pedir_input(range(contador+1))
            if opcion == 0:
                exit()
            else:
                entrenador_elegido = self.entrenadores[opcion-1]
                with open(RUTA_RONDAS, 'w', encoding='utf-8') as info_rondas:
                    info = (f"{self.entrenadores}\n[]\n1")
                    info_rondas.write(info)
                self.menu_entrenador(entrenador_elegido)

    def menu_entrenador(self, entrenador):
        while entrenador.seguir:
            print("\n"+"="*50,"MENÚ ENTRENADOR","="*50)
            print("\nEscoja la acción que desea realizar:\n"
                  "\n[1] Ir a entrenar\n"
                  "[2] Simular ronda\n"
                  "[3] Ver resumen del campeonato\n"
                  "[4] Crear objetos\n"
                  "[5] Utilizar objeto\n"
                  "[6] Ver estado del entrenador\n"
                  "[7] Volver al menú de inicio\n"
                  "[0] Salir")
            accion = pedir_input(range(8))
            if accion == 1:
                self.menu_entrenamiento(entrenador)
            elif accion == 2:
                print("\n"+"*"*45,"Elige tu luchador","*"*45)
                programon_elegido = elegir_programon(entrenador, self.programones)
                info_ronda = abrir_archivo_ronda(self.entrenadores)
                ganadores = info_ronda[0]
                perdedores = info_ronda[1]
                ronda_actual = info_ronda[2]
                ronda = LigaProgramon(self.entrenadores, perdedores, ronda_actual)
                ronda.simular_ronda(ganadores, entrenador, programon_elegido, \
                                    self.programones)
                if not entrenador.seguir:
                    print("\n¿Qué acción desea realizar?\n"
                          "[1] Volver al menú de inicio\n"
                          "[0] Salir")
                    accion = pedir_input(range(2))
                    if accion == 0:
                        exit()
                    elif accion == 1:
                        entrenador.seguir = False
                else:
                    print("\nPresione ENTER para desplegar el menú de entrenador")
                    input()
            elif accion == 3:
                info_ronda = abrir_archivo_ronda(self.entrenadores)
                perdedores = info_ronda[1]
                ronda_actual = info_ronda[2]
                ronda = LigaProgramon(self.entrenadores, perdedores, ronda_actual)
                ronda.resumen_campeonato()
                print("\nPresione ENTER para desplegar el menú de entrenador")
                input()
            elif accion == 4:
                self.menu_crear_objeto(entrenador)
                print("\nPresione ENTER para desplegar el menú de entrenador")
                input()
            elif accion == 5:
                self.menu_utilizar_objeto(entrenador)
                print("\nPresione ENTER para desplegar el menú de entrenador")
                input()
            elif accion == 6:
                programones_entrenador = []
                for programon_entrenador in entrenador.programones:
                    for programon in self.programones:
                        if programon_entrenador == programon.nombre:
                            programones_entrenador.append(programon)
                entrenador.estado_entrenador(programones_entrenador)
                print("\nPresione ENTER para desplegar el menú de entrenador")
                input()
            elif accion == 7:
                entrenador.seguir = False
            elif accion == 0:
                exit()

    def menu_entrenamiento(self, entrenador):
        print("\n"+"="*48,"MENÚ DE ENTRENAMIENTO","="*48)
        print("\nEscoja al programón que desea entrenar")
        programon_elegido = elegir_programon(entrenador, self.programones)
        if programon_elegido != None:
            if programon_elegido.nivel == 100: 
                print("\nEl programón ha alcanzado el máximo nivel")
            elif entrenador.energia < ENERGIA_ENTRENAMIENTO:
                print(f"Lo siento, no tienes sufiente energía para entrenar"
                      f" a {programon_elegido.nombre}:(")
            else:
                entrenador.energia -= ENERGIA_ENTRENAMIENTO
                print(f"La energía de {entrenador.nombre} ha disminuido en" 
                      f" {ENERGIA_ENTRENAMIENTO}\nSu energía anterior era "
                      f"{entrenador.energia + ENERGIA_ENTRENAMIENTO}"
                      f" y ahora es {entrenador.energia}")
                programon_elegido.entrenar(programon_elegido.nombre)
            print('\nPresione ENTER para volver al menú de entrenador')
            input()

    def menu_crear_objeto(self, entrenador):
        print("\n"+"="*50,"MENÚ DE OBJETOS","="*50)
        print("[1] Baya\n[2] Poción\n[3] Caramelo\n"
              "[4] Volver al menú de inicio\n"
              "[0] Salir")
        eleccion = pedir_input(range(8))
        if eleccion == 1:
            entrenador.crear_objetos(self.objetos[0])
        elif eleccion == 2:
            entrenador.crear_objetos(self.objetos[1])
        elif eleccion == 3:
            entrenador.crear_objetos(self.objetos[2])
        elif eleccion == 4:
            self.menu_inicio()
        elif eleccion == 0:
            exit()

    def menu_utilizar_objeto(self, entrenador):
        print("\n"+"*"*45,"Objetos disponibles","*"*45)
        if entrenador.objetos == []:
            print("No tienes objetos disponibles :(")
        else:
            for objeto in entrenador.objetos:
                print(f"[{entrenador.objetos.index(objeto)+1}] {objeto}")
            print(f"[{entrenador.objetos.index(objeto)+2}] Volver al menú "
                  "de inicio\n[0] Salir")
            elegir = pedir_input(range(entrenador.objetos.index(objeto)+3))
            if elegir == entrenador.objetos.index(objeto)+2:
                self.menu_inicio()
            elif elegir == 0:
                exit()
            else:
                objeto_elegido = entrenador.objetos[elegir-1]
                for tipo in self.objetos:
                    for objeto in tipo:
                        if objeto_elegido == objeto.nombre:
                            objeto_elegido = objeto
                print("\nElige al programón a quién quieres aplicar el objeto\n")
                programon_elegido = elegir_programon(entrenador, self.programones)
                print(f"\nProgramón beneficiado: {programon_elegido.nombre}\n"
                      f"Objeto utilizado: {objeto_elegido.nombre}" 
                      f"({objeto_elegido.tipo})")
                objeto_elegido.aplicar_objeto(programon_elegido)
                entrenador.objetos.remove(objeto_elegido.nombre)