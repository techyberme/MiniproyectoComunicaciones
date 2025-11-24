import socket

SERVER_IP = "172.20.10.5"   # PC servidor
PORT = 5006
#conexión al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Conectado al servidor...")

try:
    while True:
        msg = ""
        #solo se pueden enviar estos mensajes
        while msg != "LED=ON" and msg != "LED=OFF" and msg != "ESTADO":
            msg = input("Comando a enviar (LED=ON / LED=OFF / ESTADO): ")
        #envío del mensaje
        client.sendall((msg + "\n").encode())

        # Recibir datos del servidor 
        data = client.recv(1024)
        if data:
            print("Servidor: ", data.decode().strip())

except KeyboardInterrupt:
    client.close()
