import json
import os


class ArchivoServicio:

    @staticmethod
    def cargar_json(nombre_archivo):
        if not os.path.exists(nombre_archivo):
            return []

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read().strip()

                if not contenido:
                    return []

                return json.loads(contenido)

        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def guardar_json(nombre_archivo, datos):
        try:
            carpeta = os.path.dirname(nombre_archivo)

            if carpeta:
                os.makedirs(carpeta, exist_ok=True)

            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except IOError as e:
            print(
                f"Error al guardar el archivo "
                f"{nombre_archivo}: {e}"
            )