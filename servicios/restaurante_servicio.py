from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self):
        self.archivo = ArchivoServicio()

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_datos()

    # =========================
    # CARGAR DATOS
    # =========================

    def cargar_datos(self):
        productos_data = self.archivo.cargar(
            "productos.json"
        )

        usuarios_data = self.archivo.cargar(
            "usuarios.json"
        )

        ventas_data = self.archivo.cargar(
            "ventas.json"
        )

        self.productos = [
            Producto.from_dict(producto)
            for producto in productos_data
        ]

        self.usuarios = [
            Usuario.from_dict(usuario)
            for usuario in usuarios_data
        ]

        self.ventas = []

        for venta_data in ventas_data:
            venta = Venta.from_dict(
                venta_data,
                self.usuarios,
                self.productos
            )

            if venta is not None:
                self.ventas.append(venta)

    # =========================
    # GUARDAR DATOS
    # =========================

    def guardar_productos(self):
        datos = [
            producto.to_dict()
            for producto in self.productos
        ]

        return self.archivo.guardar(
            "productos.json",
            datos
        )

    def guardar_usuarios(self):
        datos = [
            usuario.to_dict()
            for usuario in self.usuarios
        ]

        return self.archivo.guardar(
            "usuarios.json",
            datos
        )

    def guardar_ventas(self):
        datos = [
            venta.to_dict()
            for venta in self.ventas
        ]

        return self.archivo.guardar(
            "ventas.json",
            datos
        )

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError(
                "El producto no es válido."
            )

        if not producto.nombre.strip():
            raise ValueError(
                "El nombre del producto es obligatorio."
            )

        if producto.precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        existe = any(
            p.nombre.lower() == producto.nombre.lower()
            for p in self.productos
        )

        if existe:
            raise ValueError(
                "El producto ya existe."
            )

        self.productos.append(producto)

        if not self.guardar_productos():
            self.productos.pop()

            raise OSError(
                "No se pudo guardar el producto."
            )

        return True

    def listar_productos(self):
        return self.productos

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError(
                "El usuario no es válido."
            )

        if not usuario.nombre.strip():
            raise ValueError(
                "El nombre del usuario es obligatorio."
            )

        existe = any(
            u.nombre.lower() == usuario.nombre.lower()
            for u in self.usuarios
        )

        if existe:
            raise ValueError(
                "El usuario ya existe."
            )

        self.usuarios.append(usuario)

        if not self.guardar_usuarios():
            self.usuarios.pop()

            raise OSError(
                "No se pudo guardar el usuario."
            )

        return True

    def listar_usuarios(self):
        return self.usuarios

    # =========================
    # LOGIN
    # =========================

    def validar_login(self, nombre):
        if not nombre or not nombre.strip():
            return False

        nombre = nombre.strip().lower()

        return any(
            usuario.nombre.lower() == nombre
            for usuario in self.usuarios
        )

    # =========================
    # VENTAS
    # =========================

    def registrar_venta(
        self,
        usuario,
        producto,
        fecha=None
    ):
        if usuario is None:
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if producto is None:
            raise ValueError(
                "Debe seleccionar un producto."
            )

        if fecha is None:
            fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        venta = Venta(
            usuario,
            producto,
            fecha
        )

        self.ventas.append(venta)

        if not self.guardar_ventas():
            self.ventas.pop()

            raise OSError(
                "No se pudo guardar la venta."
            )

        return venta

    def listar_ventas(self):
        return self.ventas