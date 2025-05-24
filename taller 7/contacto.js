function enviar() {
    let nombre = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let mensaje = document.getElementById('msg').value;

    alert("Gracias por contactarnos, " + nombre + " (" + email + ")");
    document.getElementById('respuesta').textContent = "Su mensaje será tenido en cuenta. " + mensaje;
}
