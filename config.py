import os
from decouple import config  # Para usar variables de entorno

# Obtener la ruta base del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para la aplicación (usar una clave segura en producción)
    SECRET_KEY = config('SECRET_KEY', default='your-secret-key')

    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = f"mysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@{config('MYSQL_HOST')}/{config('MYSQL_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Evitar advertencias de Flask-SQLAlchemy

# Prueba de carga de variables de entorno
if __name__ == "__main__":
    try:
        # Prueba de carga de variables de entorno
        SECRET_KEY = config('SECRET_KEY')
        MYSQL_HOST = config('MYSQL_HOST')
        MYSQL_USER = config('MYSQL_USER')
        MYSQL_PASSWORD = config('MYSQL_PASSWORD')
        MYSQL_DB = config('MYSQL_DB')
        print("Variables de entorno cargadas correctamente:")
        print(f"SECRET_KEY: {SECRET_KEY}")
        print(f"MYSQL_HOST: {MYSQL_HOST}")
        print(f"MYSQL_USER: {MYSQL_USER}")
        print(f"MYSQL_PASSWORD: {MYSQL_PASSWORD}")
        print(f"MYSQL_DB: {MYSQL_DB}")
    except Exception as e:
        print(f"Error al cargar variables de entorno: {e}")