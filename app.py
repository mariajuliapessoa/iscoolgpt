from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

from routes.conteudos import conteudos_bp
from routes.perguntas import perguntas_bp


def create_app():
    app = Flask(__name__)

    # registra blueprints
    app.register_blueprint(conteudos_bp)
    app.register_blueprint(perguntas_bp)

    # Rota inicial
    @app.route('/')
    def home():
        return jsonify({'message': 'Bem-vindo ao iscoolgpt-backend!'})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8080)
