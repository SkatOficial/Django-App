function agregarAlCarrito(boton){
    boton.addEventListener('click', function() {
        const id_auto = this.dataset.id;
        const url = `/carrito/agregar/${id_auto}/`
        
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ id_auto: id_auto })
        })
        .then(response => response.json())
        .then(data => {
            if (data.agregado) {
                const stockElement = this.closest('.carta-galeria').querySelector('.stock-info');
                if (stockElement) {
                    stockElement.innerText = `Stock: ${data.stockVehiculos}`;
                } 
            } else {
                alert(data.message);  // Muestra un mensaje si hay un problema
            }
        })
        .catch(error => console.error('Error:', error));
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const botonesAgregar = document.querySelectorAll('[data-accion="agregarAlCarro"]');
    botonesAgregar.forEach(boton => {
        agregarAlCarrito(boton)
    });
});
