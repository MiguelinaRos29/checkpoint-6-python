class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre_usuario}")
        print(f"Contraseña: {self.contraseña}")


# Crear objeto
usuario1 = Usuario("miguelina123", "claveSegura")

# Mostrar datos
usuario1.mostrar_datos()