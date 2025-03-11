import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto de Render
    app.run(host="0.0.0.0", port=port)  # Asegurar que escuche en todas las interfaces
