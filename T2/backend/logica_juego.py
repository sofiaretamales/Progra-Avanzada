from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QRect, QPoint
import parametros as p
from backend.elementos_juego import GuisanteClasico, GuisanteHielo, Guisantes \
                                    , Plantas, ZombieClasico, ZombieRapido \
                                    , Zombies , Girasol, PlantaClasica \
                                    , PlantaAzul, PlantaPatata, Soles
from random import choice, randint, shuffle
from aparicion_zombies import intervalo_aparicion
from math import ceil

class LogicaJuego(QObject):

    senal_cargar_datos_iniciales = pyqtSignal(dict)
    senal_mostrar_zombies = pyqtSignal(Zombies)
    senal_actualizar_pos_zombie = pyqtSignal(tuple)
    senal_actualizar_datos_zombie = pyqtSignal(dict)
    senal_cambiar_zombie_comiendo = pyqtSignal(Zombies)
    senal_planta_aprobada = pyqtSignal(tuple)
    senal_mover_planta = pyqtSignal(Plantas)
    senal_mostrar_proyectil = pyqtSignal(Guisantes)
    senal_actualizar_proyectil = pyqtSignal(tuple)
    senal_actualizar_label_sol = pyqtSignal(tuple)
    senal_esconder_label = pyqtSignal(tuple)
    senal_actualizar_soles = pyqtSignal(int)
    senal_mostrar_texto_final = pyqtSignal(str)
    senal_mostrar_ventana_post_ronda = pyqtSignal(dict)
    senal_esconder_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ronda = 1
        self.puntaje_total = 0
        self.usuario = ''
        self.fondo = ''

    def recibir_usuario(self, usuario):
        self.usuario = usuario

    def enviar_datos_iniciales(self):
        self.__soles = p.SOLES_INICIALES
        self.puntaje_ronda = 0
        self.zombies_destruidos = 0
        self.zombies_restantes = 0
        self.zombies_no_aparecidos = []
        self.zombies_aparecidos = []
        self.zombies_en_mov = []
        self.pos_ocupadas = []
        self.todas_las_plantas = []
        self.plantas_que_disparan = []
        self.girasoles = []
        self.soles_generados = []
        self.plantas_mordidas = []
        self.timers = []
        self.perdi = False
        self.puedo_comprar_planta = True
        self.paso_a_ventana_post_ronda = False
        datos = {'soles': str(self.soles), 'ronda': str(self.ronda),
                'costo girasol': str(p.COSTO_GIRASOL), 'costo clasica': 
                str(p.COSTO_LANZAGUISANTE), 'costo hielo': 
                str(p.COSTO_LANZAGUISANTE_HIELO), 'costo papa': 
                str(p.COSTO_PAPA), 'zombies destruidos': 
                str(self.zombies_destruidos), 'zombies restantes':
                str(self.zombies_restantes), 'puntaje': str(self.puntaje_ronda)}
        self.senal_cargar_datos_iniciales.emit(datos)

    def empezar_juego(self, fondo):
        if fondo == 'abuela':
            self.fondo = 'Jardin Abuela'
            self.ponderador = p.PONDERADOR_DIURNO
        elif fondo == 'nocturno':
            self.fondo = 'Salida Nocturna'
            self.ponderador = p.PONDERADOR_NOCTURNO
        self.instanciar_timer()
        self.generar_zombies()
        self.crear_proyectil()
    
    def generar_zombies(self):
        for n_zombie in range(p.N_ZOMBIES):
            pos_zombie_carril1 = QRect(*p.POS_INICIO_ZOMBIE_CARRIL1)
            pos_zombie_carril2 = QRect(*p.POS_INICIO_ZOMBIE_CARRIL2)
            zombie_opcion1_1 = ZombieClasico(velocidad = p.VELOCIDAD_ZOMBIE, \
                                            pos = pos_zombie_carril1)
            zombie_opcion2_1 = ZombieRapido(velocidad = 1.5 * p.VELOCIDAD_ZOMBIE, \
                                            pos = pos_zombie_carril1)
            zombie_opcion1_2 = ZombieClasico(velocidad = p.VELOCIDAD_ZOMBIE, \
                                            pos = pos_zombie_carril2)
            zombie_opcion2_2 = ZombieRapido(velocidad = 1.5 * p.VELOCIDAD_ZOMBIE, 
                                            pos = pos_zombie_carril2)
            zombie_carril1 = choice([zombie_opcion1_1, zombie_opcion2_1])
            zombie_carril2 = choice([zombie_opcion1_2, zombie_opcion2_2])
            self.zombies_no_aparecidos.append(zombie_carril1)
            self.zombies_no_aparecidos.append(zombie_carril2)
        shuffle(self.zombies_no_aparecidos) #orden al azar
        self.zombies_restantes = len(self.zombies_no_aparecidos)
        self.actualizar_datos_zombies()
        self.aparecer_zombie()
        self.timer_aparicion_zombies.start()

    def aparecer_zombie(self):
        if self.zombies_no_aparecidos != []:
            self.senal_mostrar_zombies.emit(self.zombies_no_aparecidos[0])
            self.zombies_en_mov.append(self.zombies_no_aparecidos[0])
            self.zombies_aparecidos.append(self.zombies_no_aparecidos.pop(0))

    def mover_zombie(self):
        for zombie in self.zombies_en_mov:
            zombie.x -= zombie.velocidad
            self.senal_actualizar_pos_zombie.emit((zombie, zombie.x, zombie.y)) 
            self.checkear_encuentro_planta_zombie(zombie)
            if zombie.x == p.POS_CASA_X:
                self.perdi = True
        self.comprobar_ganador()

    def checkear_encuentro_planta_zombie(self, zombie):
        for planta in self.todas_las_plantas:
            if zombie in self.zombies_en_mov:
                if zombie.x - planta.x < 30 and zombie.y == planta.y:
                    self.zombies_en_mov.remove(zombie)
                    self.senal_cambiar_zombie_comiendo.emit(zombie)
                    self.plantas_mordidas.append(planta)
                    self.morder_planta()
                    self.timer_mordida.start()

    def morder_planta(self):
        for planta in self.plantas_mordidas:
            if isinstance(planta, PlantaPatata):
                self.senal_mover_planta.emit(planta)
            if planta in self.todas_las_plantas:
                planta.vida -= p.DANO_MORDIDA
                if planta.vida == 0:
                    self.todas_las_plantas.remove(planta)
                    self.plantas_mordidas.remove(planta)
                    if planta in self.plantas_que_disparan:
                        self.plantas_que_disparan.remove(planta)
                    self.senal_esconder_label.emit((planta, planta.x))
                    self.volver_a_mover_zombie()

    def volver_a_mover_zombie(self):
        for zombie in self.zombies_aparecidos:
            if zombie not in self.zombies_en_mov:
                self.zombies_en_mov.append(zombie)

    def actualizar_datos_zombies(self):
        datos = {'zombies destruidos': str(self.zombies_destruidos),
                'zombies restantes': str(self.zombies_restantes),
                'puntaje': str(self.puntaje_ronda)}
        self.senal_actualizar_datos_zombie.emit(datos)

    def comprobar_vida_zombie(self, zombie):
        if zombie.vida == 0:
            self.zombies_aparecidos.remove(zombie)
            self.senal_esconder_label.emit((zombie, zombie.vida))
            self.zombies_destruidos += 1
            self.zombies_restantes -= 1
            if self.fondo == 'Jardin Abuela':
                self.puntaje_ronda += p.PUNTAJE_ZOMBIE_DIURNO
            elif self.fondo == 'Salida Nocturna':
                self.puntaje_ronda += p.PUNTAJE_ZOMBIE_NOCTURNO
            if self.zombies_restantes == 0:
                ptje_extra = ceil(self.puntaje_ronda*self.ponderador)
                self.puntaje_ronda += ptje_extra
            self.actualizar_datos_zombies()

    def comprobar_compra_planta(self, tupla):
        planta = tupla[0]
        pos = tupla[1]
        if planta == 'girasol':
            planta = Girasol(vida_inicial = p.VIDA_PLANTA, \
                            pos = pos)
        elif planta == 'clasica':
            planta = PlantaClasica(vida_inicial = p.VIDA_PLANTA, \
                                        pos = pos)
        elif planta == 'hielo':
            planta = PlantaAzul(vida_inicial = p.VIDA_PLANTA, \
                                pos = pos)
        elif planta == 'patata':
            planta = PlantaPatata(vida_inicial = 2*p.VIDA_PLANTA, \
                                  pos = pos)
        if self.soles >= planta.costo and pos not in self.pos_ocupadas \
            and self.puedo_comprar_planta:
            self.senal_planta_aprobada.emit((True, planta, None))
            self.soles -= planta.costo
            self.pos_ocupadas.append(pos)
            self.todas_las_plantas.append(planta)
            if isinstance(planta, PlantaClasica) or isinstance(planta, PlantaAzul):
                self.plantas_que_disparan.append(planta)
            elif isinstance(planta, Girasol):
                self.girasoles.append(planta)
            self.todas_las_plantas.append(planta)
        elif self.soles < planta.costo:
            self.senal_planta_aprobada.emit((False, planta, 
                                            'soles insuficientes'))
        elif pos in self.pos_ocupadas:
            self.senal_planta_aprobada.emit((False, planta, 
                                            'pos ocupada'))

    def mover_planta(self):
        for planta in self.todas_las_plantas:
            if not isinstance(planta, PlantaPatata):
                self.senal_mover_planta.emit(planta)

    def crear_proyectil(self):
        for planta in self.plantas_que_disparan:
            posicion = QPoint(planta.label.geometry().right(), 
                              planta.label.geometry().top())
            if isinstance(planta, PlantaClasica):
                proyectil = GuisanteClasico(pos = posicion)
            elif isinstance(planta, PlantaAzul):
                proyectil = GuisanteHielo(pos = posicion)
            planta.guisantes.append(proyectil)
            self.senal_mostrar_proyectil.emit(proyectil)
            self.timer_mover_proyectil.start()
    
    def mover_proyectil(self):
        for planta in self.plantas_que_disparan:
            for guisante in planta.guisantes:
                guisante.x += p.VELOCIDAD_PROYECTIL
                self.checkear_colision(guisante, planta)
                self.senal_actualizar_proyectil.emit((guisante, guisante.x, guisante.y))
                if guisante.x >= p.ANCHO_VENTANA:
                    self.senal_esconder_label.emit((guisante, guisante.x))

    def checkear_colision(self, proyectil, planta):
        for zombie in self.zombies_aparecidos:
            if proyectil in planta.guisantes:
                if -7 < zombie.x - proyectil.x < 7 and zombie.y == proyectil.y:
                    planta.guisantes.remove(proyectil)
                    self.senal_esconder_label.emit((proyectil, proyectil.y))
                    zombie.vida -= proyectil.dano
                    self.comprobar_vida_zombie(zombie)
                    if isinstance(proyectil, GuisanteHielo):
                        if zombie.velocidad == zombie.velocidad_inicial:
                            zombie.velocidad -= p.RALENTIZAR_ZOMBIE*zombie.velocidad

    def generar_sol_girasol(self):
        if self.girasoles != []:
            for girasol in self.girasoles:
                for n_sol in range(p.CANTIDAD_SOLES):
                    x = randint(girasol.x - 60, girasol.x + 80)
                    y = randint(girasol.y - 60, girasol.y + 80)
                    pos = QPoint(x, y)
                    sol = Soles(pos)
                    self.senal_actualizar_label_sol.emit((sol, sol.x, sol.y))
                    self.soles_generados.append(sol)

    def generar_sol(self):
        x = randint(*p.RANGO_SOL_X)
        y = randint(*p.RANGO_SOL_Y)
        pos = QPoint(x, y)
        sol = Soles(pos)
        self.senal_actualizar_label_sol.emit((sol, sol.x, sol.y))
        self.soles_generados.append(sol)

    def sumar_sol(self):
        if self.fondo == 'Jardin Abuela':
            self.soles += 2*p.SOLES_POR_RECOLECCION
        elif self.fondo == 'Salida Nocturna':
            self.soles += p.SOLES_POR_RECOLECCION

    def esconder_sol(self):
        if self.soles_generados != []:
            sol = self.soles_generados.pop(0)
            self.senal_esconder_label.emit((sol, sol.y))

    @property
    def soles(self):
        return self.__soles

    @soles.setter
    def soles(self, valor):
        if valor <= 0:
            self.__soles = 0
        else:
            self.__soles = valor
        self.senal_actualizar_soles.emit(self.soles)

    def recibir_senal_tecla(self, cheatcode):
        if cheatcode == 'sun':
            self.soles += p.SOLES_EXTRA
        elif cheatcode == 'kil':
            self.zombies_destruidos = 2*p.N_ZOMBIES

    def comprobar_ganador(self):
        if self.zombies_destruidos == 2*p.N_ZOMBIES:
            self.puntaje_total += self.puntaje_ronda
            self.parar_timers()
            self.senal_mostrar_texto_final.emit('ganador')
            self.timer_mensaje_final.start()
            self.paso_a_ventana_post_ronda = True
        elif self.perdi:
            self.puntaje_total += self.puntaje_ronda
            self.parar_timers()
            self.guardar_puntaje()
            self.senal_mostrar_texto_final.emit('perdedor')
            self.timer_mensaje_final.start()
            self.paso_a_ventana_post_ronda = True

    def pasar_ventana_post_ronda(self):
        self.senal_esconder_ventana.emit()
        if self.paso_a_ventana_post_ronda:
            datos = {'ronda': str(self.ronda), 'soles': str(self.soles),
                    'zombies': str(self.zombies_destruidos), 
                    'puntaje ronda': str(self.puntaje_ronda),
                    'puntaje total': str(self.puntaje_total)} 
            if not self.perdi:
                datos['ganador'] = True
            elif self.perdi:
                datos['ganador'] = False
            self.senal_mostrar_ventana_post_ronda.emit(datos)
            self.ronda += 1
            self.enviar_datos_iniciales()

    def instanciar_timer(self):
        self.timer_aparicion_zombies = QTimer()
        intervalo_aparicion_zombies =  ceil(intervalo_aparicion(self.ronda, \
                                                                self.ponderador))
        self.timer_aparicion_zombies.setInterval(3000*intervalo_aparicion_zombies)
        self.timer_aparicion_zombies.timeout.connect(self.aparecer_zombie)
        self.timers.append(self.timer_aparicion_zombies)
        self.timer_mover_zombie = QTimer()
        self.timer_mover_zombie.setInterval(p.INTERVALO_MOVIMIENTO_ZOMBIES)
        self.timer_mover_zombie.timeout.connect(self.mover_zombie)
        self.timer_mover_zombie.start()
        self.timers.append(self.timer_mover_zombie)
        self.timer_generar_proyectil = QTimer()
        self.timer_generar_proyectil.setInterval(p.INTERVALO_DISPARO)
        self.timer_generar_proyectil.timeout.connect(self.crear_proyectil)
        self.timer_generar_proyectil.start()
        self.timers.append(self.timer_generar_proyectil)
        self.timer_mover_proyectil = QTimer()
        self.timer_mover_proyectil.setInterval(p.INTERVALO_MOV_PROYECTIL)
        self.timer_mover_proyectil.timeout.connect(self.mover_proyectil)
        self.timers.append(self.timer_mover_proyectil)
        if self.fondo == 'Jardin Abuela':
            self.timer_aparicion_soles = QTimer()
            self.timer_aparicion_soles.setInterval(p.INTERVALO_APARICION_SOLES)
            self.timer_aparicion_soles.timeout.connect(self.generar_sol)
            self.timer_aparicion_soles.start()
            self.timers.append(self.timer_aparicion_soles)
            self.timer_permanencia_sol = QTimer()
            self.timer_permanencia_sol.setInterval(p.TIEMPO_PERMANENCIA_SOL)
            self.timer_permanencia_sol.timeout.connect(self.esconder_sol)
            self.timer_permanencia_sol.setSingleShot(True)
        self.timer_soles_girasol = QTimer()
        self.timer_soles_girasol.setInterval(p.INTERVALO_SOLES_GIRASOL)
        self.timer_soles_girasol.timeout.connect(self.generar_sol_girasol)
        self.timer_soles_girasol.start()
        self.timers.append(self.timer_soles_girasol)
        self.timer_mordida = QTimer()
        self.timer_mordida.setInterval(p.INTERVALO_TIEMPO_MORDIDA)
        self.timer_mordida.timeout.connect(self.morder_planta)
        self.timers.append(self.timer_mordida)
        self.timer_movimiento_plantas = QTimer()
        self.timer_movimiento_plantas.setInterval(p.INTERVALO_MOVIMIENTO_PLANTAS)
        self.timer_movimiento_plantas.timeout.connect(self.mover_planta)
        self.timer_movimiento_plantas.start()
        self.timer_mensaje_final = QTimer()
        self.timer_mensaje_final.setInterval(p.TIEMPO_MENSAJE_FINAL)
        self.timer_mensaje_final.timeout.connect(self.pasar_ventana_post_ronda)
        self.timer_mensaje_final.setSingleShot(True)

    def pausar(self, pausar):
        if pausar:
            self.parar_timers()
            self.puedo_comprar_planta = False
        elif not pausar:
            for timer in self.timers:
                timer.start()
            self.puedo_comprar_planta = True

    def parar_timers(self):
        for timer in self.timers:
            timer.stop()

    def avanzar_ronda(self):
        self.soles -= p.COSTO_AVANZAR
        self.parar_timers()
        self.senal_esconder_ventana.emit()
        datos = {'ganador': True, 'ronda': str(self.ronda),
                'soles': str(self.soles),'zombies': 
                str(self.zombies_destruidos), 'puntaje ronda': 
                str(self.puntaje_ronda),'puntaje total': 
                str(self.puntaje_total)} 
        self.senal_mostrar_ventana_post_ronda.emit(datos)
        self.ronda += 1
        self.enviar_datos_iniciales()

    def guardar_puntaje(self):
        with open(p.RUTA_PUNTAJES, 'a', encoding='utf-8') as puntajes:
            texto = f'\n{self.usuario},{self.puntaje_total}'
            puntajes.write(texto) 