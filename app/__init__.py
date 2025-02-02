from flask import Flask
from app.blueprints.auth import auth_bp
from app.blueprints.main import main_bp

def create_app():
    app = Flask(__name__)
    
    # Registrando os Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app