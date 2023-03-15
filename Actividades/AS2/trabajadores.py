from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):

    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        #Completar
        super().__init__()
        self.daemon = True

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        # Completar
        mensaje = "comenzó a trabajar..."
        self.log(mensaje)
        while self.energia > 0: 
            self.oro += ORO_RECOLECTADO
            mensaje_oro = f"recolectó {ORO_RECOLECTADO} monedas de oro"
            self.log(mensaje_oro)
            self.energia -= 1
            sleep(TIEMPO_RECOLECCION)

    def ingresar_oro(self) -> None:
        # Completar
        with self.centro_urbano.lock_oro:
            self.centro_urbano.oro += self.oro
            self.oro = 0
            self.log("depositó el oro en el centro urbano")
            msj = f"hay {self.centro_urbano.oro} unidades de oro en el centro urbano"
            self.log(msj)

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):

    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        #Completar
        super().__init__()
        self.daemon = True

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        # Completar
        with self.centro_urbano.lock_oro:
            if self.centro_urbano.oro >= ORO_CHOZA:
                self.centro_urbano.oro -= ORO_CHOZA
                msj = f"hay {self.centro_urbano.oro} de oro en el centro urbano"
                self.log(msj)
                return True
            elif self.centro_urbano.oro < ORO_CHOZA:
                msj = "no encontró suficiente oro en el centro urbano"
                self.log(msj)
                return False

    def construir_choza(self) -> None:
        # Completar
        with self.centro_urbano.lock_chozas:
            self.centro_urbano.chozas += 1
            msj = ("agregó una choza al centro urbano, ahora hay "
                   f"{self.centro_urbano.chozas} chozas")
            self.log(msj)
