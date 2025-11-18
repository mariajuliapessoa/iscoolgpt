from flask import Blueprint, jsonify, request
import google.generativeai as genai
import os

perguntas_bp = Blueprint('perguntas', __name__)

# Configura a API key do Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# USA O MODELO CORRETO DA LISTA
model = genai.GenerativeModel('models/gemini-2.5-flash')

@perguntas_bp.route('/api/pergunta', methods=['POST'])
def criar_pergunta():
    data = request.get_json()
    
    texto_pergunta = data.get('texto', '')
    
    if not texto_pergunta:
        return jsonify({"erro": "Pergunta vazia"}), 400
    
    try:
        # Adiciona contexto educacional
        prompt = f"""Você é um assistente educacional especializado em ajudar alunos.
Responda de forma clara, didática e em português.

Pergunta do aluno: {texto_pergunta}"""
        
        # Chama o Gemini
        response = model.generate_content(prompt)
        resposta_llm = response.text
        
        return jsonify({
            "pergunta": texto_pergunta,
            "resposta": resposta_llm
        }), 200
        
    except Exception as e:
        return jsonify({"erro": f"Erro ao processar: {str(e)}"}), 500
