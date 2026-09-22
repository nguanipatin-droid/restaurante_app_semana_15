class Venta:
    def __init__(self, usuario, producto, fecha):
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    def to_dict(self):
        return {
            "usuario": self.usuario.nombre,
            "producto": self.producto.nombre,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos, usuarios, productos):
        usuario = next(
            (u for u in usuarios if u.nombre == datos["usuario"]),
            None
        )

        producto = next(
            (p for p in productos if p.nombre == datos["producto"]),
            None
        )

        if usuario is None or producto is None:
            return None

        return cls(
            usuario,
            producto,
            datos["fecha"]
        )