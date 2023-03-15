# Diagrama de clases: DCCampeonato Programón :trophy:
### Relaciones
El programa cuenta de 11 clases que se relacionan de la siguiente forma:
* `LigaProgramon` se compone de `Entrenador` y `FlujoMenus`, ya que ambas dependen de la existencia del "mapa del juego" (un entrenador no existe si no existe el juego y el flujo de los menús dentro de él tampoco).
* `Entrenador` agrega a `Programon`, ya que un objeto de `Entrenador` tiene programones que compiten en representación de él y no son dependientes de la existencia del entrenador.
* `Programon` agrega a `Objetos`, ya que los objetos varían ciertos atributos del programón en una ronda, siendo independientes entre sí en términos de existencia.
* `Planta`, `Fuego`y `Agua` se heredan de `Programon`, ya que son tipos de programones.
* `Baya` y `Pocion` se heredan de `Objetos`, ya que son tipos de objetos.
* `Caramelo` se hereda de `Baya` y `Pocion`, ya que comparte los beneficios de ambas clases.

### Clases abstractas
* `Programon`
* `Objetos`

### Métodos abstractos
* `aplicar_objeto()` (clase `Objetos`): aplica los beneficios del objeto escogido al programón. Se implementa en `Baya`, `Pocion` con sus respectivos beneficios y estos después son heredados por `Caramelo`.
* `luchar()`(clase `Programon`): calcula el puntaje para cada tipo de programón (`Planta`, `Fuego`y `Agua`) dependiendo de la ventaja que tiene respecto a su rival.
* `ganar_batalla()` (clase `Programon`): dependiendo del tipo de programón, aplica un beneficio al ganar una batalla.

### Properties
* `vida` (clase `Programon`): Se implementa getter y setter para cuando la vida cambie en el intervalo válido ([1, 255]).
* `ataque` (clase `Programon`): Se implementa getter y setter para cuando el ataque cambie en el intervalo válido ([5, 190]).
* `defensa` (clase `Programon`): Se implementa getter y setter para cuando la defensa cambie en el intervalo válido ([5, 250]).
* `velocidad` (clase `Programon`): Se implementa getter y setter para cuando la defensa cambie en el intervalo válido ([5, 200]).
* `experiencia` (clase `Programon`): Se implementa getter y setter para cuando la defensa cambie en el intervalo válido ([0, 100]).
