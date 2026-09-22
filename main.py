import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView


def main():
    servicio = RestauranteServicio()

    if not servicio.listar_usuarios():
        from modelos.usuario import Usuario

        usuario_inicial = Usuario("admin")

        servicio.registrar_usuario(
            usuario_inicial
        )

    root = tk.Tk()

    LoginView(
        root,
        servicio
    )

    root.mainloop()


if __name__ == "__main__":
    main()