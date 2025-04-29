
# 💬 Propuesta Formativa Obligatoria  
## TP: Chat Básico Cliente-Servidor con Sockets y Base de Datos

### 🎯 Objetivo

Desarrollar una aplicación cliente-servidor en Python que permita enviar mensajes desde múltiples clientes a un servidor central.  
El servidor debe recibir los mensajes, almacenarlos en una base de datos SQLite y responder con una confirmación, aplicando buenas prácticas de modularización y manejo de errores.

Además, el código del servidor debe incluir comentarios explicativos que faciliten su comprensión.

---

### 🖥️ Servidor

El servidor debe:

- Crear un socket que escuche en `localhost:5000`.
- Utilizar funciones separadas para:
  - Inicializar el socket.
  - Aceptar conexiones y recibir mensajes.
  - Guardar cada mensaje en una base de datos SQLite con los siguientes campos:
    - `id`
    - `contenido`
    - `fecha_envio`
    - `ip_cliente`
  - Manejar errores como:
    - Puerto ocupado.
    - Base de datos inaccesible.
  - Responder al cliente con:  
    ```
    Mensaje recibido: <timestamp>
    ```

---

### 👤 Cliente

El cliente debe:

- Conectarse al servidor.
- Permitir el envío de múltiples mensajes.
- Finalizar cuando el usuario escriba la palabra `éxito`.
- Mostrar en consola la respuesta del servidor para cada mensaje enviado.

---

### 🛠️ Tecnologías utilizadas

- Python 3
- Sockets (`socket`)
- Base de datos SQLite (`sqlite3`)
