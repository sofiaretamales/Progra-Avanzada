from funciones_utiles import data_json
from PyQt5.QtCore import pyqtSignal
import threading

class Logica:

    senal_mostrar_tiempo = pyqtSignal

    def __init__(self, parent):
        self.parent = parent
        self.usuarios = {}
        self.jugadores = []
        self.lock_conectados = threading.Lock()

    def procesar_mensaje(self, mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar nombre":
            return self.verificar_nombre(mensaje["nombre"])
        elif comando == "borrar jugador": 
            nombre = mensaje["jugador"]
            self.log(f"{nombre} ha abandonado la sala de espera")
            id = list(self.usuarios.keys())[list(self.usuarios.values()).index(nombre)]
            self.usuarios.pop(id, nombre)
            self.jugadores.remove(nombre)
            return {"usuarios": self.jugadores}

    def verificar_nombre(self, nombre):
        with self.lock_conectados:
            self.log(f"Se ha ingresado el nombre de usuario: {nombre}")
            self.usuarios[self.parent.id_cliente - 1] = nombre
            cond_largo = 1 <= len(nombre) <= 10
            es_alnum = nombre.isalnum()
            repetido = nombre.lower() in self.jugadores
            sala_espera_llena = len(self.jugadores) == 2
            if cond_largo and es_alnum and not repetido and not sala_espera_llena:
                self.log(f"El nombre {nombre} es válido")
                self.jugadores.append(nombre.lower())
                if nombre.lower() == self.jugadores[0]:
                    self.log(f"{nombre} ingresó a la sala de espera")
                    self.log("La sala de espera aún no está llena")
                    return { "comando": "resp_verificar_nombre",
                                "estado": "aceptado",
                                "nombre": nombre,
                                "num_jugador": 1, 
                                "usuarios": self.jugadores}
                elif nombre.lower() == self.jugadores[1]:
                    self.log(f"{nombre} ingresó a la sala de espera")
                    self.log("La sala de espera está llena")
                    return { "comando": "resp_verificar_nombre",
                                "estado": "aceptado",
                                "nombre": nombre,
                                "num_jugador": 2,
                                "usuarios": self.jugadores}
            elif sala_espera_llena:
                self.log(f"{nombre} no ingresó a la sala de espera poqeue está llena")
                return { "comando": "resp_verificar_nombre",
                        "estado": "lleno",
                        "nombre": nombre}
            else:
                self.log(f"El nombre {nombre} no es válido")
                return {"comando": "resp_verificar_nombre",
                        "estado": "rechazado",
                        "error": "datos invalidos"}

    def eliminar_nombre(self, id):
        nombre = self.usuarios[id]
        self.usuarios.pop(id, nombre)
        self.jugadores.remove(nombre)

    def log(self, mensaje):
        print("|" + mensaje.center(80, " ") + "|")


