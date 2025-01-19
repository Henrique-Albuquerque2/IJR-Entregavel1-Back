import os
import dotenv

# Carregar variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

config = {
    "environment": os.getenv("ENVIRONMENT", "dev"),  # Define o ambiente padrão como "dev"
    "client_url": "http://localhost:5173" if os.getenv("ENVIRONMENT") == "dev" else os.getenv("CLIENT_URL", ""),
    "mongo_user": os.getenv("MONGO_USER"),
    "mongo_pwd": os.getenv("MONGO_PWD"),
    "mongo_host": os.getenv("MONGO_HOST", "clusteraula.ho8si.mongodb.net"),
}
