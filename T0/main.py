import os
import sys
from class_partida import Partida
from tablero import print_tablero
from funciones_utiles import (crear_ranking, 
                              pedir_input_int, 
                              string_a_lista)
def menu_inicio():
    while True:
        print('\nBienvenid@ a Star Advanced\n'
              '\nSeleccione una opción:\n'
              '[1] Crear partida \n'
              '[2] Cargar partida existente \n' 
              '[3] Ver ranking \n'
              '[0] Salir')
        respuesta = pedir_input_int(range(4))
        if respuesta == 1:
            print('\nTu objetivo será derrotar al malvado Canciller que intenta '
            'convertirse en el Emperador del Imperio Galáctico.\nPara esto, tendrás '
            'que encontrar a todas sus bestias escondidas en el Templo...')
            n_usuario = input('\nIngrese su nombre de usuario para comenzar: ')
            while not n_usuario.isalnum():
                n_usuario = input('\nPor favor ingrese un nombre de usuario válido: ')
            usuario = Partida(n_usuario)
            print('\nSeleccione el tamaño de su tablero\n'
                  'Nota: su dimensión no puede ser menor a 3x3 o mayor a 15x15') 
            print('\nNúmero de filas:')
            filas = pedir_input_int(range(3,16))
            print('Número de columnas:')
            columnas = pedir_input_int(range(3,16)) 
            usuario.crear_tablero(filas, columnas) 
            menu_juego(usuario)                  
        elif respuesta == 2:
            n_usuario = input('\nIngrese su nombre de usuario para cargar partida: ')
            ruta = os.path.join('partidas', n_usuario + '.txt')
            existe = os.path.exists(ruta)
            if existe:
                with open(ruta, 'r', encoding='utf-8') as p_usuario:
                    lista_info = []
                    for p in p_usuario:
                        lista_info.append(p.strip())
                    usuario = Partida(lista_info[0])
                    usuario.filas = int(lista_info[1])
                    usuario.columnas = int(lista_info[2])
                    usuario.N_bestias = int(lista_info[3])
                    usuario.lista_tablero = string_a_lista(lista_info[4])
                    usuario.tablero_con_bestias = string_a_lista(lista_info[5])
                    usuario.visitadas = string_a_lista(lista_info[6])
                    usuario.n_descubiertas = int(lista_info[7])
                menu_juego(usuario)       
            else:
                print(f'\nLa partida de {n_usuario} no existe')                
        elif respuesta == 3:
            ruta = os.path.join('puntajes', 'puntajes.txt')
            lista_ranking = crear_ranking(ruta)
            print('\n  RANKING MEJORES PUNTAJES\n'
                  'Nombre de usuario    Puntaje')
            for posicion in lista_ranking:
                print(f'{posicion[0]:15s} {posicion[1]: ^16s}')
            print('\nPresione ENTER para volver al menú de inicio')
            input()
        elif respuesta == 0:
            sys.exit() 

def menu_juego(usuario):
    accion = None
    while usuario.seguir_jugando and accion != (2,3,4):
        print('\nEstado actual de su tablero: ')
        print_tablero(usuario.lista_tablero)
        print('\nSeleccione una acción \n'
              '[1] Descubrir un sector \n'
              '[2] Guardar la partida \n'
              '[3] Volver al menú de inicio\n'
              '[0] Salir del juego')
        accion = pedir_input_int(range(4))
        if accion == 1:
            usuario.jugar_partida()
        elif accion == 2:
            usuario.guardar_partida()
        elif accion == 3:
            print('\n¿Desea guardar la partida?\n'
                  '[1] Si \n'
                  '[0] No' )
            seleccion = pedir_input_int(range(2))
            if seleccion == 1:
                usuario.guardar_partida()
                print('\n¡La partida se ha guardado con éxito!')
                menu_inicio()
            elif seleccion == 0:        
                menu_inicio() 
        elif accion == 0:
            print('\n¿Desea guardar la partida?\n'
                  '[1] Si \n'
                  '[0] No' )
            seleccion = pedir_input_int(range(2))
            if seleccion == 1:
                usuario.guardar_partida()
                print('\n¡La partida se ha guardado con éxito!')
                sys.exit()
            elif seleccion == 0:        
                sys.exit()  
    if usuario.gana:
        menu_ganador(usuario)    
    elif usuario.pierde:
        menu_perdedor(usuario)

def menu_ganador(usuario):
    print(f'\n¡Felicitaciones {usuario.nombre_usuario}!\n'
          '¡Has logrado derrotar al malvado Canciller!\n'
          f'Has obtenido un puntaje de {usuario.puntaje}\n'
          '\n¿Qué acción desea realizar? \n'
          '[1] Volver al menú de inicio\n'
          '[0] Salir del juego')
    ac = pedir_input_int(range(2))
    if ac == 1:
        menu_inicio()
    elif ac == 0:
        sys.exit()

def menu_perdedor(usuario):
    print(f'\nLo siento {usuario.nombre_usuario}, ' 
          'no pudiste derrotar al malvado Canciller :c\n'
          f'Obtuviste un puntaje de {usuario.puntaje}\n'
          'Las bestias se encontraban en:')
    print_tablero(usuario.tablero_con_bestias)
    print('\n¿Qué acción desea realizar?\n'
          '[1] Volver al menu de inicio\n'
          '[0] Salir del juego')     
    ac = pedir_input_int(range(2))
    if ac == 1:
        menu_inicio()
    elif ac == 0:
        sys.exit()

if __name__ == "__main__":
    menu_inicio()