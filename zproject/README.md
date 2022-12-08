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

Crear archivo SQLite3 para la base de datos
```py
touch db.sqlite3
```

## Despliegue 📦

En la consola, ubicarse en la carpeta que contiene la carpeta <code>env, zproject, ... </code>:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Autor ✒️
- **Jean Franco Tineo** - [tineodev](https://github.com/tineodev)
