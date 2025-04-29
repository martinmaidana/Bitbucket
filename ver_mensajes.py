import sqlite3

def mostrar_mensajes():
    try:
        conexion = sqlite3.connect("db_chat.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM mensajes")
        mensajes = cursor.fetchall()

        print("\n--- Mensajes Guardados ---\n")
        for msg in mensajes:
            print(f"ID: {msg[0]}")
            print(f"Contenido: {msg[1]}")
            print(f"Fecha de Envío: {msg[2]}")
            print(f"IP del Cliente: {msg[3]}")
            print("-" * 30)

        conexion.close()
    except sqlite3.Error as e:
        print("Error al leer la base de datos:", e)

if __name__ == "__main__":
    mostrar_mensajes()
