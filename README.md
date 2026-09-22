# Sistema de Restaurante

Nombre: Nahomy Guanipatin
Asignatura: Programación Orientada a Objetos
Paralelo: "E"

## Descripción

Sistema de gestión para un restaurante desarrollado en Python, utilizando Programación Orientada a Objetos, interfaz gráfica con Tkinter y almacenamiento de información mediante archivos JSON.

El sistema permite administrar productos, usuarios y ventas desde una aplicación de escritorio.

## Funcionalidades

### Usuarios

* Registro de usuarios.
* Listado de usuarios registrados.
* Inicio de sesión mediante nombre de usuario.
* Creación automática del usuario `admin` cuando no existen usuarios.

### Productos

* Registro de productos.
* Validación del nombre y precio.
* Validación para evitar productos duplicados.
* Listado de productos.
* Visualización del precio con formato de moneda.

### Ventas

* Selección de usuario.
* Selección de producto.
* Registro automático de fecha y hora.
* Almacenamiento de las ventas.
* Listado de ventas realizadas.

## Tecnologías utilizadas

* **Python 3**
* **Tkinter** para la interfaz gráfica.
* **JSON** para la persistencia de datos.
* **Programación Orientada a Objetos (POO)**
* Arquitectura organizada por capas.
* Git y GitHub.

## Estructura del proyecto

```text
restaurante_app_semana15/
│
├── assets/
│   ├── logo.png
│   ├── icono.png
│   └── logo_original.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

## Descripción de los módulos

### `modelos/`

Contiene las clases principales del sistema:

* `producto.py`: contiene la clase `Producto`.
* `usuario.py`: contiene la clase `Usuario`.
* `venta.py`: contiene la clase `Venta`.

Las clases utilizan métodos `to_dict()` y `from_dict()` para convertir los objetos a datos compatibles con JSON y reconstruirlos posteriormente.

### `servicios/`

Contiene la lógica de negocio y el manejo de archivos:

* `archivo_servicio.py`: administra la lectura y escritura de archivos JSON.
* `restaurante_servicio.py`: administra productos, usuarios, ventas, validaciones y persistencia.

### `ui/`

Contiene las interfaces gráficas desarrolladas con Tkinter:

* `login_view.py`: ventana de inicio de sesión.
* `main_view.py`: ventana principal del sistema.

### `datos/`

Contiene los archivos JSON utilizados para almacenar la información:

* `productos.json`: almacena los productos.
* `usuarios.json`: almacena los usuarios.
* `ventas.json`: almacena las ventas realizadas.

### `assets/`

Contiene los recursos gráficos utilizados por la aplicación:

* `logo.png`: logotipo principal.
* `icono.png`: icono de la aplicación.
* `logo_original.png`: copia de respaldo del logotipo original.

## Datos almacenados

### Productos

Ejemplo de información almacenada en `productos.json`:

```json
[
    {
        "nombre": "Hamburguesa",
        "precio": 3.5
    },
    {
        "nombre": "Papas Fritas",
        "precio": 1.0
    },
    {
        "nombre": "Ensalada de frutas",
        "precio": 2.5
    },
    {
        "nombre": "Jugo Natural",
        "precio": 1.75
    }
]
```

### Usuarios

Ejemplo de información almacenada en `usuarios.json`:

```json
[
    {
        "nombre": "admin"
    },
    {
        "nombre": "Nahomy Guanipatin"
    },
    {
        "nombre": "Carlos Torres"
    },
    {
        "nombre": "Juan Lopez"
    }
]
```

### Ventas

Ejemplo de información almacenada en `ventas.json`:

```json
[
    {
        "usuario": "Nahomy Guanipatin",
        "producto": "Hamburguesa",
        "fecha": "2026-09-22 06:03:17"
    },
    {
        "usuario": "Carlos Torres",
        "producto": "Ensalada de frutas",
        "fecha": "2026-09-22 06:03:33"
    }
]
```

## Requisitos

Para ejecutar el proyecto se necesita:

* Python 3 instalado.
* Tkinter, incluido normalmente en la instalación estándar de Python.
* No se requieren paquetes externos.

## Instalación

Clonar o descargar el repositorio y acceder a la carpeta del proyecto:

```powershell
cd restaurante_app_semana15
```

Comprobar la versión de Python:

```powershell
py --version
```

## Ejecución

Ejecutar el programa con:

```powershell
py main.py
```

Al iniciar la aplicación se mostrará la ventana de inicio de sesión.

## Ejemplos de ejecución

### 1. Inicio de sesión

Al ejecutar el programa se muestra la ventana de inicio de sesión.

El usuario debe ingresar un nombre registrado en `usuarios.json`.

Ejemplo:

```text
Usuario: admin
```

Al presionar **Iniciar sesión**, el sistema valida que el usuario exista y permite ingresar a la aplicación principal.

### 2. Registro de productos

Desde la sección **Productos** se puede ingresar el nombre y precio de un nuevo producto.

Ejemplo:

```text
Nombre: Hamburguesa
Precio: 3.50
```

Después de registrar el producto, este se almacena en `productos.json` y aparece en la lista de productos.

### 3. Registro de usuarios

Desde la sección **Usuarios** se puede registrar un nuevo usuario.

Ejemplo:

```text
Nombre: Juan Lopez
```

El usuario se guarda en `usuarios.json` y aparece en la lista de usuarios registrados.

### 4. Registro de ventas

Desde la sección **Ventas** se selecciona un usuario y un producto.

Ejemplo:

```text
Usuario: Nahomy Guanipatin
Producto: Hamburguesa
```

Al registrar la venta, el sistema genera automáticamente la fecha y hora.

Ejemplo:

```text
2026-09-22 06:03:17
```

La información se almacena en `ventas.json` y aparece en la lista de ventas.

### 5. Resultado general

El flujo de ejecución del sistema es:

```text
Ejecutar main.py
      ↓
Inicio de sesión
      ↓
Validación del usuario
      ↓
Ventana principal
      ↓
┌─────────────┬─────────────┬─────────────┐
│  Productos  │  Usuarios   │   Ventas    │
└─────────────┴─────────────┴─────────────┘
      ↓
Guardar información en JSON
```

## Persistencia de datos

La información se guarda en archivos JSON dentro de la carpeta `datos/`.

Los archivos utilizados son:

* `productos.json`
* `usuarios.json`
* `ventas.json`

Los datos permanecen almacenados aunque la aplicación se cierre.

## Manejo de errores

El sistema incluye validaciones para evitar:

* Productos sin nombre.
* Productos con precio menor o igual a cero.
* Productos duplicados.
* Usuarios sin nombre.
* Usuarios duplicados.
* Ventas sin usuario.
* Ventas sin producto.
* Archivos JSON inexistentes.
* Archivos JSON vacíos o con formato incorrecto.
* Problemas de permisos durante la lectura o escritura.

## Arquitectura

El proyecto separa las responsabilidades de la aplicación:

```text
Interfaz gráfica
       ↓
Servicios
       ↓
Modelos
       ↓
Archivos JSON
```

Esta organización permite mantener separado el código de la interfaz, la lógica del sistema, los modelos de datos y la persistencia.

## Programación Orientada a Objetos

El proyecto aplica conceptos de Programación Orientada a Objetos mediante clases como:

* `Producto`
* `Usuario`
* `Venta`
* `ArchivoServicio`
* `RestauranteServicio`
* `LoginView`
* `MainView`

Cada clase tiene responsabilidades específicas dentro del sistema.

## Estado del proyecto

Proyecto académico funcional desarrollado en Python como práctica de Programación Orientada a Objetos.
