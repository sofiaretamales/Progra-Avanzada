import os
from random import randint
from parametros import PROB_BESTIA, POND_PUNT
from funciones_utiles import (pedir_input_letra, 
                              pedir_input_int, 
                              lista_a_string)
class Partida:
    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.lista_tablero = []
        self.tablero_con_bestias = []
        self.filas = 0
        self.columnas = 0
        self.N_bestias = 0
        self.seguir_jugando = True
        self.pierde = False
        self.gana = False
        self.puntaje = 0
        self.n_descubiertas = 0
        self.visitadas = []

    def crear_tablero(self, filas, columnas):
        """
        Recibe dos argumentos de tipo int (filas y columnas) y crea
        dos listas de tablero: el que se imprime en la consola, y 
        el que contiene a las bestias.
        """
        self.filas = filas
        self.columnas = columnas
        for fil in range(filas):
            self.lista_tablero.append([])
            self.tablero_con_bestias.append([])
            for col in range(columnas):
                self.lista_tablero[fil].append(' ')
                self.tablero_con_bestias[fil].append(' ')
        self.N_bestias = int(filas*columnas*PROB_BESTIA)
        for bestia in range(self.N_bestias):
            pos_x = randint(0, columnas-1)
            pos_y = randint(0, filas-1)
            #para que no se repitan las posiciones
            while self.tablero_con_bestias[pos_y][pos_x] == 'N': 
                pos_x = randint(0, columnas-1) 
                pos_y = randint(0, filas-1)
            self.tablero_con_bestias[pos_y][pos_x] = 'N'

    def jugar_partida(self):
        """
        Pide las coordenadas a despejar y continúa el flujo
        del juego según si estaba ocupada por bestias o no.
        """
        print('\n¿Qué coordenada desea despejar?\n'
              'Considérelas según la vista del tablero.\n'
              'Columna (letra): ')
        pos_let = pedir_input_letra(self.columnas)
        print('Fila (número): ')
        pos_num = pedir_input_int(range(self.filas))
        if self.tablero_con_bestias[pos_num][pos_let] == 'N':
            self.seguir_jugando = False
            self.pierde = True
            self.calcular_puntaje()
            self.guardar_puntaje()
        elif [pos_num, pos_let] in self.visitadas:
            print('\nLo siento, ya despejaste ese sector, inténtalo de nuevo')
            self.jugar_partida()
        elif [pos_num, pos_let] not in self.visitadas:
            if self.contar_bestias(pos_num, pos_let) == 0:
                self.lista_tablero[pos_num][pos_let] = 0
                self.vecinos(pos_num, pos_let)
            else: 
                n_bestias = self.contar_bestias(pos_num, pos_let)
                self.lista_tablero[pos_num][pos_let] = n_bestias
                self.visitadas.append([pos_num, pos_let])
        if self.comprobar_ganador():
            self.seguir_jugando = False
            self.gana = True
            self.calcular_puntaje()
            self.guardar_puntaje()
                
    def contar_bestias(self, fil, col):
        """
        Recibe dos argumentos de tipo int (fila y columna) y
        cuenta la cantidad de bestias vecinas de tal coordenada
        y retorna ese número.
        """
        contador = 0
        for f in range(-1, 2):
            for c in range(-1, 2):
                fila_valida = ((fil+f >= 0) and 
                               (fil+f < len(self.lista_tablero)))
                columna_valida = ((col+c >= 0) and 
                                  (col+c < len(self.lista_tablero[f])))
                if fila_valida and columna_valida:
                    if f != 0 or c != 0:
                        if self.tablero_con_bestias[fil+f][col+c] == 'N':
                            contador += 1
        return contador

    def vecinos(self, fil, col):
        """
        Método recursivo que recibe una casilla (fila y columna)
        y llama al método 'contar_bestias' para aquellas casillas 
        vecinas que no contengan bestias alrededor.  
        """
        if [fil, col] not in self.visitadas:
            self.visitadas.append([fil, col])
            if self.contar_bestias(fil, col) == 0:
                self.lista_tablero[fil][col] = self.contar_bestias(fil, col)
                for f in range(-1, 2):
                    for c in range(-1, 2):
                        fila_valida = ((fil+f >= 0) and 
                                       (fil+f < len(self.lista_tablero)))
                        columna_valida = ((col+c >= 0) and 
                                          (col+c < len(self.lista_tablero[f])))
                        if fila_valida and columna_valida:
                            if f != 0 or c != 0:
                                self.vecinos(fil+f, col+c)
            elif self.contar_bestias(fil, col) != 0:
                self.lista_tablero[fil][col] = self.contar_bestias(fil, col)

    def comprobar_ganador(self):
        """
        Comprueba que si todas las casillas sin bestias fueron 
        descubiertas, el usuario gana y retorna True.
        """
        contador = 0
        for fil in range(self.filas):
            for col in range(self.columnas):
                casilla = self.lista_tablero[fil][col]
                casilla_bestia = self.tablero_con_bestias[fil][col]
                if casilla != ' ' and casilla_bestia != 'N':
                    contador += 1
        self.n_descubiertas = contador
        if contador == self.filas*self.columnas - self.N_bestias:
            return True
        else:
            return False

    def guardar_partida(self):
        """
        Guarda la partida en su archivo correspondiente 
        de la carpeta 'partidas'.
        """
        ruta = os.path.join('partidas', self.nombre_usuario+'.txt')
        with open(ruta, 'w', encoding='utf-8') as partidas:
            tablero_en_str = lista_a_string(self.lista_tablero, self.filas)
            tablero_bestia_str = lista_a_string(self.tablero_con_bestias, self.filas)
            self.visitadas_str = lista_a_string(self.visitadas, self.n_descubiertas)
            info = (f'{self.nombre_usuario}\n{self.filas}\n{self.columnas}\n'
                    f'{self.N_bestias}\n{tablero_en_str}\n{tablero_bestia_str}\n'
                    f'{self.visitadas_str}\n{self.n_descubiertas}')
            partidas.write(info)
        
    def calcular_puntaje(self):
        """Calcula el puntaje del ganador/perdedor."""
        self.puntaje = self.N_bestias*self.n_descubiertas*POND_PUNT  

    def guardar_puntaje(self):
        """Guarda el puntaje en el archivo 'puntajes.txt'."""
        ruta = os.path.join('puntajes' , 'puntajes.txt')
        with open(ruta, 'a', encoding='utf-8') as puntajes:
            texto = (f'{self.nombre_usuario}, {self.puntaje} \n') 
            puntajes.write(texto)