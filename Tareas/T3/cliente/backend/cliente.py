from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread
from cripto import encriptar, desencriptar

class Cliente(QObject):

    senal_mostrar_ventana_inicio = pyqtSignal()
    senal_manejar_mensaje = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False

    def iniciar_cliente(self):
        try:
            self.socket.connect((self.host, self.port))
            self.conectado = True
            self.empezar_escuchar()
            self.senal_mostrar_ventana_inicio.emit()
        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

    def empezar_escuchar(self):
            thread_escuchar = Thread(target=self.escuchar_servidor, daemon=True)
            thread_escuchar.start()

    def escuchar_servidor(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje != {}:
                    #print('mensaje recibido:', mensaje)
                    self.senal_manejar_mensaje.emit(mensaje)
        except ConnectionError:
            print('Error de conexión con el servidor')

    def enviar(self, mensaje):
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
        self.socket.sendall(mensaje_codificado)

    def recibir(self):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = self.socket.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder='big')
        for _ in range(0, largo_mensaje, 32):
            self.socket.recv(4)
            bytes_mensaje += self.socket.recv(min(32, largo_mensaje - len(bytes_mensaje)))
        bytes_msg_desencriptado = desencriptar(bytes_mensaje)
        msg_decodificado = self.decodificar_mensaje(bytes_msg_desencriptado)
        return msg_decodificado

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

    def log(self, mensaje):
        print("|" + mensaje.center(80, " ") + "|")





        

