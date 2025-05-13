from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Lista de tarefas (simples, sem banco de dados)
tasks = []

ARQUIVO = 'tarefas.json'

def salvar_tarefas():
    """
    Salva a lista de tarefas atual no arquivo JSON.

    O nome do arquivo é definido pela variável global ARQUIVO.
    """
    with open(ARQUIVO, 'w') as f:
        json.dump(tasks, f, indent=4)

def carregar_tarefas():
    """Carrega a lista de tarefas no arquivo JSON."""
    global tasks
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            tasks = json.load(f)
    
# Opção 1 - para carregar a lista
# nova_lista = carregar_tarefas()

@app.route('/')
def home():
    """Testa se a API está funcionando"""
    return "API de Lista de Tarefas - Está funcionando!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """retorna a lista de tarefas"""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Cria uma tarefa"""
    data = request.get_json()  # Pega o JSON enviado na requisição

    # Cria um novo dicionário representando a tarefa
    nova_tarefa = {
        "id": max([t['id'] for t in tasks], default=0) + 1,
        'titulo': data.get('titulo'),
        'status': data.get('status', 'pendente')  # status padrão = pendente
    }

    tasks.append(nova_tarefa)  # Adiciona a tarefa na lista    
    salvar_tarefas()

    return jsonify(nova_tarefa), 201   # 201 = Created

# Para testar o POST use isso no CMD:
# curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"titulo\":\"Estudar Python\"}"

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Procura a tarefa pelo id"""
    tarefa = next((task for task in tasks if task['id'] == task_id), None)

    if tarefa:
        return jsonify(tarefa)
    else:
        return jsonify({"mensagem": "Tarefa nao encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza a tarefa pelo id"""
    data = request.get_json()  # Pega o JSON enviado
    tarefa = next((task for task in tasks if task['id'] == task_id), None)

    if tarefa:
        # Atualiza os campos (se foram enviados)
        tarefa['titulo'] = data.get('titulo', tarefa['titulo'])
        tarefa['status'] = data.get('status', tarefa['status'])
        salvar_tarefas()
        return jsonify(tarefa)
    else:
        return jsonify({"mensagem": "Tarefa nao encontrada"}), 404

# Para testar o PUT use isso no CMD:
#curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d "{\"titulo\":\"Estudar Flask\",\"status\":\"concluida\"}"

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Deleta a tarefa pelo id"""
    global tasks
    nova_lista = [task for task in tasks if task['id'] != task_id]

    if len(nova_lista) != len(tasks):
        tasks = nova_lista
        salvar_tarefas()
        return jsonify({"mensagem": "Tarefa excluída com sucesso"})
    else:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

# Para testar o DELETE use isso no CMD:
# curl -X DELETE http://127.0.0.1:5000/tasks/1

if __name__ == '__main__':
    # Opção 2 - para carregar a lista
    carregar_tarefas()
    app.run(debug=True)
