# IsCoolGPT Backend

![CI/CD](https://github.com/mariajuliapessoa/iscoolgpt/actions/workflows/ci-cd.yml/badge.svg)

Assistente educacional inteligente desenvolvido com Flask e integração com Google Gemini AI. O sistema permite que alunos façam perguntas e recebam respostas didáticas personalizadas através de uma API RESTful.

## Índice

- [Tecnologias](#-tecnologias)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Como Executar](#-como-executar)
- [Endpoints da API](#-endpoints-da-api)
- [Testando a API](#-testando-a-api)
- [Docker](#-docker)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Segurança](#-segurança)
- [Logs](#-logs)
- [Autora](#-autora)

## Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

- **Python 3.11** - Linguagem de programação
- **Flask 3.0+** - Framework web minimalista
- **Google Generative AI (Gemini 2.5)** - Modelo de linguagem para respostas inteligentes
- **Docker** - Containerização da aplicação
- **Git/GitHub** - Controle de versão

### Bibliotecas Python utilizadas:
- `flask` - Framework web
- `google-generativeai` - Cliente da API Gemini
- `python-dotenv` - Gerenciamento de variáveis de ambiente

## Funcionalidades

- API RESTful para assistente educacional
- Integração com LLM (Google Gemini 2.5-flash)
- Sistema de logs automático de todas as requisições
- Arquitetura modular com Blueprints (Flask)
- Dockerização completa
- Respostas contextualizadas e didáticas
- Tratamento de erros robusto

## Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

### Obrigatórios:
- **Python 3.10 ou superior** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Conta Google** - Para obter API Key do Gemini

### Opcionais (mas recomendados):
- **Docker Desktop** - [Download Docker](https://www.docker.com/products/docker-desktop) (para executar em container)
- **VS Code** - [Download VS Code](https://code.visualstudio.com/) (editor de código)
- **Thunder Client** (extensão do VS Code) ou **Postman** - Para testar a API

### Obter API Key do Google Gemini:
1. Acesse: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada (formato: `AIzaSy...`)
5. Guarde em local seguro

## 🔧 Instalação

### 1. Clone o repositório

git clone https://github.com/mariajuliapessoa/iscoolgpt.git
cd iscoolgpt

text

### 2. Crie e ative o ambiente virtual

**Windows (PowerShell):**
python -m venv venv
.\venv\Scripts\Activate

text

**Linux/Mac:**
python3 -m venv venv
source venv/bin/activate

text

### 3. Instale as dependências

pip install -r requirements.txt

text

Pacotes que serão instalados:
- Flask
- google-generativeai
- python-dotenv

## ⚙️ Configuração

### 1. Crie o arquivo de variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

Windows
type nul > .env

Linux/Mac
touch .env

text

### 2. Configure a API Key

Abra o arquivo `.env` e adicione:

GEMINI_API_KEY=sua-chave-aqui

text

** IMPORTANTE:** Substitua `sua-chave-aqui` pela sua chave real do Google Gemini.

**Exemplo:**
GEMINI_API_KEY=AIzaSyBCEh1234567890abcdefghijklmnopqrs

text

### 3. Verificar configuração

O arquivo `.env` **não** deve ser commitado no Git. Verifique se está no `.gitignore`:

cat .gitignore | findstr .env # Windows
grep .env .gitignore # Linux/Mac

text

## Como Executar

### Modo desenvolvimento (local)

1. Certifique-se de que o ambiente virtual está ativo
2. Execute:

python app.py

text

3. A aplicação estará rodando em: `http://localhost:5000`

Você verá no terminal:
Serving Flask app 'app'

Debug mode: on

Running on http://127.0.0.1:5000

text

### Parar a aplicação

Pressione `Ctrl + C` no terminal

## 📡 Endpoints da API

### 1. `GET /`
Rota de boas-vindas

**Exemplo de requisição:**
GET http://localhost:5000/

text

**Resposta:**
{
"message": "Bem-vindo ao iscoolgpt-backend!"
}

text

---

### 2. `GET /api/conteudos`
Lista conteúdos educacionais disponíveis

**Exemplo de requisição:**
GET http://localhost:5000/api/conteudos

text

**Resposta:**
[
{
"id": 1,
"titulo": "Funções em Python"
},
{
"id": 2,
"titulo": "Estruturas de Dados"
}
]

text

---

### 3. `POST /api/pergunta`
Envia uma pergunta para o assistente educacional com IA

**Exemplo de requisição:**
POST http://localhost:5000/api/pergunta
Content-Type: application/json

{
"texto": "O que é uma função em Python?"
}

text

**Resposta:**
{
"pergunta": "O que é uma função em Python?",
"resposta": "Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica. Ela é definida usando a palavra-chave 'def', seguida do nome da função e parênteses. As funções ajudam a organizar o código, tornam-no mais legível e facilitam a reutilização."
}

text

**Possíveis erros:**

- **400 Bad Request** - Pergunta vazia
{
"erro": "Pergunta vazia"
}

text

- **500 Internal Server Error** - Erro ao processar com a LLM
{
"erro": "Erro ao processar: [detalhes do erro]"
}

text

## Testando a API

### Opção 1: Thunder Client (VS Code)

1. Instale a extensão **Thunder Client** no VS Code
2. Clique no ícone do raio (⚡) na barra lateral
3. Clique em **"New Request"**
4. Configure a requisição:

**Para GET /api/conteudos:**
- Método: `GET`
- URL: `http://localhost:5000/api/conteudos`
- Clique em **Send**

**Para POST /api/pergunta:**
- Método: `POST`
- URL: `http://localhost:5000/api/pergunta`
- Aba **Body** → Selecione **JSON**
- Cole:
{
"texto": "O que é Docker?"
}

text
- Clique em **Send**

### Opção 2: Postman

1. Baixe e instale: [Postman](https://www.postman.com/downloads/)
2. Crie uma nova requisição
3. Configure conforme os exemplos acima
4. Clique em **Send**

### Opção 3: cURL (Terminal)

**GET /api/conteudos:**
curl http://localhost:5000/api/conteudos

text

**POST /api/pergunta:**

**Windows (PowerShell):**
Invoke-RestMethod -Uri http://localhost:5000/api/pergunta -Method POST -ContentType "application/json" -Body '{"texto": "O que é Python?"}'

text

**Linux/Mac:**
curl -X POST http://localhost:5000/api/pergunta
-H "Content-Type: application/json"
-d '{"texto": "O que é Python?"}'

text

### Opção 4: Navegador (apenas GET)

Acesse diretamente no navegador:
- `http://localhost:5000/`
- `http://localhost:5000/api/conteudos`

## Docker

### Pré-requisitos
- Docker Desktop instalado e rodando

### Build da imagem

docker build -t iscoolgpt-backend .

text

Isso pode levar alguns minutos na primeira vez.

### Executar o container

docker run -p 5000:5000 --env-file .env iscoolgpt-backend

text

**Parâmetros:**
- `-p 5000:5000` - Mapeia a porta 5000 do container para a porta 5000 do host
- `--env-file .env` - Carrega variáveis de ambiente do arquivo `.env`
- `iscoolgpt-backend` - Nome da imagem

### Executar em background (detached)

docker run -d -p 5000:5000 --env-file .env --name iscoolgpt iscoolgpt-backend

text

### Comandos úteis do Docker

Listar containers rodando
docker ps

Ver logs do container
docker logs iscoolgpt

Parar container
docker stop iscoolgpt

Remover container
docker rm iscoolgpt

Listar imagens
docker images

Remover imagem
docker rmi iscoolgpt-backend

text

## Estrutura do Projeto

iscoolgpt-backend/
│
├── routes/ # Módulo de rotas (Blueprints)
│ ├── init.py # Inicializa o pacote routes
│ ├── conteudos.py # Endpoints relacionados a conteúdos
│ └── perguntas.py # Endpoints do assistente (integração LLM)
│
├── app.py # Aplicação principal Flask
├── requirements.txt # Dependências do projeto
├── Dockerfile # Configuração para containerização
├── .dockerignore # Arquivos ignorados pelo Docker
├── .gitignore # Arquivos ignorados pelo Git
├── .env # Variáveis de ambiente (NÃO COMMITAR)
├── request_logs.txt # Logs automáticos de requisições
└── README.md # Documentação do projeto

text

### Descrição dos arquivos principais:

- **app.py**: Ponto de entrada da aplicação. Configura Flask, registra Blueprints e middleware de logging.
- **routes/conteudos.py**: Define endpoint GET para listar conteúdos educacionais.
- **routes/perguntas.py**: Define endpoint POST para enviar perguntas ao assistente com IA (Gemini).
- **requirements.txt**: Lista todas as dependências Python necessárias.
- **Dockerfile**: Define como construir a imagem Docker da aplicação.
- **.env**: Armazena variáveis sensíveis (API keys). **Nunca** deve ser commitado.

## Segurança

### Boas práticas implementadas:

✅ **Variáveis de ambiente**: API keys armazenadas em `.env`, não no código  
✅ **`.gitignore`**: Impede commit de arquivos sensíveis (`.env`, `venv/`, logs)  
✅ **`.dockerignore`**: Não inclui arquivos desnecessários na imagem Docker  
✅ **Tratamento de erros**: Mensagens genéricas para o usuário, logs detalhados  
✅ **Logs de auditoria**: Todas as requisições são registradas  

### Avisos importantes:

- **Nunca** compartilhe seu arquivo `.env` ou API key
- **Nunca** commite o `.env` no Git
- Em produção, use serviços como **AWS Secrets Manager** ou **Azure Key Vault**
- Desative `debug=True` em produção

## Logs

A aplicação gera logs automáticos de todas as requisições em `request_logs.txt`.

### Formato do log:

{
"timestamp": "2025-11-18 09:00:00.123456",
"method": "POST",
"endpoint": "/api/pergunta",
"query_params": {},
"body": {"texto": "O que é Python?"},
"ip": "127.0.0.1"
}

text

### Visualizar logs:

Ver últimas 10 linhas
tail -n 10 request_logs.txt # Linux/Mac
Get-Content request_logs.txt -Tail 10 # Windows PowerShell

Ver em tempo real
tail -f request_logs.txt # Linux/Mac
Get-Content request_logs.txt -Wait # Windows PowerShell

text

## Autora

**Maria Julia Pessoa**

- GitHub: [@mariajuliapessoa](https://github.com/mariajuliapessoa)
- Projeto: Trabalho Final - Cloud Computing 25.2
- Instituição: CESAR School

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte da cadeira de Cloud Computing