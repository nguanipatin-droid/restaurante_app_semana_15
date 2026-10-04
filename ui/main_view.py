import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView(tk.Tk):

    def __init__(self, servicio, usuario):
        super().__init__()

        self.servicio = servicio
        self.usuario_actual = usuario

        # ==================================================
        # CONFIGURACIÓN DE LA VENTANA
        # ==================================================

        self.title("Sistema de Restaurante")
        self.geometry("1150x720")
        self.minsize(1000, 650)

        self.configure(
            bg="#F4F6F8"
        )

        # ==================================================
        # RUTAS DE LOS RECURSOS
        # ==================================================

        carpeta_proyecto = (
            Path(__file__).resolve().parent.parent
        )

        carpeta_assets = (
            carpeta_proyecto / "assets"
        )

        ruta_logo = (
            carpeta_assets / "logo original.png"
        )

        ruta_icono = (
            carpeta_assets / "icono.png"
        )

        if not ruta_logo.exists():

            ruta_logo = (
                carpeta_assets / "logo.png"
            )

        # ==================================================
        # ICONO
        # ==================================================

        try:

            self.icono_imagen = tk.PhotoImage(
                file=str(ruta_icono)
            )

            self.iconphoto(
                True,
                self.icono_imagen
            )

        except Exception:

            self.icono_imagen = None

        # ==================================================
        # LOGO
        # ==================================================

        try:

            self.logo_imagen = tk.PhotoImage(
                file=str(ruta_logo)
            )

            if self.logo_imagen.width() > 200:

                factor = max(
                    1,
                    self.logo_imagen.width() // 180
                )

                self.logo_imagen = (
                    self.logo_imagen.subsample(
                        factor,
                        factor
                    )
                )

        except Exception:

            self.logo_imagen = None

        # ==================================================
        # CENTRAR VENTANA
        # ==================================================

        self.update_idletasks()

        ancho = 1150
        alto = 720

        pantalla_ancho = (
            self.winfo_screenwidth()
        )

        pantalla_alto = (
            self.winfo_screenheight()
        )

        posicion_x = (
            pantalla_ancho - ancho
        ) // 2

        posicion_y = (
            pantalla_alto - alto
        ) // 2

        self.geometry(
            f"{ancho}x{alto}+{posicion_x}+{posicion_y}"
        )

        # ==================================================
        # ESTILOS
        # ==================================================

        self.crear_estilos()

        # ==================================================
        # INTERFAZ
        # ==================================================

        self.crear_interfaz()

        # ==================================================
        # CARGAR DATOS
        # ==================================================

        self.cargar_datos_iniciales()

    # ======================================================
    # ESTILOS
    # ======================================================

    def crear_estilos(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except tk.TclError:

            pass

        # ==================================================
        # NOTEBOOK
        # ==================================================

        estilo.configure(
            "TNotebook",
            background="#F4F6F8",
            borderwidth=0
        )

        estilo.configure(
            "TNotebook.Tab",
            background="#D9DEE3",
            foreground="#263238",
            padding=(30, 12),
            font=("Arial", 10, "bold")
        )

        estilo.map(
            "TNotebook.Tab",
            background=[
                ("selected", "#263238")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        # ==================================================
        # LABELFRAME
        # ==================================================

        estilo.configure(
            "TLabelframe",
            background="white",
            bordercolor="#D5DADF",
            borderwidth=1,
            relief="solid"
        )

        estilo.configure(
            "TLabelframe.Label",
            background="white",
            foreground="#263238",
            font=("Arial", 10, "bold")
        )

        # ==================================================
        # LABEL
        # ==================================================

        estilo.configure(
            "TLabel",
            background="white",
            foreground="#263238",
            font=("Arial", 10)
        )

        # ==================================================
        # ENTRADAS
        # ==================================================

        estilo.configure(
            "TEntry",
            padding=7
        )

        # ==================================================
        # COMBOBOX
        # ==================================================

        estilo.configure(
            "TCombobox",
            padding=7
        )

        # ==================================================
        # BOTÓN VERDE
        # ==================================================

        estilo.configure(
            "Green.TButton",
            background="#2E7D32",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Green.TButton",
            background=[
                ("active", "#1B5E20")
            ]
        )

        # ==================================================
        # BOTÓN AZUL
        # ==================================================

        estilo.configure(
            "Blue.TButton",
            background="#1565C0",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Blue.TButton",
            background=[
                ("active", "#0D47A1")
            ]
        )

        # ==================================================
        # BOTÓN MORADO
        # ==================================================

        estilo.configure(
            "Purple.TButton",
            background="#6A1B9A",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Purple.TButton",
            background=[
                ("active", "#4A148C")
            ]
        )

        # ==================================================
        # BOTÓN NARANJA
        # ==================================================

        estilo.configure(
            "Orange.TButton",
            background="#EF6C00",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Orange.TButton",
            background=[
                ("active", "#E65100")
            ]
        )

        # ==================================================
        # BOTÓN ROJO
        # ==================================================

        estilo.configure(
            "Red.TButton",
            background="#C62828",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Red.TButton",
            background=[
                ("active", "#8E0000")
            ]
        )

        # ==================================================
        # BOTÓN GRIS
        # ==================================================

        estilo.configure(
            "Gray.TButton",
            background="#546E7A",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Gray.TButton",
            background=[
                ("active", "#37474F")
            ]
        )

        # ==================================================
        # TREEVIEW
        # ==================================================

        estilo.configure(
            "Treeview",
            background="white",
            foreground="#263238",
            fieldbackground="white",
            rowheight=34,
            font=("Arial", 10),
            borderwidth=0
        )

        estilo.configure(
            "Treeview.Heading",
            background="#37474F",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=8
        )

        estilo.map(
            "Treeview",
            background=[
                ("selected", "#DCE9F7")
            ],
            foreground=[
                ("selected", "#263238")
            ]
        )

    # ======================================================
    # INTERFAZ PRINCIPAL
    # ======================================================

    def crear_interfaz(self):

        # ==================================================
        # ENCABEZADO
        # ==================================================

        encabezado = tk.Frame(
            self,
            bg="#263238",
            height=95
        )

        encabezado.pack(
            fill="x"
        )

        encabezado.pack_propagate(
            False
        )

        # ==================================================
        # LOGO
        # ==================================================

        if self.logo_imagen:

            etiqueta_logo = tk.Label(
                encabezado,
                image=self.logo_imagen,
                bg="#263238"
            )

            etiqueta_logo.pack(
                side="left",
                padx=25
            )

        # ==================================================
        # NOMBRE DEL SISTEMA
        # ==================================================

        nombre_sistema = tk.Frame(
            encabezado,
            bg="#263238"
        )

        nombre_sistema.pack(
            side="left",
            padx=10
        )

        tk.Label(
            nombre_sistema,
            text="SISTEMA DE RESTAURANTE",
            bg="#263238",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w"
        )

        # ==================================================
        # INFORMACIÓN DEL USUARIO
        # ==================================================

        usuario_frame = tk.Frame(
            encabezado,
            bg="#263238"
        )

        usuario_frame.pack(
            side="right",
            padx=30
        )

        tk.Label(
            usuario_frame,
            text=self.usuario_actual.nombre,
            bg="#263238",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(
            anchor="e"
        )

        tk.Label(
            usuario_frame,
            text="@" + self.usuario_actual.nombre_usuario,
            bg="#263238",
            fg="#B0BEC5",
            font=("Arial", 9)
        ).pack(
            anchor="e",
            pady=(2, 0)
        )

        tk.Label(
            usuario_frame,
            text=self.usuario_actual.rol,
            bg="#263238",
            fg="#81C784",
            font=("Arial", 9, "bold")
        ).pack(
            anchor="e",
            pady=(2, 0)
        )

        # ==================================================
        # CONTENEDOR
        # ==================================================

        contenedor = tk.Frame(
            self,
            bg="#F4F6F8"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ==================================================
        # NOTEBOOK
        # ==================================================

        self.notebook = ttk.Notebook(
            contenedor
        )

        self.notebook.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # TAB PRODUCTOS
        # ==================================================

        self.tab_productos = tk.Frame(
            self.notebook,
            bg="#F4F6F8"
        )

        self.notebook.add(
            self.tab_productos,
            text="Productos"
        )

        # ==================================================
        # TAB USUARIOS
        # ==================================================

        if self.usuario_actual.rol == "Administrador":

            self.tab_usuarios = tk.Frame(
                self.notebook,
                bg="#F4F6F8"
            )

            self.notebook.add(
                self.tab_usuarios,
                text="Usuarios"
            )

        # ==================================================
        # TAB VENTAS
        # ==================================================

        self.tab_ventas = tk.Frame(
            self.notebook,
            bg="#F4F6F8"
        )

        self.notebook.add(
            self.tab_ventas,
            text="Ventas"
        )

        # ==================================================
        # CREAR CONTENIDO
        # ==================================================

        self.crear_tab_productos()

        if self.usuario_actual.rol == "Administrador":

            self.crear_tab_usuarios()

        self.crear_tab_ventas()

        # ==================================================
        # EVENTOS
        # ==================================================

        self.tree_productos.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

        self.tree_ventas.bind(
            "<<TreeviewSelect>>",
            lambda event: None
        )

        if self.usuario_actual.rol == "Administrador":

            self.tree_usuarios.bind(
                "<<TreeviewSelect>>",
                self.seleccionar_usuario
            )

    # ======================================================
    # PRODUCTOS
    # ======================================================

    def crear_tab_productos(self):

        titulo = tk.Label(
            self.tab_productos,
            text="Productos",
            bg="#F4F6F8",
            fg="#2E7D32",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # --------------------------------------------------
        # BARRA DE COLOR
        # --------------------------------------------------

        barra = tk.Frame(
            self.tab_productos,
            bg="#2E7D32",
            height=5
        )

        barra.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        barra.pack_propagate(
            False
        )

        # --------------------------------------------------
        # FORMULARIO
        # --------------------------------------------------

        formulario = ttk.LabelFrame(
            self.tab_productos,
            text="Registrar producto"
        )

        formulario.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        ttk.Label(
            formulario,
            text="Nombre del producto:"
        ).grid(
            row=0,
            column=0,
            padx=(20, 10),
            pady=20,
            sticky="w"
        )

        self.entry_producto = ttk.Entry(
            formulario
        )

        self.entry_producto.grid(
            row=0,
            column=1,
            padx=10,
            pady=20,
            sticky="ew"
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=0,
            column=2,
            padx=(20, 10),
            pady=20
        )

        self.entry_precio = ttk.Entry(
            formulario,
            width=15
        )

        self.entry_precio.grid(
            row=0,
            column=3,
            padx=10,
            pady=20
        )

        ttk.Button(
            formulario,
            text="Registrar",
            style="Green.TButton",
            command=self.guardar_producto
        ).grid(
            row=0,
            column=4,
            padx=(10, 20),
            pady=20
        )

        # --------------------------------------------------
        # TABLA
        # --------------------------------------------------

        tabla_frame = ttk.LabelFrame(
            self.tab_productos,
            text="Productos registrados"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columnas = (
            "nombre",
            "precio"
        )

        self.tree_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tree_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tree_productos.heading(
            "precio",
            text="Precio"
        )

        self.tree_productos.column(
            "nombre",
            width=600,
            anchor="w"
        )

        self.tree_productos.column(
            "precio",
            width=180,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree_productos.yview
        )

        self.tree_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree_productos.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(12, 0),
            pady=12
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 12),
            pady=12
        )

    def guardar_producto(self):

        nombre = (
            self.entry_producto
            .get()
            .strip()
        )

        precio = (
            self.entry_precio
            .get()
            .strip()
        )

        try:

            self.servicio.registrar_producto(
                nombre,
                precio
            )

            messagebox.showinfo(
                "Producto",
                "Producto registrado correctamente.",
                parent=self
            )

            self.entry_producto.delete(
                0,
                tk.END
            )

            self.entry_precio.delete(
                0,
                tk.END
            )

            self.actualizar_tabla_productos()
            self.actualizar_combos()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    def seleccionar_producto(self, event=None):

        seleccion = (
            self.tree_productos.selection()
        )

        if not seleccion:
            return

        item = self.tree_productos.item(
            seleccion[0]
        )

        valores = item.get(
            "values",
            []
        )

        if len(valores) < 2:
            return

        self.entry_producto.delete(
            0,
            tk.END
        )

        self.entry_producto.insert(
            0,
            valores[0]
        )

        self.entry_precio.delete(
            0,
            tk.END
        )

        precio = str(
            valores[1]
        ).replace(
            "$",
            ""
        )

        self.entry_precio.insert(
            0,
            precio
        )

    # ======================================================
    # USUARIOS
    # ======================================================

    def crear_tab_usuarios(self):

        titulo = tk.Label(
            self.tab_usuarios,
            text="Usuarios",
            bg="#F4F6F8",
            fg="#6A1B9A",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # --------------------------------------------------
        # BARRA DE COLOR
        # --------------------------------------------------

        barra = tk.Frame(
            self.tab_usuarios,
            bg="#6A1B9A",
            height=5
        )

        barra.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        barra.pack_propagate(
            False
        )

        # --------------------------------------------------
        # FORMULARIO
        # --------------------------------------------------

        formulario = ttk.LabelFrame(
            self.tab_usuarios,
            text="Datos del usuario"
        )

        formulario.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        # --------------------------------------------------
        # IDENTIFICADOR
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Identificador:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_identificador = ttk.Entry(
            formulario,
            width=18,
            state="readonly"
        )

        self.entry_identificador.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # --------------------------------------------------
        # NOMBRE
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_nombre = ttk.Entry(
            formulario,
            width=25
        )

        self.entry_nombre.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        # --------------------------------------------------
        # CORREO
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Correo:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_correo = ttk.Entry(
            formulario,
            width=25
        )

        self.entry_correo.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # --------------------------------------------------
        # NOMBRE DE USUARIO
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Nombre de usuario:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_nombre_usuario = ttk.Entry(
            formulario,
            width=25
        )

        self.entry_nombre_usuario.grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        # --------------------------------------------------
        # CONTRASEÑA
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_contrasena = ttk.Entry(
            formulario,
            width=25,
            show="*"
        )

        self.entry_contrasena.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # --------------------------------------------------
        # ROL
        # --------------------------------------------------

        ttk.Label(
            formulario,
            text="Rol:"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.combo_rol = ttk.Combobox(
            formulario,
            values=(
                "Cliente",
                "Empleado"
            ),
            state="readonly",
            width=22
        )

        self.combo_rol.grid(
            row=2,
            column=3,
            padx=10,
            pady=10
        )

        self.combo_rol.set(
            "Cliente"
        )

        # --------------------------------------------------
        # BOTONES
        # --------------------------------------------------

        botones = tk.Frame(
            formulario,
            bg="white"
        )

        botones.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=(5, 15)
        )

        ttk.Button(
            botones,
            text="Registrar",
            style="Purple.TButton",
            command=self.guardar_usuario
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Actualizar",
            style="Blue.TButton",
            command=self.actualizar_usuario
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Cambiar contraseña",
            style="Orange.TButton",
            command=self.cambiar_contrasena
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Habilitar / Deshabilitar",
            style="Red.TButton",
            command=self.cambiar_estado_usuario
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            style="Gray.TButton",
            command=self.limpiar_formulario_usuario
        ).pack(
            side="left",
            padx=4
        )

        # --------------------------------------------------
        # TABLA
        # --------------------------------------------------

        tabla_frame = ttk.LabelFrame(
            self.tab_usuarios,
            text="Usuarios registrados"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columnas = (
            "id",
            "nombre",
            "correo",
            "usuario",
            "rol",
            "estado"
        )

        self.tree_usuarios = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tree_usuarios.heading(
            "id",
            text="ID"
        )

        self.tree_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tree_usuarios.heading(
            "correo",
            text="Correo"
        )

        self.tree_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tree_usuarios.heading(
            "rol",
            text="Rol"
        )

        self.tree_usuarios.heading(
            "estado",
            text="Estado"
        )

        self.tree_usuarios.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree_usuarios.column(
            "nombre",
            width=180,
            anchor="w"
        )

        self.tree_usuarios.column(
            "correo",
            width=220,
            anchor="w"
        )

        self.tree_usuarios.column(
            "usuario",
            width=130,
            anchor="center"
        )

        self.tree_usuarios.column(
            "rol",
            width=120,
            anchor="center"
        )

        self.tree_usuarios.column(
            "estado",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree_usuarios.yview
        )

        self.tree_usuarios.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree_usuarios.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(12, 0),
            pady=12
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 12),
            pady=12
        )

    def guardar_usuario(self):

        nombre = (
            self.entry_nombre
            .get()
            .strip()
        )

        correo = (
            self.entry_correo
            .get()
            .strip()
        )

        nombre_usuario = (
            self.entry_nombre_usuario
            .get()
            .strip()
        )

        contrasena = (
            self.entry_contrasena
            .get()
        )

        rol = (
            self.combo_rol
            .get()
        )

        try:

            self.servicio.registrar_usuario(
                nombre,
                correo,
                nombre_usuario,
                contrasena,
                rol
            )

            messagebox.showinfo(
                "Usuario",
                "Usuario registrado correctamente.",
                parent=self
            )

            self.limpiar_formulario_usuario()
            self.actualizar_tabla_usuarios()
            self.actualizar_combos()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    def seleccionar_usuario(self, event=None):

        seleccion = (
            self.tree_usuarios.selection()
        )

        if not seleccion:
            return

        item = self.tree_usuarios.item(
            seleccion[0]
        )

        valores = item.get(
            "values",
            []
        )

        if len(valores) < 6:
            return

        identificador = (
            valores[0]
        )

        usuario = (
            self.servicio.buscar_usuario_por_id(
                identificador
            )
        )

        if usuario is None:
            return

        # --------------------------------------------------
        # ID
        # --------------------------------------------------

        self.entry_identificador.config(
            state="normal"
        )

        self.entry_identificador.delete(
            0,
            tk.END
        )

        self.entry_identificador.insert(
            0,
            usuario.identificador
        )

        self.entry_identificador.config(
            state="readonly"
        )

        # --------------------------------------------------
        # NOMBRE
        # --------------------------------------------------

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_nombre.insert(
            0,
            usuario.nombre
        )

        # --------------------------------------------------
        # CORREO
        # --------------------------------------------------

        self.entry_correo.delete(
            0,
            tk.END
        )

        self.entry_correo.insert(
            0,
            usuario.correo
        )

        # --------------------------------------------------
        # USUARIO
        # --------------------------------------------------

        self.entry_nombre_usuario.delete(
            0,
            tk.END
        )

        self.entry_nombre_usuario.insert(
            0,
            usuario.nombre_usuario
        )

        # --------------------------------------------------
        # CONTRASEÑA
        # --------------------------------------------------

        self.entry_contrasena.delete(
            0,
            tk.END
        )

        # --------------------------------------------------
        # ROL
        # --------------------------------------------------

        self.combo_rol.set(
            usuario.rol
        )

    def actualizar_usuario(self):

        identificador = (
            self.entry_identificador.get()
        )

        if not identificador:

            messagebox.showwarning(
                "Usuario",
                "Seleccione primero un usuario.",
                parent=self
            )

            return

        try:

            self.servicio.actualizar_usuario(
                identificador,
                self.entry_nombre.get(),
                self.entry_correo.get(),
                self.entry_nombre_usuario.get(),
                self.combo_rol.get()
            )

            messagebox.showinfo(
                "Usuario",
                "Usuario actualizado correctamente.",
                parent=self
            )

            self.limpiar_formulario_usuario()
            self.actualizar_tabla_usuarios()
            self.actualizar_combos()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    def cambiar_contrasena(self):

        identificador = (
            self.entry_identificador.get()
        )

        if not identificador:

            messagebox.showwarning(
                "Contraseña",
                "Seleccione primero un usuario.",
                parent=self
            )

            return

        nueva_contrasena = (
            self.entry_contrasena.get()
        )

        if not nueva_contrasena:

            messagebox.showwarning(
                "Contraseña",
                "Ingrese la nueva contraseña.",
                parent=self
            )

            return

        try:

            self.servicio.cambiar_contrasena(
                identificador,
                nueva_contrasena
            )

            messagebox.showinfo(
                "Contraseña",
                "Contraseña modificada correctamente.",
                parent=self
            )

            self.entry_contrasena.delete(
                0,
                tk.END
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    def cambiar_estado_usuario(self):

        identificador = (
            self.entry_identificador.get()
        )

        if not identificador:

            messagebox.showwarning(
                "Usuario",
                "Seleccione primero un usuario.",
                parent=self
            )

            return

        try:

            self.servicio.cambiar_estado_usuario(
                identificador
            )

            messagebox.showinfo(
                "Usuario",
                "Estado del usuario actualizado.",
                parent=self
            )

            self.limpiar_formulario_usuario()
            self.actualizar_tabla_usuarios()
            self.actualizar_combos()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    def limpiar_formulario_usuario(self):

        self.entry_identificador.config(
            state="normal"
        )

        self.entry_identificador.delete(
            0,
            tk.END
        )

        self.entry_identificador.config(
            state="readonly"
        )

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_correo.delete(
            0,
            tk.END
        )

        self.entry_nombre_usuario.delete(
            0,
            tk.END
        )

        self.entry_contrasena.delete(
            0,
            tk.END
        )

        self.combo_rol.set(
            "Cliente"
        )

        if hasattr(
            self,
            "tree_usuarios"
        ):

            for seleccion in (
                self.tree_usuarios.selection()
            ):

                self.tree_usuarios.selection_remove(
                    seleccion
                )

    # ======================================================
    # VENTAS
    # ======================================================

    def crear_tab_ventas(self):

        titulo = tk.Label(
            self.tab_ventas,
            text="Ventas",
            bg="#F4F6F8",
            fg="#1565C0",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # --------------------------------------------------
        # BARRA DE COLOR
        # --------------------------------------------------

        barra = tk.Frame(
            self.tab_ventas,
            bg="#1565C0",
            height=5
        )

        barra.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        barra.pack_propagate(
            False
        )

        # --------------------------------------------------
        # FORMULARIO
        # --------------------------------------------------

        formulario = ttk.LabelFrame(
            self.tab_ventas,
            text="Registrar venta"
        )

        formulario.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=20
        )

        self.combo_usuario_venta = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_usuario_venta.grid(
            row=0,
            column=1,
            padx=10,
            pady=20
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=0,
            column=2,
            padx=15,
            pady=20
        )

        self.combo_producto_venta = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_producto_venta.grid(
            row=0,
            column=3,
            padx=10,
            pady=20
        )

        ttk.Button(
            formulario,
            text="Registrar",
            style="Blue.TButton",
            command=self.guardar_venta
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=20
        )

        # --------------------------------------------------
        # TABLA
        # --------------------------------------------------

        tabla_frame = ttk.LabelFrame(
            self.tab_ventas,
            text="Ventas registradas"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tree_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tree_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tree_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tree_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tree_ventas.column(
            "usuario",
            width=300,
            anchor="w"
        )

        self.tree_ventas.column(
            "producto",
            width=300,
            anchor="w"
        )

        self.tree_ventas.column(
            "fecha",
            width=250,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree_ventas.yview
        )

        self.tree_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree_ventas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(12, 0),
            pady=12
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 12),
            pady=12
        )

    def guardar_venta(self):

        usuario = (
            self.combo_usuario_venta.get()
        )

        producto = (
            self.combo_producto_venta.get()
        )

        try:

            self.servicio.registrar_venta(
                usuario,
                producto
            )

            messagebox.showinfo(
                "Venta",
                "Venta registrada correctamente.",
                parent=self
            )

            self.combo_usuario_venta.set(
                ""
            )

            self.combo_producto_venta.set(
                ""
            )

            self.actualizar_tabla_ventas()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self
            )

    # ======================================================
    # TABLA PRODUCTOS
    # ======================================================

    def actualizar_tabla_productos(self):

        for item in (
            self.tree_productos.get_children()
        ):

            self.tree_productos.delete(
                item
            )

        productos = (
            self.servicio.obtener_productos()
        )

        for producto in productos:

            self.tree_productos.insert(
                "",
                tk.END,
                values=(
                    producto.nombre,
                    f"${producto.precio:.2f}"
                )
            )

    # ======================================================
    # TABLA USUARIOS
    # ======================================================

    def actualizar_tabla_usuarios(self):

        if not hasattr(
            self,
            "tree_usuarios"
        ):

            return

        for item in (
            self.tree_usuarios.get_children()
        ):

            self.tree_usuarios.delete(
                item
            )

        usuarios = (
            self.servicio.obtener_usuarios()
        )

        for usuario in usuarios:

            if usuario.activo:

                estado = "Habilitado"

            else:

                estado = "Deshabilitado"

            self.tree_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificador,
                    usuario.nombre,
                    usuario.correo,
                    usuario.nombre_usuario,
                    usuario.rol,
                    estado
                )
            )

    # ======================================================
    # TABLA VENTAS
    # ======================================================

    def actualizar_tabla_ventas(self):

        for item in (
            self.tree_ventas.get_children()
        ):

            self.tree_ventas.delete(
                item
            )

        ventas = (
            self.servicio.obtener_ventas()
        )

        for venta in ventas:

            self.tree_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )

    # ======================================================
    # ACTUALIZAR COMBOS
    # ======================================================

    def actualizar_combos(self):

        usuarios = (
            self.servicio.obtener_usuarios()
        )

        productos = (
            self.servicio.obtener_productos()
        )

        usuarios_activos = []

        for usuario in usuarios:

            if usuario.activo:

                usuarios_activos.append(
                    usuario.nombre
                )

        nombres_productos = []

        for producto in productos:

            nombres_productos.append(
                producto.nombre
            )

        self.combo_usuario_venta[
            "values"
        ] = usuarios_activos

        self.combo_producto_venta[
            "values"
        ] = nombres_productos

    # ======================================================
    # CARGAR DATOS INICIALES
    # ======================================================

    def cargar_datos_iniciales(self):

        self.actualizar_tabla_productos()

        if self.usuario_actual.rol == "Administrador":

            self.actualizar_tabla_usuarios()

        self.actualizar_tabla_ventas()

        self.actualizar_combos()