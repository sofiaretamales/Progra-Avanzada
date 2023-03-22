from os.path import join

# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000 
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 5000
INTERVALO_APARICION_SOLES = 3000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5 
DANO_MORDIDA = 10
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 5
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15

#Tamaño ventana juego
ANCHO_VENTANA = 840
LARGO_VENTANA = 570
#Rutas
RUTA_VENTANA_JUEGO_DIA = join('Ventanas', 'ventana_juego_abuela.ui' )
RUTA_VENTANA_JUEGO_NOCTURNO = join('Ventanas', 'ventana_juego_nocturno.ui')
RUTA_VENTANA_RANKING = join('Ventanas', 'ventana_ranking.ui')
RUTA_VENTANA_POSTRONDA_GANADOR = join('Ventanas', 
                                      'ventana_postronda_ganador.ui')
RUTA_VENTANA_POSTRONDA_PERDEDOR = join('Ventanas', 
                                       'ventana_postronda_perdedor.ui')
RUTA_PUNTAJES = join('puntajes.txt')
RUTA_ZOMBIE_CLASICO_CAMINANDO_1 = join('sprites', 'Zombies', 'Caminando',
                                     'zombieNicoWalker_1')
RUTA_ZOMBIE_CLASICO_CAMINANDO_2 = join('sprites', 'Zombies', 'Caminando',
                                     'zombieNicoWalker_2')
RUTA_ZOMBIE_RAPIDO_CAMINANDO_1 = join('sprites', 'Zombies', 'Caminando',
                                     'zombieHernanRunner_1')
RUTA_ZOMBIE_RAPIDO_CAMINANDO_2 = join('sprites', 'Zombies', 'Caminando',
                                     'zombieHernanRunner_2')

RUTA_ZOMBIE_CLASICO_COMIENDO_1 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieNicoComiendo_1')
RUTA_ZOMBIE_CLASICO_COMIENDO_2 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieNicoComiendo_2')
RUTA_ZOMBIE_CLASICO_COMIENDO_3 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieNicoComiendo_3')                                     
RUTA_ZOMBIE_RAPIDO_COMIENDO_1 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieHernanComiendo_1')
RUTA_ZOMBIE_RAPIDO_COMIENDO_2 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieHernanRunner_2')
RUTA_ZOMBIE_RAPIDO_COMIENDO_3 = join('sprites', 'Zombies', 'Comiendo',
                                     'zombieHernanComiendo_3')
RUTA_GIRASOL_1 = join('sprites', 'Plantas', 'girasol_1.png')
RUTA_GIRASOL_2 = join('sprites', 'Plantas', 'girasol_2.png')
RUTA_LANZAGUISANTES_1 = join('sprites', 'Plantas', 'lanzaguisantes_1.png')
RUTA_LANZAGUISANTES_2 = join('sprites', 'Plantas', 'lanzaguisantes_2.png')
RUTA_LANZAGUISANTES_3 = join('sprites', 'Plantas', 'lanzaguisantes_3.png')
RUTA_LANZAGUISANTESHIELO_1 = join('sprites', 'Plantas', 'lanzaguisantesHielo_1.png')
RUTA_LANZAGUISANTESHIELO_2 = join('sprites', 'Plantas', 'lanzaguisantesHielo_2.png')
RUTA_LANZAGUISANTESHIELO_3 = join('sprites', 'Plantas', 'lanzaguisantesHielo_3.png')
RUTA_PAPA_1 = join('sprites', 'Plantas', 'papa_1.png')
RUTA_PAPA_2 = join('sprites', 'Plantas', 'papa_2.png')
RUTA_PAPA_3 = join('sprites', 'Plantas', 'papa_3.png')
RUTA_GUISANTE_1 = join('sprites', 'Elementos de juego', 'guisante_1.png')
RUTA_GUISANTE_2 = join('sprites', 'Elementos de juego', 'guisante_2.png')
RUTA_GUISANTE_3 = join('sprites', 'Elementos de juego', 'guisante_3.png')
RUTA_GUISANTEHIELO_1 = join('sprites', 'Elementos de juego', 'guisanteHielo_1.png')
RUTA_GUISANTEHIELO_2 = join('sprites', 'Elementos de juego', 'guisanteHielo_2.png')
RUTA_GUISANTEHIELO_3 = join('sprites', 'Elementos de juego', 'guisanteHielo_3.png')
RUTA_SOL = join('sprites', 'elementos de juego', 'sol.png')

#ANCHO Y ALTO ZOMBIES
ANCHO_ZOMBIE = 41
ALTO_ZOMBIE = 61
POS_INICIO_ZOMBIE_CARRIL1 = (840, 150, ANCHO_ZOMBIE, ALTO_ZOMBIE)
POS_INICIO_ZOMBIE_CARRIL2 = (840, 220, ANCHO_ZOMBIE, ALTO_ZOMBIE)
INTERVALO_MOVIMIENTO_ZOMBIES = 1000

#Area a plantar
ANCHO_AREA_PLANTAR = 391
ALTO_AREA_PLANTAR = 141
POS_AREA_PLANTAR = (240, 150)
INTERVALO_EN_X = (POS_AREA_PLANTAR[0], POS_AREA_PLANTAR[0] + ANCHO_AREA_PLANTAR)
INTERVALO_EN_Y = (POS_AREA_PLANTAR[1], POS_AREA_PLANTAR[1] + ALTO_AREA_PLANTAR)

#ANCHO Y ALTO PLANTAS
ANCHO_PLANTA = 40
ALTO_PLANTA = 55
ANCHO_PROYECTIL = 21
ALTO_PROYECTIL = 31
INTERVALO_MOVIMIENTO_PLANTAS = 660

#Posicion casa
POS_CASA_X = 240

#velocidad de proyectiles
VELOCIDAD_PROYECTIL = 10
INTERVALO_MOV_PROYECTIL = 20

#Geometría sol
ANCHO_SOL = 40
ALTO_SOL = 40
RANGO_SOL_X = (110, ANCHO_VENTANA)
RANGO_SOL_Y = (0, 390)
TIEMPO_PERMANENCIA_SOL = 6000

#Texto final
RUTA_TEXTO_PERDEDOR = join('sprites', 'Elementos de juego', 'textoFinal.png')
ANCHO_TEXTO_PERDEDOR = 460
ALTO_TEXTO_PERDEDOR = 290
POS_X_TEXTO_PERDEDOR = 230
POS_Y_TEXTO_PERDEDOR = 80
RUTA_TEXTO_GANADOR = join('sprites', 'Elementos de juego', 'mensaje_ganador.png')
ANCHO_TEXTO_GANADOR = 590
ALTO_TEXTO_GANADOR = 411
POS_X_TEXTO_GANADOR = 200
POS_Y_TEXTO_GANADOR = 60
TIEMPO_MENSAJE_FINAL = 3000