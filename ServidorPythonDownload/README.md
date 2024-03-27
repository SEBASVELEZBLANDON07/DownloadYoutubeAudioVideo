# Servidor de Descarga MediaMaster

Este es el servidor en Python que maneja las descargas de videos y audios de YouTube solicitadas por la extensión de Chrome "MediaMaster Extension".

## bibliotecas y módulos de Python

El servidor utiliza las siguientes bibliotecas y módulos de Python:

- `BaseHTTPRequestHandler` y `HTTPServer` del módulo `http.server`
- `YouTube` de `pytube`
- `Editor` de `moviepy.editor`
- `json`
- `os`
- `eyed3`
- `urllib.request`

## Configuración y Uso

1. **Asegúrate de tener Python 3.11.5 instalado en tu sistema.**
   - Descarga e instala Python desde [el sitio web oficial](https://www.python.org/downloads/) si aún no lo tienes instalado.

2. **Ejecuta el archivo `servidorDownload.py`.**
   - Abre una terminal o línea de comandos.
   - Navega hasta la ubicación del archivo `servidorDownload.py`.
   - Ejecuta el servidor utilizando el siguiente comando:
     ```bash
     python servidorDownload.py
     ```

3. **El servidor estará en funcionamiento en `localhost:8000`.**
   - Una vez que el servidor esté en ejecución, estará disponible en `http://localhost:8000`.

4. **Configuración de la Ruta de Almacenamiento:**
   - Dentro del archivo `servidorDownload.py`, asegúrate de especificar la ruta donde se almacenarán los archivos descargados. Puedes modificar la variable `folder` en el código para definir la ubicación deseada.

5. **Instalación de Bibliotecas y Módulos Necesarios:**
   - Asegúrate de tener instaladas las siguientes bibliotecas y módulos de Python:
     ```bash
     pip install pytube moviepy eyed3
     ```
   - Esto instalará las bibliotecas `pytube`, `moviepy` y `eyed3` necesarias para el funcionamiento del servidor.

6. **Conexión Automática de la Extensión de Chrome:**
   - La extensión de Chrome "MediaMaster Extension" se conectará automáticamente al servidor en `localhost:8000` para procesar las solicitudes de descarga.


## Rutas

- `/download_video`: Ruta para descargar videos de YouTube.
- `/download_audio`: Ruta para descargar audios de videos de YouTube.



