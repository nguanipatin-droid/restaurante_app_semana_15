class Venta:
    def __init__(self, usuario, producto, fecha):
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            usuario=data.get("usuario", ""),
            producto=data.get("producto", ""),
            fecha=data.get("fecha", "")
        )