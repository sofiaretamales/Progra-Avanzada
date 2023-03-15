from collections import namedtuple
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    #debe retornar lista de namedtupled
    with open(ruta_archivo, "rt") as archivo:
        platos = archivo.readlines()
    lista_platos= []
    for p in platos:
        plato_n= p.strip().split(',') 
        lista_platos.append(plato_n)
    for i in lista_platos:
        i[4]=set(i[4].split(';'))
    lista_con_tuplas=[]
    tupla_plato=namedtuple('Plato', 
    ['nombre', 'categoria', 'tiempo', 'precio','ingredientes'])
    for k in range(len(lista_platos)-1):
        lista_con_tuplas.append(tupla_plato(lista_platos[k][0], lista_platos[k][1], 
        int(lista_platos[k][2]), int(lista_platos[k][3]), lista_platos[k][4]))
    return lista_con_tuplas
     
    


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    #llave: ingrediente ; valor=cantidad
    with open(ruta_archivo, "rt") as archivo:
        ingredientes = archivo.readlines()
    lista_archivo=[]
    for i in ingredientes:
        ing= i.strip().split(',')
        lista_archivo.append(ing)
    diccionario={}
    for l in lista_archivo:
        diccionario[l[0]]=int(l[1])
    return diccionario
