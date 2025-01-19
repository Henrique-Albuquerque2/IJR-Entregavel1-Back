from fastapi import FastAPI
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import dotenv
from importlib import import_module
from config.config import config  # Importa o arquivo de configuração

# Carregar variáveis de ambiente
dotenv.load_dotenv()

# Conectar ao banco de dados MongoDB
connect(
    host=f"mongodb+srv://{config['mongo_user']}:{config['mongo_pwd']}@{config['mongo_host']}/?retryWrites=true&w=majority"
)

# Instanciar o aplicativo FastAPI
app = FastAPI()

# Teste de conexão
@app.get("/")
def test():
    return {"status": "OK v2 (3)"}

# Configurar CORS para permitir comunicações do front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Front-end no localhost
        "http://127.0.0.1:5173",  # Front-end no IP local
    ],
    allow_credentials=True,               # Permitir envio de cookies ou headers de autenticação
    allow_methods=["*"],                  # Permitir todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                  # Permitir todos os headers
)

# Obtém o diretório atual onde o arquivo app.py está localizado
working_directory = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para o diretório onde os "use_cases" (casos de uso) estão localizados
use_cases_directory = os.path.join(working_directory, "use_cases")

# Procura recursivamente por arquivos index.py dentro dos diretórios de casos de uso
routes = glob.glob(os.path.join(use_cases_directory, "**/*.py"), recursive=True)

# Importa e registra automaticamente as rotas definidas em cada arquivo index.py
for route in routes:
    # Converte o caminho do arquivo em um nome de módulo relativo
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')
    try:
        # Importa dinamicamente o módulo
        module = import_module(module_name)
        # Se o módulo possui um objeto 'router', inclui as rotas no aplicativo FastAPI
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        # Exibe uma mensagem de erro caso o módulo não seja encontrado
        print(f"Erro ao importar módulo {module_name}: {e}")
