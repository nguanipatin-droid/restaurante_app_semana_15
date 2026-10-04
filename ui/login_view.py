import tkinter as tk
from tkinter import messagebox
from pathlib import Path


class LoginView(tk.Tk):

    def __init__(self, servicio, on_login_success):
        super().__init__()

        self.servicio = servicio
        self.on_login_success = on_login_success

        # ==========================================
        # RUTAS DE LOS RECURSOS
        # ==========================================

        carpeta_proyecto = Path(__file__).resolve().parent.parent
        carpeta_assets = carpeta_proyecto / "assets"

        ruta_logo = carpeta_assets / "logo original.png"
        ruta_icono = carpeta_assets / "icono.png"

        # Si no existe el logo original,
        # utilizar logo.png como respaldo.
        if not ruta_logo.exists():
            ruta_logo = carpeta_assets / "logo.png"

        # ==========================================
        # CONFIGURACIÓN DE LA VENTANA
        # ==========================================

        self.title("Sistema de Restaurante")
        self.geometry("700x560")
        self.resizable(False, False)

        self.configure(
            bg="#ECEFF1"
        )

        # ==========================================
        # ICONO DE LA VENTANA
        # ==========================================

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

        # ==========================================
        # CENTRAR LA VENTANA
        # ==========================================

        self.update_idletasks()

        ancho = 700
        alto = 560

        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()

        posicion_x = (
            pantalla_ancho - ancho
        ) // 2

        posicion_y = (
            pantalla_alto - alto
        ) // 2

        self.geometry(
            f"{ancho}x{alto}+{posicion_x}+{posicion_y}"
        )

        # ==========================================
        # CARGAR LOGO
        # ==========================================

        self.logo_imagen = None

        try:

            self.logo_imagen = tk.PhotoImage(
                file=str(ruta_logo)
            )

            # Reducir el logo solamente si es
            # demasiado grande.
            if self.logo_imagen.width() > 300:

                factor = max(
                    1,
                    self.logo_imagen.width() // 250
                )

                self.logo_imagen = (
                    self.logo_imagen.subsample(
                        factor,
                        factor
                    )
                )

        except Exception:

            self.logo_imagen = None

        # ==========================================
        # CREAR INTERFAZ
        # ==========================================

        self.crear_interfaz()

        # ==========================================
        # CURSOR INICIAL
        # ==========================================

        self.entry_usuario.focus()

        # ==========================================
        # TECLA ENTER
        # ==========================================

        self.bind(
            "<Return>",
            lambda event: self.validar_login()
        )

    # ==================================================
    # CREAR INTERFAZ
    # ==================================================

    def crear_interfaz(self):

        # ==========================================
        # CONTENEDOR PRINCIPAL
        # ==========================================

        contenedor = tk.Frame(
            self,
            bg="#ECEFF1"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=35
        )

        # ==========================================
        # TARJETA PRINCIPAL
        # ==========================================

        tarjeta = tk.Frame(
            contenedor,
            bg="white",
            highlightbackground="#D5D8DC",
            highlightthickness=1
        )

        tarjeta.pack(
            fill="both",
            expand=True
        )

        # ==========================================
        # LOGO
        # ==========================================

        if self.logo_imagen:

            etiqueta_logo = tk.Label(
                tarjeta,
                image=self.logo_imagen,
                bg="white"
            )

            etiqueta_logo.pack(
                pady=(35, 35)
            )

        # ==========================================
        # FORMULARIO
        # ==========================================

        formulario = tk.Frame(
            tarjeta,
            bg="white"
        )

        formulario.pack(
            padx=70,
            fill="x"
        )

        # ==========================================
        # NOMBRE DE USUARIO
        # ==========================================

        tk.Label(
            formulario,
            text="Nombre de usuario",
            bg="white",
            fg="#263238",
            font=("Arial", 11, "bold"),
            anchor="w"
        ).pack(
            fill="x",
            pady=(0, 7)
        )

        self.entry_usuario = tk.Entry(
            formulario,
            font=("Arial", 12),
            relief="solid",
            bd=1,
            bg="#FAFAFA",
            fg="#263238",
            insertbackground="#263238"
        )

        self.entry_usuario.pack(
            fill="x",
            ipady=9,
            pady=(0, 20)
        )

        # ==========================================
        # CONTRASEÑA
        # ==========================================

        tk.Label(
            formulario,
            text="Contraseña",
            bg="white",
            fg="#263238",
            font=("Arial", 11, "bold"),
            anchor="w"
        ).pack(
            fill="x",
            pady=(0, 7)
        )

        self.entry_contrasena = tk.Entry(
            formulario,
            font=("Arial", 12),
            show="*",
            relief="solid",
            bd=1,
            bg="#FAFAFA",
            fg="#263238",
            insertbackground="#263238"
        )

        self.entry_contrasena.pack(
            fill="x",
            ipady=9
        )

        # ==========================================
        # BOTÓN INICIAR SESIÓN
        # ==========================================

        boton_login = tk.Button(
            tarjeta,
            text="Iniciar Sesión",
            bg="#263238",
            fg="white",
            activebackground="#37474F",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=22,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.validar_login
        )

        boton_login.pack(
            pady=(30, 25)
        )

    # ==================================================
    # VALIDAR INICIO DE SESIÓN
    # ==================================================

    def validar_login(self):

        nombre_usuario = (
            self.entry_usuario
            .get()
            .strip()
        )

        contrasena = (
            self.entry_contrasena
            .get()
        )

        # ==========================================
        # VALIDAR NOMBRE DE USUARIO
        # ==========================================

        if not nombre_usuario:

            messagebox.showerror(
                "Error",
                "Ingrese su nombre de usuario.",
                parent=self
            )

            self.entry_usuario.focus()

            return

        # ==========================================
        # VALIDAR CONTRASEÑA
        # ==========================================

        if not contrasena:

            messagebox.showerror(
                "Error",
                "Ingrese su contraseña.",
                parent=self
            )

            self.entry_contrasena.focus()

            return

        # ==========================================
        # COMPROBAR CREDENCIALES
        # ==========================================

        try:

            usuario = self.servicio.validar_login(
                nombre_usuario,
                contrasena
            )

            # ======================================
            # CERRAR LOGIN
            # ======================================

            self.destroy()

            # ======================================
            # ABRIR VENTANA PRINCIPAL
            # ======================================

            self.on_login_success(
                usuario
            )

        except ValueError as error:

            messagebox.showerror(
                "Error de inicio de sesión",
                str(error),
                parent=self
            )

            # Limpiar contraseña

            self.entry_contrasena.delete(
                0,
                tk.END
            )

            self.entry_contrasena.focus()