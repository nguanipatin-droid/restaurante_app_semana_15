from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        self.path_productos = "datos/productos.json"
        self.path_usuarios = "datos/usuarios.json"
        self.path_ventas = "datos/ventas.json"

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_datos()

        # Si no existen usuarios, crear un administrador inicial
        if not self.usuarios:
            self._crear_administrador_inicial()

    # ==========================================================
    # CARGA DE DATOS
    # ==========================================================

    def cargar_datos(self):
        self.productos = self.obtener_productos()
        self.usuarios = self.obtener_usuarios()
        self.ventas = self.obtener_ventas()

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def obtener_productos(self):
        datos = ArchivoServicio.cargar_json(self.path_productos)

        return [
            Producto.from_dict(dato)
            for dato in datos
        ]

    def guardar_productos(self):
        ArchivoServicio.guardar_json(
            self.path_productos,
            [
                producto.to_dict()
                for producto in self.productos
            ]
        )

    def registrar_producto(self, nombre, precio_str):
        nombre = nombre.strip()

        if not nombre:
            raise ValueError(
                "El nombre del producto no puede estar vacío."
            )

        try:
            precio = float(precio_str)
        except ValueError:
            raise ValueError(
                "El precio debe ser un número válido."
            )

        if precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        if any(
            producto.nombre.lower() == nombre.lower()
            for producto in self.productos
        ):
            raise ValueError(
                "El producto ya se encuentra registrado."
            )

        nuevo_producto = Producto(
            nombre,
            precio
        )

        self.productos.append(nuevo_producto)
        self.guardar_productos()

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def obtener_usuarios(self):
        datos = ArchivoServicio.cargar_json(
            self.path_usuarios
        )

        return [
            Usuario.from_dict(dato)
            for dato in datos
        ]

    def guardar_usuarios(self):
        ArchivoServicio.guardar_json(
            self.path_usuarios,
            [
                usuario.to_dict()
                for usuario in self.usuarios
            ]
        )

    def _crear_administrador_inicial(self):
        administrador = Usuario(
            identificador="1",
            nombre="Administrador",
            correo="admin@restaurante.local",
            nombre_usuario="admin",
            contrasena="123456",
            rol="Administrador",
            activo=True
        )

        self.usuarios.append(administrador)
        self.guardar_usuarios()

    def siguiente_identificador(self):
        if not self.usuarios:
            return "1"

        identificadores = []

        for usuario in self.usuarios:
            try:
                identificadores.append(
                    int(usuario.identificador)
                )
            except (ValueError, TypeError):
                pass

        if not identificadores:
            return "1"

        return str(max(identificadores) + 1)

    def registrar_usuario(
        self,
        nombre,
        correo,
        nombre_usuario,
        contrasena,
        rol="Cliente"
    ):
        nombre = nombre.strip()
        correo = correo.strip()
        nombre_usuario = nombre_usuario.strip()

        if not nombre:
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo:
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if not nombre_usuario:
            raise ValueError(
                "El nombre de usuario no puede estar vacío."
            )

        if not contrasena:
            raise ValueError(
                "La contraseña no puede estar vacía."
            )

        if rol not in Usuario.ROLES:
            raise ValueError(
                "El rol seleccionado no es válido."
            )

        # En esta versión no permitimos crear nuevos
        # administradores desde el formulario.
        if rol == "Administrador":
            raise ValueError(
                "No se permite registrar nuevos administradores."
            )

        if any(
            usuario.nombre_usuario.lower()
            == nombre_usuario.lower()
            for usuario in self.usuarios
        ):
            raise ValueError(
                "El nombre de usuario ya existe."
            )

        if any(
            usuario.correo.lower()
            == correo.lower()
            for usuario in self.usuarios
        ):
            raise ValueError(
                "El correo ya se encuentra registrado."
            )

        nuevo_usuario = Usuario(
            identificador=self.siguiente_identificador(),
            nombre=nombre,
            correo=correo,
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            rol=rol,
            activo=True
        )

        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()

    def buscar_usuario_por_id(self, identificador):
        identificador = str(identificador)

        return next(
            (
                usuario
                for usuario in self.usuarios
                if usuario.identificador == identificador
            ),
            None
        )

    def buscar_usuario_por_nombre_usuario(
        self,
        nombre_usuario
    ):
        nombre_usuario = nombre_usuario.strip().lower()

        return next(
            (
                usuario
                for usuario in self.usuarios
                if usuario.nombre_usuario.lower()
                == nombre_usuario
            ),
            None
        )

    def actualizar_usuario(
        self,
        identificador,
        nombre,
        correo,
        nombre_usuario,
        rol
    ):
        usuario = self.buscar_usuario_por_id(
            identificador
        )

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        nombre = nombre.strip()
        correo = correo.strip()
        nombre_usuario = nombre_usuario.strip()

        if not nombre:
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo:
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if not nombre_usuario:
            raise ValueError(
                "El nombre de usuario no puede estar vacío."
            )

        if rol not in Usuario.ROLES:
            raise ValueError(
                "El rol seleccionado no es válido."
            )

        if (
            rol == "Administrador"
            and usuario.rol != "Administrador"
        ):
            raise ValueError(
                "No se puede asignar el rol Administrador."
            )

        for otro in self.usuarios:
            if otro.identificador == usuario.identificador:
                continue

            if (
                otro.nombre_usuario.lower()
                == nombre_usuario.lower()
            ):
                raise ValueError(
                    "El nombre de usuario ya existe."
                )

            if (
                otro.correo.lower()
                == correo.lower()
            ):
                raise ValueError(
                    "El correo ya está registrado."
                )

        usuario.nombre = nombre
        usuario.correo = correo
        usuario.nombre_usuario = nombre_usuario
        usuario.rol = rol

        self.guardar_usuarios()

    def cambiar_contrasena(
        self,
        identificador,
        nueva_contrasena
    ):
        usuario = self.buscar_usuario_por_id(
            identificador
        )

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        if not nueva_contrasena:
            raise ValueError(
                "La nueva contraseña no puede estar vacía."
            )

        usuario.contrasena = nueva_contrasena

        self.guardar_usuarios()

    def cambiar_estado_usuario(self, identificador):
        usuario = self.buscar_usuario_por_id(
            identificador
        )

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        if usuario.rol == "Administrador":
            raise ValueError(
                "No se puede deshabilitar al administrador."
            )

        usuario.activo = not usuario.activo

        self.guardar_usuarios()

    def eliminar_usuario(
        self,
        identificador,
        usuario_actual=None
    ):
        usuario = self.buscar_usuario_por_id(
            identificador
        )

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        if (
            usuario_actual is not None
            and usuario.nombre_usuario.lower()
            == usuario_actual.lower()
        ):
            raise ValueError(
                "No puede eliminar su propia cuenta."
            )

        if usuario.rol == "Administrador":
            raise ValueError(
                "No se puede eliminar un administrador."
            )

        self.usuarios.remove(usuario)

        self.guardar_usuarios()

    # ==========================================================
    # LOGIN
    # ==========================================================

    def validar_login(
        self,
        nombre_usuario,
        contrasena
    ):
        usuario = self.buscar_usuario_por_nombre_usuario(
            nombre_usuario
        )

        if usuario is None:
            raise ValueError(
                "El usuario no está registrado."
            )

        if not usuario.activo:
            raise ValueError(
                "El usuario se encuentra deshabilitado."
            )

        if usuario.contrasena != contrasena:
            raise ValueError(
                "La contraseña es incorrecta."
            )

        return usuario

    # ==========================================================
    # VENTAS
    # ==========================================================

    def obtener_ventas(self):
        datos = ArchivoServicio.cargar_json(
            self.path_ventas
        )

        return [
            Venta.from_dict(dato)
            for dato in datos
        ]

    def guardar_ventas(self):
        ArchivoServicio.guardar_json(
            self.path_ventas,
            [
                venta.to_dict()
                for venta in self.ventas
            ]
        )

    def registrar_venta(
        self,
        nombre_usuario,
        nombre_producto
    ):
        nombre_usuario = nombre_usuario.strip()
        nombre_producto = nombre_producto.strip()

        if not nombre_usuario:
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if not nombre_producto:
            raise ValueError(
                "Debe seleccionar un producto."
            )

        usuario = next(
            (
                usuario
                for usuario in self.usuarios
                if usuario.nombre == nombre_usuario
            ),
            None
        )

        if usuario is None:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = next(
            (
                producto
                for producto in self.productos
                if producto.nombre == nombre_producto
            ),
            None
        )

        if producto is None:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        fecha_actual = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        nueva_venta = Venta(
            usuario.nombre,
            producto.nombre,
            fecha_actual
        )

        self.ventas.append(nueva_venta)
        self.guardar_ventas()