import os
import tkinter as tk
from tkinter import messagebox

from ui.main_view import MainView


class LoginView:
    def __init__(
        self,
        root,
        servicio
    ):
        self.root = root
        self.servicio = servicio

        self.root.title(
            "Sistema de Restaurante - Login"
        )

        self.root.geometry(
            "450x450"
        )

        self.root.resizable(
            False,
            False
        )

        self.cargar_icono()
        self.crear_interfaz()

    # =========================
    # RECURSOS
    # =========================

    def obtener_ruta_asset(
        self,
        nombre_archivo
    ):
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
            max_alto = 120

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
    # INTERFAZ
    # =========================

    def crear_interfaz(self):
        contenedor = tk.Frame(
            self.root,
            padx=30,
            pady=25
        )

        contenedor.pack(
            expand=True,
            fill="both"
        )

        self.logo = self.cargar_logo()

        if self.logo is not None:
            logo_label = tk.Label(
                contenedor,
                image=self.logo
            )

            logo_label.pack(
                pady=(5, 15)
            )

        else:
            self.mostrar_titulo(
                contenedor
            )

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 13)
        )

        subtitulo.pack(
            pady=(5, 20)
        )

        etiqueta = tk.Label(
            contenedor,
            text="Nombre de usuario:",
            font=("Arial", 11)
        )

        etiqueta.pack(
            anchor="w"
        )

        self.entrada_usuario = tk.Entry(
            contenedor,
            font=("Arial", 12)
        )

        self.entrada_usuario.pack(
            fill="x",
            pady=(5, 20)
        )

        boton = tk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            width=20,
            font=("Arial", 10, "bold")
        )

        boton.pack(
            pady=10
        )

        informacion = tk.Label(
            contenedor,
            text=(
                "Use un usuario registrado "
                "en el sistema."
            ),
            fg="gray"
        )

        informacion.pack(
            pady=15
        )

    def mostrar_titulo(
        self,
        contenedor
    ):
        titulo = tk.Label(
            contenedor,
            text="Sistema de Restaurante",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(20, 10)
        )

    # =========================
    # LOGIN
    # =========================

    def iniciar_sesion(self):
        nombre = (
            self.entrada_usuario
            .get()
            .strip()
        )

        if not nombre:
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el nombre de usuario."
            )

            return

        if not self.servicio.validar_login(
            nombre
        ):
            messagebox.showerror(
                "Acceso denegado",
                "El usuario no está registrado."
            )

            return

        usuario_actual = None

        for usuario in (
            self.servicio.listar_usuarios()
        ):
            if (
                usuario.nombre.lower()
                == nombre.lower()
            ):
                usuario_actual = usuario
                break

        if usuario_actual is None:
            messagebox.showerror(
                "Error",
                "No se pudo encontrar el usuario."
            )

            return

        for widget in (
            self.root.winfo_children()
        ):
            widget.destroy()

        MainView(
            self.root,
            self.servicio,
            usuario_actual
        )