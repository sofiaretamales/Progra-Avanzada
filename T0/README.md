# Tarea 0: _Star Advanced_ :milky_way:

## Consideraciones generales :octocat:
* Los archivos ```parametros.py``` y ```tablero.py``` los dejé en .gitignore, pero es necesario que estén en la misma carpeta que ```main.py``` para ejecutarlo.
* El juego tiene 4 menús: el de inicio, el de juego, el que se muestra cuando el jugador gana, y el que se muestra cuando el jugador pierde y sólo a partir de ellos se puede salir del juego o regresar atrás, por lo tanto al comenzar o cargar una partida no se podrá retroceder hasta llegar al menú de juego (o sea que si o si tendrá que llenar los datos que se van pidiendo).
* En la carpeta ```partidas``` dejé el archivo ```usuario.txt``` con el formato en el cual se guardan los datos de la partida. Al igual que en el archivo ```puntajes.txt``` contenido en la carpeta ```puntajes```, en el cual dejé algunos puntajes guardados como referencia.

### Cosas implementadas y no implementadas :white_check_mark: :x:
A partir de la pauta que está en AvanzadaApp.
* Programación Orientada a Objetos
    * ✅Menú de inicio: Hecho completo (```main```, línea 8).
    * ✅Funcionalidades partida nueva: Hecho completo (```main```, línea 17).
    * ✅Funcionalidades cargar partida: Hecho completo (```main```, línea 33)
    * 🟠Salir programa: Incompleto. Se sale del juego, pero no de la consola (solo cierra el archivo ```main```) (se encuentra en ```main```, en todos los menús).
    * ✅Puntajes: Hecho completo (```main```, línea 53).
* Flujo del juego
    * ✅Menú de juego: Hecho completo (```main```, línea 65).
    * ✅Generar tablero: Hecho completo (```class_partida```, línea 22).
    * ✅Visualización tablero: Hecho completo (```main```, línea 69).
    * ✅Actualización tablero: Hecho completo (```class_partida```; línea 65, 117).
    * ✅Cálculo bestias: Hecho completo (```class_partida```, línea 36).
    * ✅Sector sin bestias: Hecho completo (```class_partida```, línea 79).
    * ✅Guardado automático: Hecho completo (```class_partida```, línea 138).
    * ✅Formato archivos partidas: Hecho completo (```class_partida```, línea 138).
* Fin del juego
    * ✅Fin juego (derrota): Hecho completo (```class_partida```, línea 57).
    * ✅Fin juego (victoria): Hecho completo (```class_partida```; línea 73, 120).
    * ✅Cálculo puntaje: Hecho completo (```class_partida```, línea 153).
    * ✅Guardar puntaje: Hecho completo (```class_partida```, línea 157).
* General
    * ✅Menús: Hecho completo (```main```; línea 8, 65, 107, 120).
    * ✅Parámetros: Hecho completo (```class_partida```; línea 3, 36, 155).
    * PEP8: En general cumple, pero no descarto que se me haya pasado algún espacio o algo así.
* ✅Bonus: Hecho completo (```class_partida```, línea 98).

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Se necesita que se descarguen los archivos ```class_partida.py```, ```funciones_utiles.py``` y las carpetas ```partidas``` y ```puntajes```.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path()```
2. ```sys```: ```exit()``` 
3. ```random```: ```randint()``` 
4. ```string```: ```ascii_uppercase()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```class_partida```: Contiene a la clase ```Partida```. Esta contiene el flujo del juego (menos el menú de juego).
2. ```funciones_utiles```: Contiene funciones para pedir inputs, ordenar el ranking y transformar listas a string y viceversa. En cada función dentro del archivo está explicado lo que hacen.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

* El nombre de usuario sólo recibe caracteres alfanuméricos.
* Cuando se quiere cargar otra partida y el nombre de usuario indicado no tiene una partida guardada, se regresa al menú de inicio.
* Cuando se guarde una partida y después al reanudarla el usuario termine la partida, esta seguirá guardada en la carpeta como checkpoint tal cual la había dejado, a no ser de que haya guardado la misma partida en otro punto o comience otra con el mismo nombre de usuario y la guarde.
* Cuando se muestra el ranking de puntajes, pueden repetirse los nombres de usuario con distinto puntaje. En caso de que dos usuarios tengan el mismo puntaje, se ubican en el ranking según orden en que se agregó al archivo. Para volver al menú de inicio, la consola dirá que presione ENTER, pero cualquier caracter sirve.
* Cuando se pida la coordenada a despejar, se pedirán dos inputs: primero el de la columna, que corresponde a una letra según el tablero impreso (puede ser en mayúscula o minúscula) y después la fila, que es un número.

PD: Al comienzo hay muchos commits innecesarios, perdón lo estaba aprendiendo a ocupar:c

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://www.askpython.com/python/examples/create-minesweeper-using-python: lo utilicé para implementar el módulo ```vecinos()``` (línea 88) y ```comprobar_ganador()``` (línea 110) en el archivo ```class_partida``` .  ```vecinos()``` es una función recursiva y cuenta cuántas bestias tienen alrededor las casillas vecinas de una casilla que no contiene bestias (cambié la forma de recorrer las casillas). ```comprobar_ganador()``` comprueba que si ya se descubrieron todas las casillas libres, el usuario gana.
