# Django_API
API en Django
Este proyecto es una API RESTful construida con Django y Django REST Framework (DRF).
La API maneja la gestión de tareas para usuarios con manejo de JWT.

# **Instrucciones para la instalación de la API**
## Clonación del projecto
Para clonar el proyeco ejecuta en la carpeta de tu preferencia:
```git clone https://github.com/juliandross/Django_API.git```

## Si no tienes python instalado
En la terminal ejecuta: python
Para verificar si python se instaló correctamente entonces ejecuta este comando: ```python --version```

## Instalación de requerimientos del proyecto 
Con este comando podrás ejecutar las dependencias de la API: ```pip install -r requirements.txt```

Dependencias que se descargaran con requirements.txt:<br>

- Python 3.11.6
- asgiref==3.8.1
- attrs==25.1.0
- Django==5.1.6
- django-filter==25.1
- djangorestframework==3.15.2
- djangorestframework_simplejwt==5.4.0
- drf-spectacular==0.28.0
- drf-yasg==1.21.8
- inflection==0.5.1
- jsonschema==4.23.0
- jsonschema-specifications==2024.10.1
- packaging==24.2
- PyJWT==2.10.1
- pytz==2025.1
- PyYAML==6.0.2
- referencing==0.36.2
- rpds-py==0.23.1
- sqlparse==0.5.3
- typing_extensions==4.12.2
- tzdata==2025.1
- uritemplate==4.1.1

# **Para ejecutar la API**
- Para poner en marcha la api, en el directorio raiz del proyecto se ejecuta el comando: ```python manage.py runserver```
- Para revisar el resultado de los test ejecuta el comando: ```python manage.py test```

# **Para probar el funcionamiento de la api**
No tiene una interfaz gráfica como tal, sin embargo utilizo la proporcionada por DRF para probar los endpoints.<br>
Así que todo los servicios ofrecidos por la api deberan ser consultados en un navegador en ```localhost:8000.```<br>
Primero el usuario deberá registrarse: ```localhost:8000/api/register.```<br>
Luego del registro puede hacer el login en el boton login de la esquina superior derecha<br>
Una vez registrado y logeado podrá acceder a los diferentes endpoints que tiene la API:
### Consultar una tarea en especifico
```- localhost:8000/api/task/{id}```
### Consultar todas las tareas del usuario
```- localhost:8000/api/task```
### Agregar una tarea
-``` localhost:8000/api/task (En la parte inferior de la pantalla se mostrara el formulario)```
### Modificar una tarea
```- localhost:8000/api/task/{id} (En la parte inferior de la pantalla se mostrara el formulario)```
### Eliminar una tarea
```- localhost:8000/api/task/{id} (En la parte inferior de la pantalla se mostrara el formulario)```

# **Documentación**
Para revisar la documentación puede hacerlo con<br>
```- localhost:8000/api/doc```
o también con
```- localhost:8000/api/redoc```

## **Nota importante**
Ya hay datos precargados para hacer algunas pruebas
### Usuario
Nombre: usuario1 - Contraseña: 123456
#### Tareas
-1<br>
"id": 3,
"title": "tituloBonitoModificado"
-2<br>
"id": 5,
"title": "otroTitulo"

### Usuario
Nombre: usuario2 - Contraseña: 12345678
#### Tareas
-1<br>
"id": 4,
"title": "tareaDelUsuario2"

#### Usuario
Nombre: admin - Contraseña 1234
#### Tareas
-1<br>
"id": 1,
"title": "titulo1"
-2<br>
"id": 2,
"title": "titulo12"
