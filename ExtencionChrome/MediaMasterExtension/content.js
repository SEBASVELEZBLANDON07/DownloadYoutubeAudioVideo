// Recibe los mensajes enviados por el archivo de backeground.js 
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    // Se verifica el tipo del mensaje 
    // Si es download_complete "un mensaje de descarga completa"
        if (message.type === 'download_complete') {
        // Se imprime en consola el mensaje de descarga completa 
        console.log("Descarga completa", message.data);

        // Verifica si el mensaje es un objeto y si contiene la propiedad "message"
        if (message.data && message.data.message) {
            // Se obtiene el mensaje del objeto
            var messageString = message.data.message;
            
            // Se envía una aleta al usuario indicando la descarga completa
            alert(messageString);
        }
    }
    // Si es error_download "un mensaje de error de descarga"
    else if (message.type === 'error_download'){
        // Se imprime en consola el error de la descarga 
        if (message.error && message.error.message) {
            console.log("Error en la descarga:", message.error.message);
        } else {
            console.log("Error en la descarga:", message.error);
        }
        //console.error("Error en la descarga:", message.error);

        // Se envía una aleta al usuario indicando un error de descarga
        alert("¡Error en el servidor!");
    }
});

// Función para agregar botones de descarga
function addButton() {
    // Busca el elemento del reproductor de YouTube
    var player = document.querySelector('.html5-main-video');

    // Si el reproductor existe, agrega el botón de descarga
    if (player) {
        // Crea el botón de descarga de video
        var downloadButtonVideo = document.createElement('button');
        downloadButtonVideo.innerText = 'Video';
        downloadButtonVideo.id = 'downloadButtonVideo';

        //Se envia un mensaje al archivo backhround.js cuando se hace clic en el botón de video
        downloadButtonVideo.addEventListener('click', function() {
            chrome.runtime.sendMessage({type: 'download_video', url: window.location.href});
        });

        // Crea el botón de descarga de audio
        var downloadButtonAudio = document.createElement('button');
        downloadButtonAudio.innerText = 'Audio';
        downloadButtonAudio.id = 'downloadButtonAudio';

        // Se envia un mensaje al archivo backhround.js cuando se hace clic en el botón de audio
        downloadButtonAudio.addEventListener('click', function() {
            chrome.runtime.sendMessage({type: 'download_audio', url: window.location.href});
        });

        // Se insertan los botton antes del reproductor de YouTube
        player.parentNode.insertBefore(downloadButtonVideo, player);
        player.parentNode.insertBefore(downloadButtonAudio, player);

    } else {
        console.log("No se encontró el reproductor de YouTube.");
    }
}

// Se verifica si chrome.runtime está definido antes de agregar el botón
if (typeof chrome.runtime !== 'undefined') {
    addButton();
} else {
    console.log("chrome.runtime no está definido.");
}
