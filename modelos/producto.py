class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = float(precio)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data.get("nombre", ""),
            precio=data.get("precio", 0.0)
        )