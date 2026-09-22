class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def to_dict(self):
        return {
            "nombre": self.nombre
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(datos["nombre"])