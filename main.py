from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_app():

    servicio = RestauranteServicio()

    def abrir_principal(usuario):

        app = MainView(
            servicio,
            usuario
        )

        app.mainloop()

    login = LoginView(
        servicio,
        abrir_principal
    )

    login.mainloop()


if __name__ == "__main__":
    iniciar_app()