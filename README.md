# Gerenciamento de Tarefas - Back-End

## Descrição
Este projeto é a API do sistema de gerenciamento de tarefas, desenvolvido com FastAPI e MongoDB. Ele fornece todos os endpoints necessários para a autenticação, criação, edição, exclusão e consulta de tarefas.

## Endpoints Disponíveis

### 1. **Autenticação**
- **`POST /login`**
  - Realiza a autenticação do usuário.
  - Retorna um token JWT válido para acesso aos outros endpoints.

### 2. **Tarefas**
- **`GET /tasks`**
  - Retorna todas as tarefas associadas ao usuário autenticado.
  - Requer um token JWT válido no cabeçalho de autorização.

- **`POST /tasks`**
  - Cria uma nova tarefa.
  - Campos obrigatórios:
    - `title`: Título da tarefa.
    - `description`: Descrição da tarefa.
    - `status`: Status atual (`pendente`, `emProgresso`, `finalizada`).
    - `priority`: Prioridade (`baixa`, `média`, `alta`).
    - `due_date`: Data de conclusão da tarefa.

- **`PUT /tasks/{task_id}`**
  - Atualiza uma tarefa existente.
  - Requer o ID da tarefa e os campos a serem atualizados.

- **`DELETE /tasks/{task_id}`**
  - Exclui uma tarefa pelo ID.
  - Requer um token JWT válido.

### 3. **Filtros**
- **`GET /tasks?status={status}&priority={priority}`**
  - Permite filtrar as tarefas por status, prioridade ou ambos.
  - Exemplo: `/tasks?status=pendente&priority=alta`.

## Tecnologias Utilizadas
- **FastAPI**: Framework para desenvolvimento rápido de APIs.
- **MongoDB**: Banco de dados NoSQL.
- **PyJWT**: Gerenciamento de tokens JWT.
- **MongoEngine**: ODM para interação com o MongoDB.

## Como Executar
1. Clone o repositório.
2. Configure as variáveis de ambiente, incluindo a URI do MongoDB.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Execute o servidor com `uvicorn main:app --reload`.
