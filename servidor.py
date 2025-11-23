import socket
import threading

IP = "0.0.0.0"   #cualquier red conectada al servidor
PORT = 5006
buffer_size= 1024
clients = []

def clientes(conn, addr):
    print(f"Nuevo cliente conectado: {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break

           
            msg = data.decode().strip()
            print(f"[{addr}] → {msg}")
            # Reenviar el mensaje a TODOS los clientes excepto el que lo manda
            for c in clients:
                if c is not conn:
                    c.sendall((msg + "\n").encode())

    except:
        pass

    print(f" Cliente desconectado: {addr}")
    clients.remove(conn)
    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)

print(f" Servidor escuchando en {PORT}...")

while True:
    conn, addr = server.accept()
    ##Nos sirve para handlear varios clientes a la
    thread = threading.Thread(target=clientes, args=(conn, addr))
    thread.start()