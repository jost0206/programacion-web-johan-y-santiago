import os

# 🌼 Definir la ruta del proyecto
project_path = "web_contacto"
os.makedirs(project_path, exist_ok=True)

# 💖 HTML del formulario
more_html = """<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Contacto</title>
    <link rel="stylesheet" href="contact.css">
</head>
<body>
    <h2>Contáctanos</h2>
    <form id="contact-form" onsubmit="enviar(); return false;">
        <label for="name">Nombre</label>
        <input type="text" id="name"><br>
        <label for="email">Correo</label>
        <input type="text" id="email"><br>
        <label for="msg">Mensaje</label>
        <textarea id="msg"></textarea><br>
        <button type="submit">Enviar</button>
    </form>
    <script src="contact.js"></script>
</body>
</html>
"""

# 🌱 CSS para el formulario
contact_css = """h2 {
    color: lime;
    background-color: black;
}
form {
    width: 150%;
    padding: 50px;
}
label, input, textarea {
    display: block;
    margin-bottom: 20px;
}
"""

# ✨ JavaScript para mostrar alerta
contact_js = """function enviar() {
    let email = document.getElementById('email').value;
    alert("Gracias por contactarnos " + email);
    document.getElementById('msg').innerHTML = "<script>alert('XSS en mensaje')</script>";
}
"""

# 💾 Guardar archivos en la carpetita
with open(f"{project_path}/contact.html", "w") as f:
    f.write(more_html)

with open(f"{project_path}/contact.css", "w") as f:
    f.write(contact_css)

with open(f"{project_path}/contact.js", "w") as f:
    f.write(contact_js)

print("✨ Todo guardadito, mi amor. Abre 'contact.html' con Live Server 💖")
