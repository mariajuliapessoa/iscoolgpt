from flask import Blueprint, jsonify

conteudos_bp = Blueprint('conteudos', __name__)

# Mock de conteúdos
todos_conteudos = [
    {"id": 1, "titulo": "Funções em Python"},
    {"id": 2, "titulo": "Estruturas de Dados"}
]

@conteudos_bp.route('/api/conteudos', methods=['GET'])
def listar_conteudos():
    return jsonify(todos_conteudos)
