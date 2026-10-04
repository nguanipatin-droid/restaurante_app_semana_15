class Usuario:
    ROLES = ("Administrador", "Empleado", "Cliente")

    def __init__(
        self,
        identificador,
        nombre,
        correo,
        nombre_usuario,
        contrasena,
        rol="Cliente",
        activo=True
    ):
        self.identificador = str(identificador)
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.nombre_usuario = nombre_usuario.strip()
        self.contrasena = contrasena
        self.rol = rol
        self.activo = bool(activo)

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "correo": self.correo,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "rol": self.rol,
            "activo": self.activo
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            identificador=datos.get(
                "identificador",
                datos.get("id", "")
            ),
            nombre=datos.get("nombre", ""),
            correo=datos.get("correo", ""),
            nombre_usuario=datos.get("nombre_usuario", ""),
            contrasena=datos.get("contrasena", ""),
            rol=datos.get("rol", "Cliente"),
            activo=datos.get("activo", True)
        )