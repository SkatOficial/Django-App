function SumarACarrito(boton){
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
                const cantidadElement = this.closest('.fila-producto').querySelector('.cantidad-carrito');
                const precioTotalElement = this.closest('.fila-Producto').querySelector('.valor-total')
                const precioFinalElement = document.querySelector('.precio-final');

                if (cantidadElement && precioTotalElement && precioFinalElement) {
                    cantidadElement.innerText = `${data.cantidadCarrito}`;
                    precioTotalElement.innerText = `$${data.precioTotal}`;
                    precioFinalElement.innerText = `$${data.precioFinal}`;
                } 
            } else {
                alert(data.message);  
            }
        })
        .catch(error => console.error('Error:', error));
    });
}

function RestarACarrito(boton){
    boton.addEventListener('click', function() {
        const id_auto = this.dataset.id;
        const url = `/carrito/restar/${id_auto}/`
        
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
            if (data.restado) {
                const cantidadElement = this.closest('.fila-producto').querySelector('.cantidad-carrito');
                const precioTotalElement = this.closest('.fila-Producto').querySelector('.valor-total');
                const precioFinalElement = document.querySelector('.precio-final');

                const filaProductoElement = this.closest('.fila-Producto');
                const tablaBodyCarritoElement = this.closest('.tabla-body-carrito');
                const tablaBodyPrecioFinalElement = document.querySelector('.tabla-body-precio-final');

                if(data.cantidadCarrito == 0){//Elimina la fila entera del producto
                    filaProductoElement.remove();
                    precioFinalElement.innerText = `$${data.precioFinal}`;
                    if(tablaBodyCarritoElement.children.length === 0){
                        tablaBodyCarritoElement.innerHTML = `
                            <tr>
                                <td colspan="8">
                                    <div class="alert alert-danger text-center">
                                        Sin productos
                                    </div>
                                </td>
                            </tr>
                        `;
                        tablaBodyPrecioFinalElement.innerHTML =`
                        <tr>
                            <td>No se registran productos</td>
                        </tr>
                        ` 
                    }
                }else if(cantidadElement && precioTotalElement && precioFinalElement){
                    cantidadElement.innerText = `${data.cantidadCarrito}`;
                    precioTotalElement.innerText = `$${data.precioTotal}`;
                    precioFinalElement.innerText = `$${data.precioFinal}`;
                } 
            } else {
                alert(data.message);  
            }
        })
        .catch(error => console.error('Error:', error));
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const botonesSumar = document.querySelectorAll('[data-accion="sumar"]');
    const botonesRestar = document.querySelectorAll('[data-accion="restar"]');
    
    botonesSumar.forEach(boton => {
        SumarACarrito(boton);
    });

    botonesRestar.forEach(boton => {
        RestarACarrito(boton);
    });
    

});