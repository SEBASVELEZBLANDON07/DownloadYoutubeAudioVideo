// Recibe los mensajes enviados por el archivo de content.js
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
   
    //Se verifica el botton presionado
    //Si es el botton para descargar el video
    if (message.type === 'download_video') {
        //Se hace una solicitud POST al servidor local para descargar el video
        fetch("http://localhost:8000/download_video", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            // Se adjunta la URL de la página actual al servidor en el cuerpo de la solicitud 
            body: JSON.stringify({url: message.url})
        })
        .then(response => {
            // Respuesta de la solicitud
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Se devuelve los datos recibidos en formato JSON
            return response.json();
        })
        .then(data => {
            // Se envía un mensaje al archivo de content.js indicando que la descarga ha sido completada
            chrome.tabs.sendMessage(sender.tab.id, { type: 'download_complete', data: data });
        })
        .catch(error => {
            // Se envía un mensaje al archivo de content.js indicando que la descarga ha tenido un error 
            chrome.tabs.sendMessage(sender.tab.id, { type: 'error_download', error });
        });
    }
    //Si es el botton para descargar el audio
    else if (message.type === 'download_audio'){

        //Se hace una solicitud POST al servidor local para descargar el audio
        fetch("http://localhost:8000/download_audio", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            // Se adjunta la URL de la página actual al servidor en el cuerpo de la solicitud
            body: JSON.stringify({url: message.url})
        })
        .then(response => {
            // Respuesta de la solicitud
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Se devuelve los datos recibidos en formato JSON
            return response.json();
        })
        .then(data => {
            // Se envía un mensaje al archivo de content.js indicando que la descarga ha sido completada
            chrome.tabs.sendMessage(sender.tab.id, { type: 'download_complete', data: data });
        })
        .catch(error => {
            // Se envía un mensaje al archivo de content.js indicando que la descarga ha tenido un error 
            chrome.tabs.sendMessage(sender.tab.id, { type: 'error_download', error });
        });
    }
});
 