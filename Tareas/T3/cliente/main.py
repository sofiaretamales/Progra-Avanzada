import sys
from PyQt5.QtWidgets import QApplication
from backend.interfaz import Interfaz
from backend.cliente import Cliente
from funciones_utiles import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    try:
        app = QApplication(sys.argv)
        cliente = Cliente(HOST, PORT)
        interfaz = Interfaz()

        #Señales
    
        cliente.senal_mostrar_ventana_inicio.connect(
            interfaz.mostrar_ventana_inicio)

        interfaz.ventana_inicio.senal_enviar_login.connect(
            cliente.enviar)

        cliente.senal_manejar_mensaje.connect(
            interfaz.manejar_mensaje)

        interfaz.senal_login_rechazado.connect(
            interfaz.ventana_inicio.mostrar_error_usuario_invalido)

        interfaz.senal_sala_espera_llena.connect(
            interfaz.ventana_inicio.mostrar_error_sala_llena)

        interfaz.senal_actualizar_usuarios_sala_espera.connect(
            interfaz.ventana_espera.set_datos)

        interfaz.senal_comenzar_cuenta_regresiva.connect(
            interfaz.ventana_espera.comenzar_cuenta_regresiva)

        interfaz.ventana_espera.senal_abrir_sala_juego.connect(
            interfaz.mostrar_ventana_juego)

        interfaz.ventana_espera.senal_abrir_sala_inicio.connect(
            interfaz.ventana_inicio.mostrar)

        interfaz.ventana_espera.senal_borrar_jugador.connect(
            cliente.enviar)

        cliente.iniciar_cliente()

        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        sys.exit()