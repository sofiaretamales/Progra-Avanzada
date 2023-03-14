# Tarea 3: DCCard-Jitsu 🐧🥋

## Consideraciones generales :octocat:
En general, implementé la parte de networking y manejo de bytes solo para la ventana de inicio y de espera, por lo tanto no se puede jugar.
* La sala de espera tiene algunas fallas en consistencia, porque al momento de correr el código a veces no se actualiza la información para ambos clientes y otras veces sí (o si no se actualiza uno y el otro no). Noté que falla también después de que un cliente presiona "volver" y después ingresa de nuevo a la sala de espera (en algunas pruebas si funcionó). 

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### ✅ Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### 🟠 Consistencia 	
##### ✅ Logs 
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ✅ Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### 🟠 Sala de Espera 			
##### ❌ Ventana de juego							
##### ❌ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ❌ Inicio del juego			
##### ❌ Ronda				
##### ❌ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ❌ Cartas.py	
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ❌ Chat

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` de la carpetas ```servidor``` y ```cliente```.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```json```
2. ```socket```
3. ```threading```: ```Thread```
4. ```sys```: ```exit()```
5. ```PyQt5.QtWidgets```: ```QMessageBox```,  ```QApplication```
6. ```PyQt5.QtCore```: ```pyqtSignal```, ```QTimer```, ```QObject```
7. ```PyQt5.uic```
8. ```os.path```: ```join()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

#### Cliente
##### Backend
1. ```cliente.py```: Contiene a clase ```Cliente``` (inicia al cliente, recibe y envía mensajes).
2. ```interfaz.py```: Contiene a clase ```Interfaz``` (contiene a la lógica de las ventanas).
##### Frontend
1. ```funciones_utiles.py```: Contiene a función ```data_json``` (se utiliza durante la tarea para los parámetros en formato json).
2. ```ventana_inicio.py```: Contiene a clase ```VentanaInicio```.
3. ```ventana_espera.py```: Contiene a clase ```VentanaEspera```.
4. ```ventana_juego.py```: Contiene a clase ```VentanaJuego``` (no hay mucho código porque al ejecutar el juego, solo se alcanza a abrir esta ventana sin nada).

#### Servidor:
1. ```servidor.py```: Contiene a clase ```Servidor``` (recibe clientes, intercambio de mensajes).
2. ```logica.py```: Contiene a clase ```Logica```.
3. ```funciones_utiles.py```: Contiene a función ```data_json``` (se utiliza durante la tarea para los parámetros en formato json).

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
* Cuando ingresa un tercer cliente (3 o +), se da el aviso que la sala de espera está llena mediante la interfaz, pero este no ingresará automáticamente si se desocupa la sala de espera.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. AF3: función ```data_json``` (contenida en ```funciones_utiles.py``` del cliente y servidor). En general la estructura se basó en esta actividad.
