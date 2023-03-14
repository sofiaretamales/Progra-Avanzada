from random import random, choice
from beautifultable import BeautifulTable

class Entrenador:
    
    def __init__(self, nombre, programones, energia, objetos):
        self.nombre = nombre
        self.programones = programones
        self.energia = energia
        self.objetos = objetos
        self.seguir = True

    def estado_entrenador(self, programones):
        tabla_estado = BeautifulTable()
        tabla_estado.rows.append(["Nombre", "Tipo", "Nivel", "Vida"])
        for programon in programones:
            tabla_estado.rows.append([programon.nombre, programon.tipo \
                                    , programon.nivel, programon.vida])
        tabla_estado.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
        titulo = BeautifulTable()
        titulo.columns.header = ["ESTADO DE ENTRENADOR"]
        titulo.rows.append(["Programones"])
        titulo.rows.append([tabla_estado])
        titulo.set_style(BeautifulTable.STYLE_NONE)
        titulo.border.top = "="
        titulo.columns.header.separator = "="
        titulo.rows.separator = "="
        print(titulo)
        

    def crear_objetos(self, objetos_de_tipo):
        objeto_asignado = choice(objetos_de_tipo)
        if self.energia >= objeto_asignado.costo:
            self.energia -= objeto_asignado.costo
            probabilidad = random()
            if probabilidad >= objeto_asignado.prob_exito:
                self.objetos.append(objeto_asignado.nombre)
                print(f"Se ha creado el objeto {objeto_asignado.nombre} con éxito!\n"
                f"Gasto de energía: {objeto_asignado.costo}\n"
                f"Tu energía pasó de {self.energia+objeto_asignado.costo} a"
                f" {self.energia}\nObjetos disponibles: {', '.join(self.objetos)}")
            elif probabilidad < objeto_asignado.prob_exito:
                print("Lo siento, la probabilidad no fue exitosa "
                    "y no se creó el objeto :(")
        elif self.energia < objeto_asignado.costo:
            print("Lo siento, no tienes suficiente energía para crear"
                  " un objeto:(")
