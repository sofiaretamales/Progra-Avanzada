from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from backend.elementos_juego import PlantaPatata
import parametros as p

class VentanaJuego(QMainWindow):

    senal_pedir_datos_iniciales = pyqtSignal()
    senal_iniciar_juego = pyqtSignal(str)
    senal_aparecer_zombie = pyqtSignal()
    senal_mover_zombie = pyqtSignal()
    senal_comprobar_compra = pyqtSignal(tuple)
    senal_avanzar_ronda = pyqtSignal()
    senal_sumar_soles = pyqtSignal()
    senal_pausar_juego = pyqtSignal(bool)
    senal_abrir_ventana_inicio = pyqtSignal()
    senal_mostrar_ventana_post_ronda = pyqtSignal(dict)
    senal_teclas = pyqtSignal(str)
    senal_mostrar_ventana_post_ronda = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.fondo = None

    def mostrar_fondo_elegido(self, fondo):
        if fondo == 'abuela':
            uic.loadUi(p.RUTA_VENTANA_JUEGO_DIA, self) 
            self.fondo = 'abuela'
        elif fondo == 'nocturno':
            uic.loadUi(p.RUTA_VENTANA_JUEGO_NOCTURNO, self) 
            self.fondo = 'nocturno'
        self.boton_iniciar.clicked.connect(self.enviar_empezar_juego)
        self.boton_avanzar.clicked.connect(self.avanzar_ronda)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_pausa.clicked.connect(self.pausar_juego)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")
        self.casillas = [self.casilla_1, self.casilla_2, 
                        self.casilla_3, self.casilla_4,
                        self.casilla_5, self.casilla_6,
                        self.casilla_7, self.casilla_8,
                        self.casilla_9, self.casilla_10,
                        self.casilla_11, self.casilla_12,
                        self.casilla_13, self.casilla_14,
                        self.casilla_15, self.casilla_16,
                        self.casilla_17, self.casilla_18,
                        self.casilla_19, self.casilla_20]
        self.click_izquierdo_apretado = False
        self.en_partida = False
        self.planta_a_comprar = None
        self.juego_pausado = False
        self.soles_aparecidos = []
        self.labels_elementos = []
        self.show()
        self.senal_pedir_datos_iniciales.emit()

    def setear_datos(self, datos):
        self.setear_label(self.soles_disponibles, datos['soles'])
        self.setear_label(self.nivel, datos['ronda'])
        self.setear_label(self.costo_girasol, datos['costo girasol'])
        self.setear_label(self.costo_pclasica, datos['costo clasica'])
        self.setear_label(self.costo_phielo, datos['costo hielo'])
        self.setear_label(self.costo_patata, datos['costo papa'])
        self.setear_label(self.z_destruidos, datos['zombies destruidos'])
        self.setear_label(self.z_restantes, datos['zombies restantes'])
        self.setear_label(self.puntaje, datos['puntaje'])

    def enviar_empezar_juego(self):
        self.boton_iniciar.setEnabled(False)
        self.en_partida = True
        self.senal_iniciar_juego.emit(self.fondo)

    def aparecer_zombie(self, zombie):
        zombie.label.setParent(self)
        zombie.label.setVisible(True)
        self.senal_mover_zombie.emit()
        self.labels_elementos.append(zombie.label)

    def actualizar_posicion_zombie(self, tupla):
        zombie = tupla[0]
        pos_x = tupla[1]
        pos_y = tupla[2]
        if zombie.frame_caminando == 1:
            zombie.label.setPixmap(zombie.pixmap_caminando_2)
            zombie.frame_caminando += 1
        elif zombie.frame_caminando == 2:
            zombie.label.setPixmap(zombie.pixmap_caminando_1)
            zombie.frame_caminando -= 1
        zombie.label.move(pos_x, pos_y)

    def cambiar_zombie_comiendo(self, zombie):
        if zombie.frame_comiendo == 0:
            zombie.label.setPixmap(zombie.pixmap_comiendo_1)
        elif zombie.frame_comiendo == 1:
            zombie.label.setPixmap(zombie.pixmap_comiendo_2)
        elif zombie.frame_comiendo == 2:
            zombie.label.setPixmap(zombie.pixmap_comiendo_3)

    def actualizar_datos_zombies(self, datos):
        self.z_destruidos.setText(datos['zombies destruidos'])
        self.z_restantes.setText(datos['zombies restantes'])
        self.puntaje.setText(datos['puntaje'])
        self.z_destruidos.repaint()
        self.z_restantes.repaint()
        self.puntaje.repaint()

    def recibir_comprobacion_compra(self, tupla):
        pude_comprar = tupla[0]
        planta = tupla[1]
        error = tupla[2]
        if pude_comprar:
            self.mostrar_planta(planta)
        elif not pude_comprar:
            if error == 'soles insuficientes':
                mensaje = 'Lo siento, no tienes suficientes soles:('
                QMessageBox.about(self, 'Compra inválida', mensaje)
            elif error == 'pos ocupada':
                mensaje = 'Lo siento, esa posición ya está ocupada:('
                QMessageBox.about(self, 'Compra inválida', mensaje)

    def mostrar_planta(self, planta):
        planta.label.setParent(self)
        planta.label.setVisible(True)
        self.labels_elementos.append(planta.label)

    def animar_planta(self, planta):
        if planta.frame == 1:
            planta.label.setPixmap(planta.pixmap_2)
            planta.frame += 1
        elif planta.frame == 2:
            planta.label.setPixmap(planta.pixmap_3)
            planta.frame += 1
        elif planta.frame == 3:
            if not isinstance(planta, PlantaPatata):
                planta.label.setPixmap(planta.pixmap_1)
                planta.frame -= 2

    def aparecer_guisante(self, guisante):
        guisante.label.setParent(self)
        guisante.label.setVisible(True)
        self.labels_elementos.append(guisante.label)

    def actualizar_disparo(self, tupla):
        guisante = tupla[0]
        pos_x = tupla[1]
        pos_y = tupla[2]
        if guisante.frame == 1:
            guisante.label.setPixmap(guisante.pixmap_2)
            guisante.frame += 1
        elif guisante.frame == 2:
            guisante.label.setPixmap(guisante.pixmap_3)
            guisante.frame += 1
        elif guisante.frame == 3:
            guisante.label.setPixmap(guisante.pixmap_1)
            guisante.frame -= 2
        guisante.label.move(pos_x, pos_y)

    def actualizar_soles(self, soles):
        self.soles_disponibles.setText(str(soles))
        self.soles_disponibles.repaint()
        
    def actualizar_label_sol(self, tupla):
        sol = tupla[0]
        pos_x = tupla[1]
        pos_y = tupla[2]
        sol.label.setParent(self)
        sol.label.setVisible(True)
        sol.label.move(pos_x, pos_y)
        self.soles_aparecidos.append(sol)
        self.labels_elementos.append(sol.label)

    def setear_label(self, label, texto):
        label.setText(texto)
        label.repaint()

    def esconder_label(self, tupla_con_objeto):
        objeto = tupla_con_objeto[0]
        objeto.label.hide()

    def mousePressEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            pos = evento.pos()
            if not self.click_izquierdo_apretado:
                self.click_izquierdo_apretado = True
                if self.boton_girasol.geometry().contains(pos): 
                    self.planta_a_comprar = 'girasol'
                elif self.boton_planta_clasica.geometry().contains(pos):
                    self.planta_a_comprar = 'clasica'
                elif self.boton_planta_hielo.geometry().contains(pos):
                    self.planta_a_comprar = 'hielo'
                elif self.boton_patata.geometry().contains(pos):
                    self.planta_a_comprar = 'patata'
                else:
                    self.click_izquierdo_apretado = False
            elif self.click_izquierdo_apretado:
                for casilla in self.casillas:
                    if casilla.geometry().contains(pos):
                        pos = casilla.pos()
                        self.senal_comprobar_compra.emit((self.planta_a_comprar, pos))
                self.click_izquierdo_apretado = False
        elif evento.button() == Qt.RightButton:
            pos = evento.pos()
            for sol in self.soles_aparecidos:
                if sol.label.geometry().contains(pos):
                    self.senal_sumar_soles.emit()
                    sol.label.hide()

    def keyPressEvent(self, evento):
        if evento.key() == Qt.Key_P:
            self.pausar_juego()
        if evento.key() == Qt.Key_S:
            self.s_presionada = True
        if evento.key() == Qt.Key_U and self.s_presionada:
            self.u_presionada = True
        if evento.key() == Qt.Key_N and self.s_presionada and self.u_presionada:
            self.senal_teclas.emit('sun')
            self.s_presionada = False
            self.u_presionada = False
        if evento.key() == Qt.Key_K:
            self.k_presionada = True
        if evento.key() == Qt.Key_I and self.k_presionada:
            self.i_presionada = True
        if evento.key() == Qt.Key_L and self.k_presionada and self.i_presionada:
            self.senal_teclas.emit('kil')
            self.k_presionada = False
            self.i_presionada = False

    def avanzar_ronda(self):
        if int(self.soles_disponibles.text()) > p.COSTO_AVANZAR:
            self.senal_avanzar_ronda.emit()
            self.boton_iniciar.setEnabled(True)

    def pausar_juego(self):
        if not self.juego_pausado:
            self.juego_pausado = True
            self.senal_pausar_juego.emit(True)
        elif self.juego_pausado:
            self.juego_pausado = False
            self.senal_pausar_juego.emit(False)

    def mostrar_label_final(self, resultado):
        label_texto = QLabel('')
        if resultado == 'ganador':
            pixmap_texto = QPixmap(p.RUTA_TEXTO_GANADOR)
            label_texto.setPixmap(pixmap_texto)
            label_texto.setScaledContents(True)
            label_texto.resize(p.ANCHO_TEXTO_GANADOR, p.ALTO_TEXTO_GANADOR)
            label_texto.move(p.POS_X_TEXTO_GANADOR, p.POS_Y_TEXTO_GANADOR)
        elif resultado == 'perdedor':
            pixmap_texto = QPixmap(p.RUTA_TEXTO_PERDEDOR)
            label_texto.setPixmap(pixmap_texto)
            label_texto.setScaledContents(True)
            label_texto.resize(p.ANCHO_TEXTO_PERDEDOR, p.ALTO_TEXTO_PERDEDOR)
            label_texto.move(p.POS_X_TEXTO_PERDEDOR, p.POS_Y_TEXTO_PERDEDOR)
        label_texto.setParent(self)
        label_texto.setVisible(True)
        
    def esconder(self):
        self.hide()
        self.boton_iniciar.setEnabled(True)
        for label in self.labels_elementos:
            label.hide()

    def salir(self):
        self.senal_abrir_ventana_inicio.emit()
        self.senal_pausar_juego.emit(True)
        self.close()