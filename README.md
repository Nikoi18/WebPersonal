# WebPersonal - Portafolio Personal

Este es un proyecto de portafolio personal desarrollado con Django, diseñado para mostrar proyectos, habilidades e información de contacto.

## Características

*   **Página de Inicio:** Bienvenida y resumen.
*   **Acerca de Mí:** Información personal y profesional.
*   **Portafolio:** Muestra de proyectos con descripciones, imágenes y enlaces.
*   **Contacto:** Formulario o información de contacto.
*   **Panel de Administración:** Para gestionar el contenido de los proyectos fácilmente.

## Tecnologías Utilizadas

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS y potencialmente JavaScript
*   **Base de Datos:** SQLite (por defecto en desarrollo)

## Requisitos Previos

*   Python 3.x
*   Pip (manejador de paquetes de Python)
*   Git

## Instalación y Configuración

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/WebPersonal.git
    cd WebPersonal
    ```

2.  **Crea y activa un entorno virtual** (recomendado):
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Necesitarás crear un archivo `requirements.txt`. Puedes generarlo con `pip freeze > requirements.txt` una vez tengas todas las dependencias instaladas en tu entorno virtual, como Django).*

4.  **Realiza las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario** (para acceder al panel de administración):
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear tu usuario administrador.

## Ejecución del Proyecto

1.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

2.  Abre tu navegador y ve a `http://127.0.0.1:8000/`.
3.  Para acceder al panel de administración, ve a `http://127.0.0.1:8000/admin/`
