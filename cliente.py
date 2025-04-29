import socket

# Cliente TCP que se conecta a localhost:5000
def cliente_chat():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 5000))
    print("Conectado al servidor. Escribí tus mensajes (escribí 'éxito' para salir):")
    
    while True:
        mensaje = input("> ")
        cliente.send(mensaje.encode())
        if mensaje.lower() == "éxito":
            break
        respuesta = cliente.recv(1024).decode()
        print(respuesta)

    cliente.close()

if __name__ == "__main__":
    cliente_chat()
