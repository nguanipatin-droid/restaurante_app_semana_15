# Sistema de Restaurante

Nombre: Nahomy Guanipatin

Asignatura: Programación Orientada a Objetos

Paralelo: "E"

---

## Descripción

Sistema de gestión para un restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO), interfaz gráfica con Tkinter y almacenamiento de información mediante archivos JSON.

El sistema permite administrar productos, usuarios y ventas desde una aplicación de escritorio.

La aplicación cuenta con un sistema de inicio de sesión y gestión de usuarios mediante roles y estados, permitiendo organizar las diferentes funciones del sistema de acuerdo con el tipo de usuario.

---

## Evolución del proyecto - Semana 15

El proyecto de la Semana 15 parte de la aplicación desarrollada en semanas anteriores y conserva su arquitectura principal, manteniendo la separación entre datos, modelos, servicios, interfaz gráfica y archivo principal.

En esta semana se incorporaron mejoras manteniendo las funcionalidades existentes del sistema.

Entre las principales mejoras realizadas se encuentran:

- Integración y gestión de usuarios mediante una estructura más completa.
- Incorporación de identificador, nombre, correo, nombre de usuario, contraseña, rol y estado.
- Inicio de sesión mediante nombre de usuario y contraseña.
- Validación de las credenciales ingresadas.
- Validación del estado del usuario.
- Identificación del rol del usuario.
- Registro, consulta y actualización de usuarios.
- Modificación de contraseña.
- Habilitación y deshabilitación de usuarios.
- Validación de usuarios duplicados.
- Integración de la gestión de ventas con usuarios y productos.
- Registro automático de fecha y hora en las ventas.
- Persistencia de productos, usuarios y ventas mediante archivos JSON.
- Mejora de la interfaz gráfica.
- Integración de los recursos visuales ubicados en la carpeta `assets/`.
- Aplicación de fundamentos de manejo de eventos mediante `command=` y callbacks.
- Conservación de la separación de responsabilidades entre la interfaz, los servicios, los modelos y la persistencia.

---

## Funcionalidades

### Inicio de sesión

- Inicio de sesión mediante nombre de usuario y contraseña.
- Validación de las credenciales ingresadas.
- Verificación de que el usuario se encuentre habilitado.
- Identificación del rol del usuario.
- Acceso a la ventana principal después de una autenticación correcta.
- Mensajes de error cuando las credenciales son incorrectas.

### Usuarios

- Registro de usuarios.
- Listado de usuarios registrados.
- Consulta de usuarios mediante identificador.
- Actualización de información de usuarios.
- Modificación de contraseña.
- Habilitación y deshabilitación de usuarios.
- Asignación de roles.
- Validación de usuarios duplicados.
- Almacenamiento permanente de los usuarios en JSON.
- Visualización del estado del usuario.
- El usuario con rol de Administrador tiene acceso a la gestión de usuarios.

Los usuarios manejan los siguientes datos:

- Identificador.
- Nombre.
- Correo.
- Nombre de usuario.
- Contraseña.
- Rol.
- Estado.

Los roles disponibles son:

- Administrador.
- Empleado.
- Cliente.

### Productos

- Registro de productos.
- Validación del nombre.
- Validación del precio.
- Validación para evitar productos duplicados.
- Listado de productos registrados.
- Visualización del precio con formato de moneda.
- Almacenamiento de los productos en JSON.

### Ventas

- Selección de usuario.
- Selección de producto.
- Validación de la información seleccionada.
- Registro automático de fecha y hora.
- Relación entre usuario y producto.
- Almacenamiento de las ventas en `ventas.json`.
- Listado de ventas realizadas en la interfaz.
- Actualización de la tabla después de registrar una venta.

---


## Estructura del proyecto

```text
restaurante_app_semana15/
│
├── assets/
│   ├── logo.png
│   ├── icono.png
│   └── logo original.png
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
Descripción de los módulos
modelos/

Contiene las clases principales del sistema.

producto.py

Contiene la clase Producto, encargada de representar los productos del restaurante.

Sus principales atributos son:

Nombre.
Precio.

La clase utiliza los métodos to_dict() y from_dict() para convertir objetos en estructuras compatibles con JSON y reconstruir los objetos posteriormente.

usuario.py

Contiene la clase Usuario, encargada de representar a los usuarios del sistema.

Sus atributos son:

Identificador.
Nombre.
Correo.
Nombre de usuario.
Contraseña.
Rol.
Estado.

La clase también utiliza los métodos to_dict() y from_dict() para facilitar la persistencia de los datos.

venta.py

Contiene la clase Venta, encargada de representar las ventas realizadas.

Sus datos principales son:

Usuario.
Producto.
Fecha.
servicios/

Contiene la lógica de negocio y el manejo de la información.

archivo_servicio.py

Se encarga de:

Leer archivos JSON.
Guardar información en archivos JSON.
Crear las carpetas necesarias.
Manejar archivos inexistentes.
Manejar archivos vacíos.
Manejar archivos con formato JSON incorrecto.
Controlar problemas durante la lectura o escritura de archivos.
restaurante_servicio.py

Contiene la lógica principal del sistema.

Se encarga de:

Administrar productos.
Administrar usuarios.
Validar usuarios.
Validar el inicio de sesión.
Administrar contraseñas.
Administrar roles.
Habilitar y deshabilitar usuarios.
Registrar ventas.
Consultar información.
Validar los datos antes de realizar operaciones.
Guardar los cambios en archivos JSON.
ui/

Contiene las interfaces gráficas desarrolladas con Tkinter.

login_view.py

Contiene la ventana de inicio de sesión.

Permite ingresar:

Nombre de usuario.
Contraseña.

El sistema valida las credenciales antes de permitir el acceso a la ventana principal.

main_view.py

Contiene la ventana principal del sistema.

Incluye las secciones:

Productos.
Usuarios.
Ventas.

La sección de usuarios se encuentra disponible para el usuario con rol de Administrador.

La interfaz utiliza los recursos gráficos ubicados en la carpeta assets/.

datos/

Contiene los archivos JSON utilizados para almacenar la información del sistema.

productos.json: almacena los productos.
usuarios.json: almacena los usuarios.
ventas.json: almacena las ventas realizadas.
assets/

Contiene los recursos gráficos utilizados por la aplicación.

logo.png: logotipo utilizado por la aplicación.
icono.png: icono de la aplicación.
logo original.png: logotipo utilizado como recurso gráfico.

Estos recursos forman parte de la identidad visual del sistema y son utilizados por las interfaces de la aplicación.

Datos almacenados
Productos

Ejemplo de información almacenada en productos.json:

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
Usuarios

La información de los usuarios se almacena incluyendo sus datos, credenciales, rol y estado.

Ejemplo de información almacenada en usuarios.json:

[
    {
        "identificador": "1",
        "nombre": "Administrador",
        "correo": "admin@restaurante.local",
        "nombre_usuario": "admin",
        "contrasena": "123456",
        "rol": "Administrador",
        "activo": true
    },
    {
        "identificador": "2",
        "nombre": "Nahomy Guanipatin",
        "correo": "nahomy@restaurante.local",
        "nombre_usuario": "nahomy",
        "contrasena": "123456",
        "rol": "Cliente",
        "activo": true
    },
    {
        "identificador": "3",
        "nombre": "Carlos Torres",
        "correo": "carlos@restaurante.local",
        "nombre_usuario": "carlos",
        "contrasena": "123456",
        "rol": "Empleado",
        "activo": true
    },
    {
        "identificador": "4",
        "nombre": "Juan Lopez",
        "correo": "juan@restaurante.local",
        "nombre_usuario": "juan",
        "contrasena": "123456",
        "rol": "Cliente",
        "activo": true
    }
]
Ventas

Ejemplo de información almacenada en ventas.json:

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
    },
    {
        "usuario": "Administrador",
        "producto": "Jugo Natural",
        "fecha": "2026-09-22 06:03:43"
    },
    {
        "usuario": "Juan Lopez",
        "producto": "Papas Fritas",
        "fecha": "2026-09-22 06:06:54"
    }
]
Manejo de eventos

La interfaz gráfica utiliza el parámetro command= de Tkinter para asociar los botones con funciones callback.

Los callbacks se encargan de obtener la información ingresada por el usuario, coordinar la operación solicitada y delegar la lógica de negocio al RestauranteServicio.

Las acciones de registrar productos, registrar usuarios, actualizar usuarios, cambiar contraseñas, habilitar o deshabilitar usuarios y registrar ventas se ejecutan mediante callbacks asociados a los botones de la interfaz.

El flujo general de un evento es:

Usuario interactúa con un botón
              ↓
          command=
              ↓
           Callback
              ↓
Obtención de la información
              ↓
     RestauranteServicio
              ↓
     Validación y operación
              ↓
       Actualización de datos
              ↓
      Persistencia en JSON
              ↓
    Actualización de la interfaz

De esta manera, la interfaz gráfica no concentra la lógica de negocio ni la persistencia, sino que delega estas responsabilidades al servicio correspondiente.

Requisitos

Para ejecutar el proyecto se necesita:

Python 3 instalado.
Tkinter, incluido normalmente en la instalación estándar de Python.
No se requieren paquetes externos.
Instalación

Clonar o descargar el repositorio y acceder a la carpeta del proyecto:

cd restaurante_app_semana15

Comprobar la versión de Python:

py --version
Ejecución

Para ejecutar el proyecto se utiliza:

py main.py

Al iniciar la aplicación se mostrará la ventana de inicio de sesión.

Ejemplos de ejecución
1. Inicio de sesión

Al ejecutar el programa se muestra la ventana de inicio de sesión.

Se debe ingresar un nombre de usuario y una contraseña registrados en usuarios.json.

Ejemplo:

Usuario: admin
Contraseña: 123456

Al presionar Iniciar Sesión, el sistema valida las credenciales y verifica que el usuario esté habilitado.

Si los datos son correctos, se abre la ventana principal.

2. Ventana principal

Después de iniciar sesión se muestra la aplicación principal con el título:

SISTEMA DE RESTAURANTE

La aplicación contiene las secciones:

Productos | Usuarios | Ventas

El apartado Usuarios está disponible para el usuario con rol de Administrador.

3. Registro de productos

Desde la sección Productos se puede ingresar el nombre y precio de un nuevo producto.

Ejemplo:

Nombre del producto: Hamburguesa
Precio: 3.50

Después de registrar el producto, la información se guarda en productos.json y aparece en la tabla de productos registrados.

4. Registro de usuarios

Desde la sección Usuarios, el administrador puede registrar nuevos usuarios.

Ejemplo:

Nombre: María López
Correo: maria@restaurante.local
Nombre de usuario: maria
Contraseña: 123456
Rol: Cliente

El usuario se almacena en usuarios.json y aparece en la tabla de usuarios registrados.

5. Consulta y actualización de usuarios

El administrador puede seleccionar un usuario desde la tabla y consultar o modificar sus datos.

Se pueden actualizar:

Nombre.
Correo.
Nombre de usuario.
Rol.

Después de presionar Actualizar, los cambios se guardan en usuarios.json.

6. Cambio de contraseña

El administrador puede seleccionar un usuario e ingresar una nueva contraseña.

Ejemplo:

Nueva contraseña: 789456

Al presionar Cambiar contraseña, la nueva contraseña se almacena en usuarios.json.

7. Habilitar y deshabilitar usuarios

El administrador puede cambiar el estado de un usuario mediante el botón:

Habilitar / Deshabilitar

El estado se muestra en la tabla como:

Habilitado

o:

Deshabilitado

Los usuarios deshabilitados no pueden iniciar sesión.

8. Registro de ventas

Desde la sección Ventas se selecciona un usuario y un producto.

Ejemplo:

Usuario: Nahomy Guanipatin
Producto: Hamburguesa

Al registrar la venta, el sistema genera automáticamente la fecha y hora.

Ejemplo:

2026-09-22 06:03:17

La información se almacena en ventas.json y aparece en la tabla de ventas registradas.

Persistencia de datos

La información del sistema se almacena en archivos JSON dentro de la carpeta datos/.

Los archivos utilizados son:

productos.json
usuarios.json
ventas.json

La clase ArchivoServicio se encarga de realizar las operaciones de lectura y escritura de los archivos.

Los datos permanecen almacenados aunque la aplicación se cierre.

Al volver a ejecutar el programa, la información es cargada nuevamente desde los archivos JSON.

La persistencia permite conservar los productos, usuarios y ventas registrados durante la ejecución de la aplicación.

Manejo de errores

El sistema incluye validaciones para evitar:

Productos sin nombre.
Productos con precio menor o igual a cero.
Productos duplicados.
Usuarios sin nombre.
Usuarios sin correo.
Usuarios sin nombre de usuario.
Usuarios sin contraseña.
Usuarios duplicados.
Contraseñas vacías.
Ventas sin usuario.
Ventas sin producto.
Inicio de sesión con credenciales incorrectas.
Inicio de sesión de usuarios deshabilitados.
Archivos JSON inexistentes.
Archivos JSON vacíos.
Archivos JSON con formato incorrecto.
Problemas durante la lectura o escritura de archivos.
Arquitectura

El proyecto separa las responsabilidades de la aplicación mediante diferentes capas:

Interfaz gráfica
       ↓
Servicios
       ↓
Modelos
       ↓
Archivos JSON

Esta organización permite mantener separado:

El código de la interfaz.
La lógica de negocio.
Los modelos de datos.
La persistencia de información.
Interfaz gráfica

La carpeta ui/ contiene las ventanas desarrolladas con Tkinter.

Servicios

La carpeta servicios/ contiene la lógica de negocio y las operaciones relacionadas con los datos.

Modelos

La carpeta modelos/ contiene las clases que representan las entidades principales del sistema.

Persistencia

La carpeta datos/ contiene los archivos JSON utilizados para almacenar la información.

Programación Orientada a Objetos

El proyecto aplica conceptos de Programación Orientada a Objetos mediante diferentes clases.

Clases principales
Producto
Usuario
Venta
ArchivoServicio
RestauranteServicio
LoginView
MainView

Cada clase posee responsabilidades específicas dentro del sistema.

La clase Usuario permite representar los datos completos de cada usuario, incluyendo identificador, datos personales, credenciales, rol y estado.

Los métodos to_dict() y from_dict() permiten realizar la conversión entre objetos y estructuras compatibles con JSON.

La separación mediante clases permite organizar el código y facilitar su mantenimiento.

Roles del sistema

El sistema contempla tres roles:

Administrador

Puede acceder a la gestión de usuarios y realizar operaciones como:

Registrar usuarios.
Actualizar usuarios.
Cambiar contraseñas.
Habilitar o deshabilitar usuarios.
Consultar usuarios registrados.
Empleado

El sistema identifica al usuario con rol de Empleado durante el inicio de sesión y permite acceder a las funciones habilitadas para dicho usuario.

Cliente

El sistema identifica al usuario con rol de Cliente durante el inicio de sesión y permite acceder a las funciones habilitadas para dicho usuario.

La aplicación identifica el rol del usuario al momento de iniciar sesión.

Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando Tkinter.

El diseño incluye:

Encabezado principal.
Logotipo.
Nombre del sistema.
Información del usuario conectado.
Rol del usuario.
Pestañas para las diferentes funciones.
Formularios para ingreso de información.
Tablas para visualizar los registros.
Botones para ejecutar las operaciones.
Colores diferenciados para las principales acciones.
Recursos gráficos mediante la carpeta assets/.

La interfaz mantiene una identidad visual uniforme entre la ventana de inicio de sesión y la ventana principal.

La aplicación utiliza los archivos gráficos:

logo.png
icono.png
logo original.png

ubicados en la carpeta assets/.

Flujo general del sistema
Ejecutar main.py
       ↓
Inicio de sesión
       ↓
Ingresar usuario y contraseña
       ↓
Validación de credenciales
       ↓
Validación del estado del usuario
       ↓
Identificación del rol
       ↓
Ventana principal
       ↓
┌─────────────┬─────────────┬─────────────┐
│  Productos  │  Usuarios   │   Ventas    │
└─────────────┴─────────────┴─────────────┘
       ↓
Procesamiento mediante servicios
       ↓
Actualización de modelos
       ↓
Guardar información en JSON
       ↓
Actualizar la interfaz
Gestión de ventas

La gestión de ventas permite relacionar un usuario con un producto registrado.

El proceso se realiza de la siguiente manera:

El usuario selecciona un usuario registrado.
Selecciona un producto registrado.
La interfaz ejecuta el callback correspondiente mediante command=.
El callback obtiene la información seleccionada.
La operación es delegada al RestauranteServicio.
El servicio valida que el usuario y producto sean válidos.
Se genera automáticamente la fecha y hora.
Se crea el objeto Venta.
La venta se almacena en ventas.json.
La interfaz actualiza la tabla de ventas.

De esta forma, la interfaz se encarga de la interacción con el usuario, mientras que el servicio administra la lógica de negocio y la persistencia.

Estado del proyecto

Proyecto académico funcional desarrollado en Python como práctica de Programación Orientada a Objetos y manejo de eventos en interfaces gráficas.

El sistema integra:

Programación Orientada a Objetos.
Interfaz gráfica con Tkinter.
Manejo de eventos mediante command= y callbacks.
Gestión de usuarios.
Identificador y datos completos de usuarios.
Roles y estados.
Inicio de sesión.
Gestión de productos.
Registro de ventas.
Relación entre usuarios y productos.
Persistencia de información mediante archivos JSON.
Validaciones de datos.
Separación de responsabilidades mediante capas.
Recursos visuales mediante la carpeta assets/.
Continuidad de la arquitectura desarrollada en semanas anteriores.
Proyecto académico

Este proyecto corresponde al desarrollo de la Semana 15 de la asignatura Programación Orientada a Objetos.

La implementación mantiene la arquitectura y funcionalidades previamente desarrolladas y agrega mejoras relacionadas con la gestión de ventas, manejo de eventos, persistencia, organización de usuarios e integración de la interfaz gráfica.