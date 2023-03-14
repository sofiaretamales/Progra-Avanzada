import json
import socket
import threading
from logica import Logica
from cripto import encriptar, desencriptar

class Servidor:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("\nInicializando servidor...")
        self.sockets = {}
        self.lock_usuarios = threading.Lock()
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log(f'servidor escuchando...\nhost: {self.host}\nport: {self.port}')
        self.comenzar_a_aceptar()

    def comenzar_a_aceptar(self):
        thread = threading.Thread(target=self.aceptar_cliente, daemon=True)
        thread.start()

    def aceptar_cliente(self):
        while True: 
            try:
                with self.lock_usuarios:
                    socket_jugador, _ = self.socket_servidor.accept()
                    thread = threading.Thread(
                        target=self.escuchar_cliente,
                        args=(self.id_cliente, socket_jugador), daemon=True)
                    thread.start()
                    self.sockets[self.id_cliente] = socket_jugador
                    self.id_cliente += 1
            except ConnectionError:
                self.log("Ha ocurrido un error con la conexión")

    def escuchar_cliente(self, id_cliente, socket_cliente):
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        try:
            while True: 
                mensaje = self.recibir_mensaje(socket_cliente)
                respuesta = self.logica.procesar_mensaje(mensaje)
                if respuesta:
                    self.enviar_mensaje(respuesta, socket_cliente)
                    self.enviar_a_todos(respuesta)
        except ConnectionError: 
            self.log(f"Error al escuchar al cliente {id_cliente}")
            self.eliminar_cliente(id_cliente, socket_cliente)

    def enviar_a_todos(self, respuesta):
        if "usuarios" not in respuesta:
            return
        for socket in self.sockets:
            self.enviar_mensaje({"comando": "respuesta_actualizar_usuarios",
                                "usuarios": respuesta["usuarios"]}, self.sockets[socket])

    def recibir_mensaje(self, socket_cliente):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder='big')
        for _ in range(0, largo_mensaje, 32):
            socket_cliente.recv(4)
            bytes_mensaje += socket_cliente.recv(min(32, largo_mensaje - len(bytes_mensaje)))
        bytes_msg_desencriptado = desencriptar(bytes_mensaje)
        return self.decodificar_mensaje(bytes_msg_desencriptado)

    def enviar_mensaje(self, mensaje, socket_cliente):
        mensaje_codificado  = bytearray()
        bytes_mensaje = self.codificar_mensaje(mensaje)
        bytes_msg_encriptado = encriptar(bytes_mensaje)
        largo_mensaje = len(bytes_msg_encriptado).to_bytes(4, byteorder='big')
        mensaje_codificado += largo_mensaje
        for i in range(0, len(bytes_msg_encriptado), 32):
            chunk = bytearray(bytes_msg_encriptado[i:i+32])
            chunk = chunk.ljust(32, b"\0")
            largo_chunk = (i+1).to_bytes(4, byteorder='little')
            mensaje_codificado += largo_chunk
            mensaje_codificado += chunk
        #print('SE ENVIO EL MENSAJE', mensaje)
        socket_cliente.sendall(mensaje_codificado)
        
    def codificar_mensaje(self, mensaje):
        try:
            return json.dumps(mensaje).encode('utf-8')
        except json.JSONDecodeError:
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            return json.loads(mensaje_bytes)
        except json.JSONDecodeError:
            return dict()

    def eliminar_cliente(self, id_cliente, socket_cliente):
        try:
            self.log(f"El cliente {id_cliente} se ha desconectado")
            socket_cliente.close()
            self.sockets.pop(id_cliente, None)
            self.logica.eliminar_nombre(id_cliente)
            #self.enviar_a_todos()

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def log(self, mensaje):
        print("|" + mensaje.center(80, " ") + "|")