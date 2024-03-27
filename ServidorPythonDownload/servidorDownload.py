#importaciones 
from http.server import BaseHTTPRequestHandler, HTTPServer
from pytube import YouTube
from moviepy.editor import *
import json
import os 
import eyed3
import urllib.request

# Definición de la clase RequestHandler que hereda de BaseHTTPRequestHandler.
# Esta clase maneja las solicitudes HTTP recibidas por el servidor.
class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        # Se configuran las cabeceras de respuesta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')  
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        # Se manejan las solicitudes OPTIONS para CORS
        self._set_headers()

    def do_POST(self):
        # Se manejan las solicitudes POST
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Rutas del servidor 
        # Ruta para descargar video 
        if self.path == '/download_video':
            url = data['url']
            result = self.download_video(url)
        # Ruta para descargar el audio
        elif self.path == '/download_audio':
            url = data['url']
            result = self.download_audio(url)
        # Si se llama una ruta no existente 
        else:
            result = {"success": False, "error": "Invalid path"}

        # Se configuran las cabeceras de respuesta
        self._set_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))

    # Funcion para descargar videos de YouTube
    def download_video(self, url):
        try:
            # Descargar el video utilizando pytube
            
            # Ruta de la carpeta donde se almacenará el video
            folder = "../video/"
            youtube = YouTube(url)
            video = youtube.streams.get_highest_resolution()
            video.download(output_path=folder)
              
            print("video descragado exitosamente")
            
            # Se modifica la respuesta para incluir un mensaje de descarga completa
            result = {"success": True, "message": "¡Descarga del Video completa!"}
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    # Funcion para descargar el audio de los videos de YouTube
    def download_audio(self, url):
        try:
            # Descargar el audio utilizando pytube
            
            video = YouTube(url)
            titulo_video = video.title
            
            # Se genera el nombre de archivo
            
            # Si el título del video tiene un guion, el título no cambia 
            if "-" in titulo_video:
                nombreArchivo = titulo_video 
            # Si el título del video no tiene un guion, se agrega el nombre del autor 
            else:
                nombreArchivo = f"{titulo_video} - {video.author}"
            
            # Se reemplazan las barras diagonales dobles con guion bajo
            nombreArchivo = titulo_video.replace('//', '_') 

            # Se obtene la mejor calidad de audio disponible
            audio_streams = video.streams.filter(only_audio=True)
            audio = audio_streams.first()
            audio_file = audio.download(filename='temp_audio')
            
            # Ruta de la carpeta donde se almacenará el audio
            folder = "../music/"
            
            # Obtener la URL de la imagen de portada
            imagen_url = video.thumbnail_url
            
            # Descargar la imagen de portada
            imagen_filename = os.path.join(folder, nombreArchivo + ".jpg")
            # Verifica si existe una URL de imagen disponible.
            if imagen_url:
                try:
                    urllib.request.urlretrieve(imagen_url, imagen_filename)
                except Exception as e:
                    print("Error al descargar la imagen:", str(e))
            else:
                print("URL de imagen no disponible.")
            
            # Se converte a formato MP3
            mp4_file = AudioFileClip(audio_file)
            mp3_filename = os.path.join(folder, nombreArchivo + ".mp3")
            mp4_file.write_audiofile(mp3_filename)
            mp4_file.close()
            
            # Se adjunta la imagen de portada al archivo MP3
            audiofile = eyed3.load(mp3_filename)
            
            # Verifica si hay una imagen disponible para adjuntar
            # Si hay una imagen, la adjunta al archivo MP3
            if os.path.exists(imagen_filename): 
                audiofile.tag.images.set(3, open(imagen_filename,'rb').read(), 'image/jpeg')
                audiofile.tag.save()
            # Si no hay una imagen disponible
            else:
                print("No se encontró ninguna imagen para adjuntar al archivo MP3.")
                
            # Elimina el archivo de audio temporal e imagen de portada
            os.remove(audio_file)
            os.remove(imagen_filename)

            print("¡Audio descargado y convertido exitosamente como 'audio.mp3'!")
        
            # Se modifica la respuesta para incluir un mensaje de descarga completa
            result = {"success": True, "message": "¡Descarga del audio completa!"}
            return result
        
        except Exception as e:
            return {"success": False, "error": str(e)}

def run():
    # Se configura y ejecuta el servidor HTTP
    address = ('localhost', 8000)
    httpd = HTTPServer(address, RequestHandler)
    httpd.timeout = 180 
    print('Servidor HTTP iniciado en {}:{}'.format(*address))
    httpd.serve_forever()

# Se verifica si este script está siendo ejecutado directamente como el programa principal.
if __name__ == '__main__':
    # Se llama a la función 'run' para iniciar el servidor.
    run()
