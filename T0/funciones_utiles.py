from string import ascii_uppercase
def pedir_input_int(rango): 
    """
    Recibe un input numérico restringido en un rango y 
    lo retorna como tipo int.
    """
    inp = input()
    if not inp.isdigit() or int(inp) not in rango:
        print('Por favor seleccione una opción válida:')
        inp = pedir_input_int(rango)
    return int(inp)

def pedir_input_letra(columna):
    """
    Recibe un input de una letra, restringida según su 
    posición en el abecedario y retorna la posición.
    """
    letra = input()
    if not letra.isalpha() or len(letra) != 1:
        print('Por favor seleccione una opción válida:')
        letra = pedir_input_letra(columna)
    else:
        lista_abc = list(ascii_uppercase)
        pos_letra = lista_abc.index(letra.upper())
        if pos_letra > columna:
            print('Por favor seleccione una opción válida')
            letra = pedir_input_letra(columna)
        return pos_letra

def ordenar_puntajes(lista):
    """
    Se utiliza como key en la función 'crear_ranking'.
    """
    return int(lista[1])

def crear_ranking(ruta):
    """
    Recibe una ruta como argumento y ordena de mayor
    a menor los diez mejores puntajes contenidos en el 
    archivo de la ruta en una lista y la retorna.
    """
    lista_puntajes = []
    with open(ruta, 'r', encoding='utf-8') as puntajes:
        for p in puntajes:
            puntaje = p.strip().split(',')
            lista_puntajes.append(puntaje)
    lista_puntajes.sort(key=ordenar_puntajes, reverse=True)
    if len(lista_puntajes) >= 10:
        return lista_puntajes[:10]
    else:
        return lista_puntajes

def lista_a_string(lista, filas):
    """
    Transforma una lista en un string 
    que comienza y termina con '/' y 
    lo retorna.
    """
    lista_en_str = '/'
    for fil in range(filas):
        fila_str = ','.join(map(str, lista[fil])) + ';'
        lista_en_str += fila_str
    lista_en_str = lista_en_str.rstrip(';') + '/'
    return lista_en_str

def string_a_lista(string):
    """
    Tranforma un string formado con el método
    'lista_a_sting' en una lista y la retorna.
    """
    lista = []
    filas = string.strip('/').split(';')
    for columnas in filas:
        columna = columnas.split(',')
        for c in range(len(columna)):
            if columna[c].isdigit():
                columna[c] = int(columna[c])
        lista.append(columna)
    return lista