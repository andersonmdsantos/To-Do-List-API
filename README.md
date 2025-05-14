# To-Do-List
Este repositório foi criado para praticar conceitos de desenvolvimento de APIs RESTful utilizando Flask. A aplicação simula uma lista de tarefas (To-Do List) simples, permitindo que os usuários adicionem, editem, excluam e visualizem suas tarefas.

# Funcionalidades
A API oferece os seguintes endpoints:

- `GET /tasks`
Retorna uma lista de todas as tarefas cadastradas.

Resposta:

200 OK: Retorna a lista de tarefas (em formato JSON).

- `POST /tasks`
Adiciona uma nova tarefa à lista.
Requisição:
```json
{
    "titulo": "Sua tarefa aqui",
    "status": "pendente" // Opcional, valor padrão é "pendente"
}
```
Resposta:

201 Created: Retorna a tarefa criada (em formato JSON).

- `GET /tasks/{id}`
Retorna os detalhes de uma tarefa específica pelo id.

Resposta:

200 OK: Retorna a tarefa (em formato JSON).

404 Not Found: Caso a tarefa com o id não exista.

- `PUT /tasks/{id}`
Atualiza os dados de uma tarefa existente.

Requisição:
```json
{
    "titulo": "Novo título",
    "status": "concluída"
}
```
Resposta:

200 OK: Retorna a tarefa atualizada.

- `DELETE /tasks/{id}`
Exclui uma tarefa pelo id.

Resposta:

200 OK: Retorna uma mensagem de confirmação da exclusão.

404 Not Found: Caso a tarefa com o id não exista.

## Para executar a API, você precisa ter:

- `Python 3.10 ou superior`

- `Flask instalado`

## Instalando as dependências
Recomenda-se utilizar um ambiente virtual para evitar conflitos com outras dependências.
Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

## Como Executar
1 - Após fazer o clone do repositório, navegue até a pasta do projeto:
```
cd /caminho/para/seu/projeto
```

2 - Execute o servidor Flask:
```
python app.py
```

3 - A API estará rodando em http://127.0.0.1:5000/.

## Como Testar
-  Página inicial (funcionamento da API):
Abra o navegador e acesse http://127.0.0.1:5000/ para ver uma mensagem dizendo: "API de Lista de Tarefas - Está funcionando!"

 - Listar tarefas:
Acesse http://127.0.0.1:5000/tasks no seu navegador ou use o curl:
```
curl http://127.0.0.1:5000/tasks
```

 - Adicionar uma nova tarefa:

1. Utilize o script test_post.py para adicionar uma tarefa automaticamente, ou

2. Execute o seguinte comando curl no terminal:
```
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"titulo\":\"Estudar Flask\"}"
```

 - Estrutura de Arquivos

1. `app.py`: Arquivo principal que contém a lógica da API.

2. `test_post.py`: Script de teste para adicionar uma tarefa via POST.

3. `tarefas.json`: Arquivo onde as tarefas são armazenadas localmente.

## Licença
Esse projeto é de código aberto. Você pode usar, modificar e distribuir de acordo com os termos da MIT License.