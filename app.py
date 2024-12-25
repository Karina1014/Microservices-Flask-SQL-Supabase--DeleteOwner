from flask import Flask
from Routes.deleteOwnerRoutes import delete_owner_bp

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Registrar las rutas de eliminación de propietario
app.register_blueprint(delete_owner_bp)

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
