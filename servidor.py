import socket
import sqlite3
from datetime import datetime

# Configuración del socket TCP/IP
def inicializar_socket():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('localhost', 5000))
        servidor.listen(5)
        print("Servidor escuchando en localhost:5000")
        return servidor
    except OSError as e:
        print("Error al iniciar el socket:", e)
        exit()

# Crear base de datos y tabla si no existe
def inicializar_db():
    try:
        conexion = sqlite3.connect("db_chat.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print("Error al acceder a la base de datos:", e)
        exit()

# Guardar mensaje en la base de datos
def guardar_mensaje(mensaje, ip):
    try:
        conexion = sqlite3.connect("db_chat.db")
        cursor = conexion.cursor()
        fecha_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (mensaje, fecha_envio, ip))
        conexion.commit()
        conexion.close()
        return fecha_envio
    except sqlite3.Error as e:
        print("Error al guardar mensaje:", e)

# Aceptar conexiones y procesar mensajes
def aceptar_conexiones(servidor):
    while True:
        cliente_socket, direccion = servidor.accept()
        print(f"Conexión establecida con {direccion}")
        while True:
            mensaje = cliente_socket.recv(1024).decode()
            if mensaje.lower() == "éxito":
                break
            timestamp = guardar_mensaje(mensaje, direccion[0])
            respuesta = f"Mensaje recibido: {timestamp}"
            cliente_socket.send(respuesta.encode())
        cliente_socket.close()
        print(f"Conexión cerrada con {direccion}")

# Punto de entrada
if __name__ == "__main__":
    inicializar_db()
    servidor = inicializar_socket()
    aceptar_conexiones(servidor)
