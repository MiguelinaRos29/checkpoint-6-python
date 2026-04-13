10. Ejercicio práctico
Enunciado

Crear una clase Usuario con nombre de usuario y contraseña usando __init__.

Solución

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre_usuario}")
        print(f"Contraseña: {self.contrasena}")


usuario1 = Usuario("miguelina123", "clave123")
usuario1.mostrar_datos()

