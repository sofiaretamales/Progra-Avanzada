# Tarea 1: DCCampeonato 🏃‍♂️🏆

## Consideraciones generales :octocat:
* El flujo de los menús se hace mediante la clase FlujoMenus (en `Menus.py`) y para cuando se solicite ver el resumen del campeonato y ver el estado del entrenador, no se podrá volver al menú de inicio o salir desde allí, sino que vuelve al menú de entrenador (pide presionar ENTER, pero serviría poner cualquier input).
* Siempre los participantes que aparecen en el resumen del campeonato serán los 16 entrenadores que están en el archivo `entrenadores.csv`.
* Para simular las rondas, se guarda la información de cada ronda en el archivo `guardar_ronda.txt` (entrenadores que avanzan a la siguiente ronda, los que perdieron y el número de ronda). Este archivo está en la carpeta del repositorio y quedó escrito en él la información de una prueba que hice (se me olvidó limpiarlo ups).
* Los atributos de `Programon`: vida, ataque, defensa, velocidad y experiencia son properties para que no se pasen de los límites establecidos, pero cuando se modifican estos y llegan a su máx/mmín no se avisa nada en la consola y se quedan en el valor límite, entonces si se sigue sumando después, se quedará así (excepto `experiencia` que avisa que se subió de nivel).

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama 
##### ✅ Definición de clases, atributos, métodos y properties (en archivos `LigaProgramon.py`, `Menus.py`, `Entrenador.py`, `Programon.py`, `Objetos.py`)	
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	(en menú inicio)
##### ✅Menú de Inicio (`Menus.py`, linea 15)
##### ✅Menú Entrenador (`Menus.py`, linea 38)
##### ✅ Menu Entrenamiento (`Menus.py`, linea 105)
##### ✅ Simulación ronda campeonato (`LigaProgramon.py`, linea 28)
##### ✅Ver estado del campeonato (`LigaProgramon.py`, linea 12)
##### ✅ Menú crear objeto (`Menus.py`, linea 125)
##### ✅ Menú utilizar objeto (`Menus.py`, linea 142)
##### ✅ Ver estado del entrenador (`Entrenador.py`, linea 13)
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se debe crear nada más, todos los archivos necesarios están en la carpeta `T1`.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```, ```random()```, ```choice()```
2. ```beautifultable```: ```BeatifulTable()``` (debe instalarse)
3. ```os```: ```path()```
4. ```sys```: ```exit()```
5. ```abc```: ```ABC```, ```abstractmethod```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones_utiles```: Contiene a las funciones que abren los archivos .csv y que piden inputs.
2. ```Menus```: Contiene a la clase `FlujoMenus`, en donde están todos los menús pedidos.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Cuando un programón esté en el nivel 100 y se selecciona la opción de entrenarlo, el entrenador no va a perder energía, en ese caso sólo se avisa en consola que ya alcanzó su máximo nivel.


