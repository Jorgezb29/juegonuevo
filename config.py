import os
from decouple import config  # Para usar variables de entorno

class Config:
    SECRET_KEY = config('SECRET_KEY', default='your-secret-key')
    SQLALCHEMY_DATABASE_URI = f"mysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@{config('MYSQL_HOST')}/{config('MYSQL_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Prueba de carga de variables de entorno (esto solo es útil para pruebas locales)
if __name__ == "__main__":
    try:
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
