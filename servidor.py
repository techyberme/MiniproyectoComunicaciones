import socket
import threading

IP = "0.0.0.0"   #cualquier red conectada al servidor
PORT = 5006
buffer_size= 1024
clients = []
#Función de manejo de cliente
def clientes(conn, addr):
    print(f"Nuevo cliente conectado: {addr}")
    #añade el nuevo cliente a la lista
    clients.append(conn)
    try:
        while True:
            data = conn.recv(buffer_size)   #recepción de datos
            if not data:
                break

           #decodificado del mensaje
            msg = data.decode().strip()
            print(f"[{addr}] → {msg}")
            # Reenviar el mensaje a TODOS los clientes excepto el que lo manda
            for c in clients:
                if c is not conn:
                    c.sendall((msg + "\n").encode())

    except:
        pass
    #rutina de desconexión
    print(f" Cliente desconectado: {addr}")
    clients.remove(conn)  #se quita el cliente de la lista y se cierra la conexión.
    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))  #se crea el servidor en la red
server.listen(5)

print(f" Servidor escuchando en {PORT}...")

while True:
    conn, addr = server.accept()
    ##Nos sirve para handlear varios clientes a la
    thread = threading.Thread(target=clientes, args=(conn, addr))
    thread.start()
