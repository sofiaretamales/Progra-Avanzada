from sys import exit
from Entrenador import Entrenador
from Programon import Planta, Fuego, Agua
from Objetos import Baya, Pocion, Caramelo
from parametros import GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO \
                        , GASTO_ENERGIA_POCION, PROB_EXITO_BAYA \
                        , PROB_EXITO_CARAMELO, PROB_EXITO_POCION \
                        , RUTA_ENTRENADORES, RUTA_OBJETOS \
                        , RUTA_PROGRAMONES, RUTA_RONDAS

def pedir_input(rango): 
    inp = input()
    if not inp.isdigit() or int(inp) not in rango:
        print('Por favor seleccione una opción válida:')
        inp = pedir_input(rango)
    return int(inp)

def abrir_entrenadores():
    with open(RUTA_ENTRENADORES, 'r', encoding='utf-8') as entrenadores:
        next(entrenadores)
        todos_entrenadores = []
        for entrenador in entrenadores:
            info_entrenador = entrenador.strip().split(',')
            nombre = info_entrenador[0]
            programones = info_entrenador[1].split(';')
            energia = int(info_entrenador[2])
            objetos = info_entrenador[3].split(';')
            objeto_entrenador = Entrenador(
                nombre, programones, energia, objetos)
            todos_entrenadores.append(objeto_entrenador)
    return todos_entrenadores


def abrir_programones():
    with open(RUTA_PROGRAMONES, 'r', encoding='utf-8') as programones:
        next(programones)
        todos_programones = []
        for programon in programones:
            info_programon = programon.strip().split(',')
            nombre = info_programon[0]
            tipo = info_programon[1]
            nivel = int(info_programon[2])
            vida = int(info_programon[3])
            ataque = int(info_programon[4])
            defensa = int(info_programon[5])
            velocidad = int(info_programon[6])
            if tipo == 'planta':
                objeto_programon = Planta(
                        nombre,tipo, nivel, vida, ataque, defensa, velocidad)
            elif tipo == 'fuego':
                objeto_programon = Fuego(
                        nombre, tipo, nivel, vida, ataque, defensa, velocidad)
            elif tipo == 'agua':
                objeto_programon = Agua(
                        nombre, tipo, nivel, vida, ataque, defensa, velocidad)
            todos_programones.append(objeto_programon)
    return todos_programones

def abrir_objetos():
    with open(RUTA_OBJETOS, 'r', encoding='utf-8') as objetos:
        next(objetos)
        objetos_baya = []
        objetos_pocion = []
        objetos_caramelo = []
        todos_objetos = []
        for obj in objetos:
            info_objeto = obj.strip().split(',')
            nombre = info_objeto[0]
            tipo = info_objeto[1]
            if tipo == 'baya':
                objeto = Baya(nombre=nombre, tipo=tipo \
                              , costo=GASTO_ENERGIA_BAYA \
                              , prob_exito=PROB_EXITO_BAYA)
                objetos_baya.append(objeto)
            elif tipo == 'pocion':
                objeto = Pocion(nombre=nombre, tipo=tipo \
                                , costo=GASTO_ENERGIA_POCION \
                                , prob_exito=PROB_EXITO_POCION)
                objetos_pocion.append(objeto)
            elif tipo == 'caramelo':
                objeto = Caramelo(nombre=nombre, tipo=tipo \
                                  , costo=GASTO_ENERGIA_CARAMELO \
                                  , prob_exito=PROB_EXITO_CARAMELO)
                objetos_caramelo.append(objeto)
        todos_objetos.append(objetos_baya)
        todos_objetos.append(objetos_pocion)
        todos_objetos.append(objetos_caramelo)     
    return todos_objetos

def abrir_archivo_ronda(obj_entrenadores):
    with open(RUTA_RONDAS, 'r', encoding='utf-8') as info_rondas:
        lista_info_ronda = []
        for info in info_rondas:
            lista_info_ronda.append(info.strip())
        entrenadores_str = lista_info_ronda[0].strip('][').split(', ')
        entrenadores = []
        for entrenador in entrenadores_str:
            for obj_entrenador in obj_entrenadores:
                if entrenador == str(obj_entrenador):
                    entrenadores.append(obj_entrenador)
        nombres_perdedores = lista_info_ronda[1].strip('][').split(', ')
        perdedores = []
        for perdedor in nombres_perdedores:
            for obj_entrenador in obj_entrenadores:
                if perdedor == str(obj_entrenador):
                    perdedores.append(obj_entrenador)
        ronda = int(lista_info_ronda[2])
    return entrenadores, perdedores, ronda

def elegir_programon(entrenador, programones):
    for p in entrenador.programones:
        print(f"[{entrenador.programones.index(p)+1}] {p}")
    print(f"[{entrenador.programones.index(p)+2}] Volver al menú de inicio\n"
    "[0] Salir")
    elegir = pedir_input(range(entrenador.programones.index(p)+3))  
    if elegir == entrenador.programones.index(p)+2:
        entrenador.seguir = False
    elif elegir == 0:
        exit() 
    else:
        programon_elegido = entrenador.programones[elegir-1]
        for programon in programones:
            if programon.nombre == programon_elegido:
                programon_elegido = programon
        return programon_elegido 
