from flask import Flask

def create_app():
    app = Flask(__name__)

    # Cargar configuración desde un objeto de configuración
    app.config.from_object('config.Config')

    # Registrar rutas desde un blueprint (asegúrate de tener el blueprint en otro archivo)
    from .routes import main  # Asegúrate de que 'routes' y 'main' existan
    app.register_blueprint(main)

    return app
