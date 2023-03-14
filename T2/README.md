# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:

## Consideraciones generales :octocat:
* Al momento de aparecer los zombies a partir de la función (ocupando el ponderador) noté que salían muy seguidos, asi que cuando hice el setInterval de ese timer, lo multipliqué para que sea más tiempo (línea 317 en el archivo ```logica_juego.py```).
* Para los cheatcodes (S+U+N y K+I+L), se presionan las teclas en secuencia sin considerar ningún tiempo, o sea que se podrían apretar las letras en distintos momentos cuando se esté jugando, pero siempre en ese orden.
* Cuando se sale del juego y se vuelve a la pantalla de inicio, si se comienza otro juego, el escenario seleccionado será el del juego anterior (estará presionado ese botón) y si se puede cambiar al otro.
* Los soles cuando aparecen, aparecen en lugares aleatorios de la pantalla de juego, pero no desaparecen, así que hay que ir recogiéndolos para que no se acumulen en la pantalla.
* Al momento de comprar una planta en medio de la partida, si se quiere poner en una posición en donde los zombies ya se comieron una planta, no se va a poder y aparecerá que la posición está ocupada.

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅Ventana de Ranking	
##### ✅Ventana principal
##### ✅Ventana de juego	
##### ✅Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅Plantas
##### ✅Zombies
##### ✅Escenarios		
##### ✅Fin de ronda	
##### ✅Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅Clicks	
##### 🟠Animaciones (me faltó hacer la de los zombies cuando están comiendo)
#### Cheatcodes: 8 pts (8%)
##### ✅Pausa
##### ✅S + U + N (para ambas: se presionan en secuencia)
##### ✅K + I + L
#### Archivos: 4 pts (4%)
##### ✅Sprites
##### ✅Parametros.py
#### Bonus: 9 décimas máximo
##### ❌Crazy Cruz Dinámico
##### ❌Pala
##### ❌Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Todo lo necesario está en la carpeta T2.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```QtWidgets```, ```QtCore```, ```QtGui```, ```uic```
2. ```sys```: ```exit```
3. ```math```: ```ceil```
4. ```random```: ```randint```, ```choice```, ```shuffle```
5. ```os```: ```path```
6. ```ABC```: ```abc```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

* ```ventana_inicio```: Contiene a ```VentanaInicio```
* ```ventana_prinicipal```: Contiene a ```VentanaPrincipal```
* ```ventana_juego```: Contiene a ```VentanaJuego```
* ```ventana_postjuego```: Contiene a ```VentanaPostRonda```
* ```ventana_ranking```: Contiene a ```VentanaRanking```
* ```logica_inicio```: Contiene a ```LogicaInicio```
* ```logica_principal```: Contiene a ```LogicaPrincipal```
* ```logica_juego```: Contiene a ```LogicaJuego```
* ```logica_ranking```: Contiene a ```LogicaRanking```
* ```elementos_juego```: Contiene a clases ```Plantas```, ```Zombies```, ```Guisantes```, ```Soles```, y sus respectivas sub-clases.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. La animación de la papa ocurre cuando se la están comiendo.
2. En la ventana post-ronda, si se perdió, queda deshabilitado el botón de avanzar, pero no dice ningún mensaje.
3. Los guisantes que no colisionan con ningún zombie, quedan al final de la pantalla estáticos, y si sale otro zombie, se detectará esa colisión.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/60549049/background-picture-in-qmainwindow-pyqt5 : Está implementado en el archivo <ventana_inicio.py> en las líneas 20-22 y este hace que el fondo de la ventana sea una imagen.
2. https://stackoverflow.com/questions/28720217/multiple-inheritance-metaclass-conflict/28727066#28727066: Lo implementé en el archivo <elementos_juego.py> para poder heredar las clases de ABC y QObject.
3. https://stackoverflow.com/questions/36686548/how-to-check-if-a-qpointf-is-in-a-qrect: Está implementado en el archivo <ventana_juego.py> en el método `mousePressEvent` (línea 184) y este ve si una posicion (en QPoint) está contenida en un botón (QRect), para comrpobar que se apretó ese botón.

