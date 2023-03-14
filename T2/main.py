import sys
from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_principal import LogicaPrincipal
from backend.logica_juego import LogicaJuego
from backend.logica_ranking import LogicaRanking
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_postjuego import VentanaPostRonda

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_juego = VentanaJuego()
    ventana_ranking = VentanaRanking()
    ventana_postronda = VentanaPostRonda()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()
    logica_principal = LogicaPrincipal()
    logica_juego = LogicaJuego()
    logica_ranking = LogicaRanking()

    #Conexiones de señales
    '''Ventana de inicio y lógica inicio'''
    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_usuario)
    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion)
    logica_inicio.senal_abrir_ventana_principal.connect(
        ventana_principal.mostrar)
    ventana_inicio.senal_ver_ranking.connect(
        ventana_ranking.mostrar)
    logica_inicio.senal_enviar_usuario_a_juego.connect(
        logica_juego.recibir_usuario)
    
    '''Ventana principal y lógica principal'''
    ventana_principal.senal_verificar_eleccion.connect(
        logica_principal.comprobar_seleccion)
    logica_principal.senal_devolver_verificacion.connect(
        ventana_principal.recibir_verificacion)
    logica_principal.senal_abrir_juego.connect(
        ventana_juego.mostrar_fondo_elegido)

    '''Ventana juego y lógica juego'''
    ventana_juego.senal_pedir_datos_iniciales.connect(
        logica_juego.enviar_datos_iniciales)
    logica_juego.senal_cargar_datos_iniciales.connect(
        ventana_juego.setear_datos)
    ventana_juego.senal_iniciar_juego.connect(
        logica_juego.empezar_juego)
    logica_juego.senal_mostrar_zombies.connect(
        ventana_juego.aparecer_zombie)
    ventana_juego.senal_mover_zombie.connect(
         logica_juego.mover_zombie)
    logica_juego.senal_actualizar_pos_zombie.connect(
         ventana_juego.actualizar_posicion_zombie)
    logica_juego.senal_actualizar_datos_zombie.connect(
        ventana_juego.actualizar_datos_zombies)
    logica_juego.senal_cambiar_zombie_comiendo.connect(
        ventana_juego.cambiar_zombie_comiendo)
    ventana_juego.senal_comprobar_compra.connect(
        logica_juego.comprobar_compra_planta)
    logica_juego.senal_planta_aprobada.connect(
        ventana_juego.recibir_comprobacion_compra)
    logica_juego.senal_mover_planta.connect(
        ventana_juego.animar_planta)
    logica_juego.senal_actualizar_soles.connect(
        ventana_juego.actualizar_soles)
    logica_juego.senal_mostrar_proyectil.connect(
        ventana_juego.aparecer_guisante)
    logica_juego.senal_actualizar_proyectil.connect(
        ventana_juego.actualizar_disparo)
    logica_juego.senal_actualizar_label_sol.connect(
        ventana_juego.actualizar_label_sol)
    logica_juego.senal_esconder_label.connect(
        ventana_juego.esconder_label)
    ventana_juego.senal_sumar_soles.connect(
        logica_juego.sumar_sol)
    ventana_juego.senal_avanzar_ronda.connect(
        logica_juego.avanzar_ronda)
    ventana_juego.senal_abrir_ventana_inicio.connect(
        ventana_inicio.mostrar)
    ventana_juego.senal_pausar_juego.connect(
        logica_juego.pausar)
    logica_juego.senal_mostrar_ventana_post_ronda.connect(
        ventana_postronda.mostrar_ventana)
    logica_juego.senal_esconder_ventana.connect(
        ventana_juego.esconder)
    ventana_juego.senal_teclas.connect(
        logica_juego.recibir_senal_tecla)
    logica_juego.senal_mostrar_texto_final.connect(
        ventana_juego.mostrar_label_final)

    '''Ventana ranking y lógica ranking '''
    ventana_ranking.senal_crear_ranking.connect(
        logica_ranking.crear_ranking)
    ventana_ranking.senal_volver.connect(
        ventana_inicio.mostrar)
    logica_ranking.senal_enviar_datos.connect(
        ventana_ranking.actualizar_datos)

    '''Ventana post ronda'''
    ventana_postronda.senal_comenzar_otra_ronda.connect(
        ventana_juego.init_gui)
    ventana_postronda.senal_abrir_ventana_inicio.connect(
        ventana_inicio.mostrar)

    ventana_inicio.mostrar()
    app.exec()