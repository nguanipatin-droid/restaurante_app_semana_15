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
    def from_dict(cls, datos):
        return cls(
            datos["nombre"],
            datos["precio"]
        )