# Proyecto Unidad 04 [Aula 05]
Este es un proyecto de Silabuz Academy del Curso MPTE BE de la Unidad 01.


## Proyecto
Se presenta el proyecto del portafolio personal, donde se hace uso del Framework Django, sus utilidades y sus conexiones a DB, asimismo el uso de sesiones y registro de usuarios, por último la obtencion de IP para fines estadísticos.


## Pre-requisitos 📋
Para que el proyecto funcione correctamente, se deben tener en cuenta varios aspectos:
- Contar con una versión de Python y PIP dentro del sistema
- Contar con un módulo de entornos virtuales (virtualenv recomendado)


## Instalación
Iniciar creando el entorno virtual para el despliegue
```py
pip install virtualenv
```

Crear y activar entorno virtual
```bash
virtualenv env

Linux:
source env/bin/activate

Windows:
env\Scripts\activate.bat
```

Instalar requirements.txt
```py
pip install -r requirements.txt
```

Crear archivo <code>SQLite3</code> para la base de datos
```bash
touch db.sqlite3
```

Crear archivo <code>.env</code> en la misma carpeta que <code>zproject</code> para variables de entorno
```bash
touch .env
```

Agregue una clave secreta, como se hace en el ejemplo siguiente
```
SECRET_KEY=Esta_es_el_password
```

Realice las migraciones correspondientes para las bases de datos
```bash
python manage.py makemigrations
python manage.py migrate
```


## Despliegue 📦

Abrir shell, ubicarse en la carpeta que contiene la carpeta <code>env, zproject, ... </code>:
```bash
python manage.py runserver
```


## Autor ✒️
- **Jean Franco Tineo** - [tineodev](https://github.com/tineodev)
