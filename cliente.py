import socket

SERVER_IP = "172.20.10.5"   # PC servidor
PORT = 5006

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Conectado al servidor...")

try:
    while True:
        msg = ""
        while msg != "LED=ON" and msg != "LED=OFF" and msg != "ESTADO":
            msg = input("Comando a enviar (LED=ON / LED=OFF / ESTADO): ")

        client.sendall((msg + "\n").encode())

        # Recibir datos del servidor (del ESP32)
        data = client.recv(1024)
        if data:
            print("Servidor: ", data.decode().strip())

except KeyboardInterrupt:
    client.close()
