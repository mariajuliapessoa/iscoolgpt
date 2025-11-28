from flask import Flask, jsonify, request
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()

from routes.conteudos import conteudos_bp
from routes.perguntas import perguntas_bp


def create_app():
    app = Flask(__name__)

    @app.before_request
    def log_all_requests():
        log_data = {
            "timestamp": str(datetime.utcnow()),
            "method": request.method,
            "endpoint": request.path,
            "query_params": request.args.to_dict(),
            "body": request.get_json(silent=True),
            "ip": request.remote_addr
        }

        with open("request_logs.txt", "a") as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
    
    app.register_blueprint(conteudos_bp)
    app.register_blueprint(perguntas_bp)

    # Rota inicial
    @app.route('/')
    def home():
        return jsonify({'message': 'Bem-vindo ao iscoolgpt-backend!'})

    return app

if __name__ == "__main__":
    app = create_app()
app.run(debug=True, host='0.0.0.0',  port=8080)
