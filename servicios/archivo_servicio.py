import json
import os


class ArchivoServicio:
    def __init__(self):
        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.datos_dir = os.path.join(
            self.base_dir,
            "datos"
        )

        os.makedirs(self.datos_dir, exist_ok=True)

    def guardar(self, nombre_archivo, datos):
        ruta = os.path.join(
            self.datos_dir,
            nombre_archivo
        )

        try:
            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except (PermissionError, OSError):
            return False

    def cargar(self, nombre_archivo):
        ruta = os.path.join(
            self.datos_dir,
            nombre_archivo
        )

        if not os.path.exists(ruta):
            return []

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:
                contenido = archivo.read().strip()

                if not contenido:
                    return []

                return json.loads(contenido)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

        except PermissionError:
            return []

        except OSError:
            return []