class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre_usuario}")
        print(f"Contraseña: {self.contrasena}")


usuario1 = Usuario("miguelina123", "clave123")
usuario1.mostrar_datos()

