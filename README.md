# Sistema de Control Distribuido con arquitecura Cliente Servidor
## Descripción General
Este proyecto implementa una arquitectura de red cliente-servidor basada en Sockets (TCP/IP) para el control remoto de actuadores en sistemas embebidos. El objetivo principal es establecer un enlace de comunicación robusto donde un cliente de escritorio (PC) envía comandos de control a un servidor central, el cual enruta dichas peticiones hacia un microcontrolador (ESP32) para modificar el estado físico de un LED.

## Arquitectura del Sistema
El sistema utiliza una topología en estrella donde el script de Python actúa como nodo central.

Servidor (Python): Actúa como broker de mensajes. Gestiona las conexiones entrantes, mantiene los sockets abiertos y retransmite los comandos recibidos desde la interfaz de usuario hacia el nodo IoT.

Cliente de Mando (Python): Interfaz de control. Permite al usuario enviar tramas de datos específicas (comandos) al servidor.

Nodo Actuador (ESP32 - C++): Cliente embebido. Mantiene una conexión persistente con el servidor vía WiFi, escucha comandos entrantes y ejecuta la lógica de control de hardware (GPIO) sobre el LED.

## Estructura del Repositorio
servidor.py: Código fuente del servidor. Implementa la creación del socket, el binding a la dirección IP/Puerto y el bucle de escucha para gestionar el tráfico de datos entre clientes.

cliente.py: Script de cliente para PC. Genera las tramas de control (ej. "ON", "OFF") y las transmite al servidor.

cliente2.ino: Firmware para el ESP32. Gestiona la pila TCP/IP del microcontrolador, la conexión a la red WiFi y la lógica de actuación sobre los pines de salida digital.

 
