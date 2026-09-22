import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario


class MainView:
    def __init__(
        self,
        root,
        servicio,
        usuario_actual
    ):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.root.title(
            "Sistema de Restaurante"
        )

        self.root.geometry(
            "900x650"
        )

        self.root.minsize(
            800,
            600
        )

        self.cargar_icono()
        self.crear_interfaz()

    # =========================
    # RECURSOS
    # =========================

    def obtener_ruta_asset(self, nombre_archivo):
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        return os.path.join(
            base_dir,
            "assets",
            nombre_archivo
        )

    def cargar_icono(self):
        ruta_icono = self.obtener_ruta_asset(
            "icono.png"
        )

        if not os.path.exists(ruta_icono):
            return

        try:
            self.icono = tk.PhotoImage(
                file=ruta_icono
            )

            self.root.iconphoto(
                True,
                self.icono
            )

        except tk.TclError:
            self.icono = None

    def cargar_logo(self):
        ruta_logo = self.obtener_ruta_asset(
            "logo.png"
        )

        if not os.path.exists(ruta_logo):
            return None

        try:
            logo = tk.PhotoImage(
                file=ruta_logo
            )

            ancho = logo.width()
            alto = logo.height()

            max_ancho = 180
            max_alto = 80

            factor_ancho = max(
                1,
                (ancho + max_ancho - 1)
                // max_ancho
            )

            factor_alto = max(
                1,
                (alto + max_alto - 1)
                // max_alto
            )

            factor = max(
                factor_ancho,
                factor_alto
            )

            if factor > 1:
                logo = logo.subsample(
                    factor,
                    factor
                )

            return logo

        except tk.TclError:
            return None

    # =========================
    # INTERFAZ PRINCIPAL
    # =========================

    def crear_interfaz(self):
        encabezado = tk.Frame(
            self.root,
            padx=25,
            pady=15
        )

        encabezado.pack(
            fill="x"
        )

        # -------------------------
        # LOGO
        # -------------------------

        self.logo = self.cargar_logo()

        if self.logo is not None:
            logo_label = tk.Label(
                encabezado,
                image=self.logo
            )

            logo_label.pack(
                side="left",
                padx=(0, 20)
            )

        # -------------------------
        # TITULO
        # -------------------------

        titulo = tk.Label(
            encabezado,
            text="Sistema de Restaurante",
            font=("Arial", 22, "bold")
        )

        titulo.pack(
            side="left",
            pady=10
        )

        # -------------------------
        # USUARIO
        # -------------------------

        usuario_label = tk.Label(
            encabezado,
            text=(
                f"Usuario: "
                f"{self.usuario_actual.nombre}"
            ),
            font=("Arial", 11)
        )

        usuario_label.pack(
            side="right"
        )

        separador = ttk.Separator(
            self.root,
            orient="horizontal"
        )

        separador.pack(
            fill="x"
        )

        # -------------------------
        # PESTAÑAS
        # -------------------------

        self.notebook = ttk.Notebook(
            self.root
        )

        self.notebook.pack(
            expand=True,
            fill="both",
            padx=15,
            pady=15
        )

        self.crear_pestana_productos()
        self.crear_pestana_usuarios()
        self.crear_pestana_ventas()

    # =========================
    # PRODUCTOS
    # =========================

    def crear_pestana_productos(self):
        pestana = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            pestana,
            text="Productos"
        )

        formulario = ttk.LabelFrame(
            pestana,
            text="Registrar producto",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_producto = ttk.Entry(
            formulario,
            width=35
        )

        self.entrada_producto.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_precio = ttk.Entry(
            formulario,
            width=35
        )

        self.entrada_precio.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        boton = ttk.Button(
            formulario,
            text="Registrar producto",
            command=self.registrar_producto
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        tabla_frame = ttk.LabelFrame(
            pestana,
            text="Productos registrados",
            padding=10
        )

        tabla_frame.pack(
            expand=True,
            fill="both"
        )

        columnas = (
            "nombre",
            "precio"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Producto"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.column(
            "nombre",
            width=350
        )

        self.tabla_productos.column(
            "precio",
            width=150,
            anchor="center"
        )

        self.tabla_productos.pack(
            expand=True,
            fill="both"
        )

        self.actualizar_productos()

    def registrar_producto(self):
        nombre = (
            self.entrada_producto
            .get()
            .strip()
        )

        precio_texto = (
            self.entrada_precio
            .get()
            .strip()
        )

        if not nombre:
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el nombre del producto."
            )
            return

        if not precio_texto:
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el precio."
            )
            return

        try:
            precio = float(
                precio_texto
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        try:
            producto = Producto(
                nombre,
                precio
            )

            self.servicio.registrar_producto(
                producto
            )

            messagebox.showinfo(
                "Producto registrado",
                "El producto se registró correctamente."
            )

            self.entrada_producto.delete(
                0,
                tk.END
            )

            self.entrada_precio.delete(
                0,
                tk.END
            )

            self.actualizar_productos()
            self.actualizar_combos()

        except (
            ValueError,
            OSError
        ) as error:
            messagebox.showerror(
                "No se pudo registrar",
                str(error)
            )

    def actualizar_productos(self):
        for item in (
            self.tabla_productos.get_children()
        ):
            self.tabla_productos.delete(
                item
            )

        for producto in (
            self.servicio.listar_productos()
        ):
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.nombre,
                    f"${producto.precio:.2f}"
                )
            )

    # =========================
    # USUARIOS
    # =========================

    def crear_pestana_usuarios(self):
        pestana = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            pestana,
            text="Usuarios"
        )

        formulario = ttk.LabelFrame(
            pestana,
            text="Registrar usuario",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.entrada_usuario = ttk.Entry(
            formulario,
            width=35
        )

        self.entrada_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        boton = ttk.Button(
            formulario,
            text="Registrar usuario",
            command=self.registrar_usuario
        )

        boton.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=10
        )

        tabla_frame = ttk.LabelFrame(
            pestana,
            text="Usuarios registrados",
            padding=10
        )

        tabla_frame.pack(
            expand=True,
            fill="both"
        )

        self.tabla_usuarios = ttk.Treeview(
            tabla_frame,
            columns=("nombre",),
            show="headings"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.column(
            "nombre",
            width=400
        )

        self.tabla_usuarios.pack(
            expand=True,
            fill="both"
        )

        self.actualizar_usuarios()

    def registrar_usuario(self):
        nombre = (
            self.entrada_usuario
            .get()
            .strip()
        )

        if not nombre:
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el nombre del usuario."
            )
            return

        try:
            usuario = Usuario(
                nombre
            )

            self.servicio.registrar_usuario(
                usuario
            )

            messagebox.showinfo(
                "Usuario registrado",
                "El usuario se registró correctamente."
            )

            self.entrada_usuario.delete(
                0,
                tk.END
            )

            self.actualizar_usuarios()
            self.actualizar_combos()

        except (
            ValueError,
            OSError
        ) as error:
            messagebox.showerror(
                "No se pudo registrar",
                str(error)
            )

    def actualizar_usuarios(self):
        for item in (
            self.tabla_usuarios.get_children()
        ):
            self.tabla_usuarios.delete(
                item
            )

        for usuario in (
            self.servicio.listar_usuarios()
        ):
            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.nombre,
                )
            )

    # =========================
    # VENTAS
    # =========================

    def crear_pestana_ventas(self):
        pestana = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            pestana,
            text="Ventas"
        )

        formulario = ttk.LabelFrame(
            pestana,
            text="Registrar venta",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        boton = ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=12
        )

        tabla_frame = ttk.LabelFrame(
            pestana,
            text="Ventas registradas",
            padding=10
        )

        tabla_frame.pack(
            expand=True,
            fill="both"
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "usuario",
            width=200
        )

        self.tabla_ventas.column(
            "producto",
            width=250
        )

        self.tabla_ventas.column(
            "fecha",
            width=180
        )

        self.tabla_ventas.pack(
            expand=True,
            fill="both"
        )

        self.actualizar_combos()
        self.actualizar_ventas()

    def actualizar_combos(self):
        if not hasattr(
            self,
            "combo_usuario"
        ):
            return

        usuarios = [
            usuario.nombre
            for usuario in (
                self.servicio.listar_usuarios()
            )
        ]

        productos = [
            producto.nombre
            for producto in (
                self.servicio.listar_productos()
            )
        ]

        self.combo_usuario["values"] = usuarios
        self.combo_producto["values"] = productos

        if usuarios:
            self.combo_usuario.current(0)
        else:
            self.combo_usuario.set("")

        if productos:
            self.combo_producto.current(0)
        else:
            self.combo_producto.set("")

    def registrar_venta(self):
        usuario_nombre = (
            self.combo_usuario
            .get()
            .strip()
        )

        producto_nombre = (
            self.combo_producto
            .get()
            .strip()
        )

        if not usuario_nombre:
            messagebox.showwarning(
                "Dato requerido",
                "Seleccione un usuario."
            )
            return

        if not producto_nombre:
            messagebox.showwarning(
                "Dato requerido",
                "Seleccione un producto."
            )
            return

        usuario = next(
            (
                u
                for u in (
                    self.servicio.listar_usuarios()
                )
                if u.nombre == usuario_nombre
            ),
            None
        )

        producto = next(
            (
                p
                for p in (
                    self.servicio.listar_productos()
                )
                if p.nombre == producto_nombre
            ),
            None
        )

        try:
            fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.servicio.registrar_venta(
                usuario,
                producto,
                fecha
            )

            messagebox.showinfo(
                "Venta registrada",
                "La venta se registró correctamente."
            )

            self.actualizar_ventas()

        except (
            ValueError,
            OSError
        ) as error:
            messagebox.showerror(
                "No se pudo registrar la venta",
                str(error)
            )

    def actualizar_ventas(self):
        for item in (
            self.tabla_ventas.get_children()
        ):
            self.tabla_ventas.delete(
                item
            )

        for venta in (
            self.servicio.listar_ventas()
        ):
            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.usuario.nombre,
                    venta.producto.nombre,
                    venta.fecha
                )
            )