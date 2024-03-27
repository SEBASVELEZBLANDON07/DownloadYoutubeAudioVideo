# MediaMaster Extension

Esta es una extensión de Chrome que te permite descargar videos y audios de YouTube. Esta extensión se comunica con un servidor local en Python que maneja las descargas.

## Estructura del Repositorio

## DownloadYoutubeAudioVideo<br>
├── **ServidorPythonDownload**<br>
│   ├── [servidorDownload.py](ServidorPythonDownload/servidorDownload.py)<br>
│   └── [README.md](ServidorPythonDownload/README.md)<br>
├── **ExtencionChrome**<br>
│   ├── **MediaMasterExtension**<br>
│   │   ├── [background.js](ExtencionChrome/MediaMasterExtension/background.js)<br>
│   │   ├── [content.js](ExtencionChrome/MediaMasterExtension/content.js)<br>
│   │   ├── [icon128.png](ExtencionChrome/MediaMasterExtension/icon128.png)<br>
│   │   ├── [manifest.json](ExtencionChrome/MediaMasterExtension/manifest.json)<br>
│   │   └── [styles.css](ExtencionChrome/MediaMasterExtension/styles.css)<br>
│   └── [README.md](ExtencionChrome/README.md)<br>
└── [README.md](README.md)<br>


## Configuración y Uso

1. Clona este repositorio en tu máquina local.
2. Configura el servidor Python ejecutando el archivo `servidorDownload.py`.
3. Carga la extensión en Chrome siguiendo las instrucciones proporcionadas por Chrome Developer Documentation.





