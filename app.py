from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas (simples, sem banco de dados)
tasks = []

@app.route('/')
def home():
    return "API de Lista de Tarefas - Está funcionando!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()  # Pega o JSON enviado na requisição

    # Cria um novo dicionário representando a tarefa
    nova_tarefa = {
        "id": len(tasks) + 1,
        "titulo": data['titulo'],
        "status": "pendente"   # Por padrão, nova tarefa começa pendente
    }

    tasks.append(nova_tarefa)  # Adiciona a tarefa na lista

    return jsonify(nova_tarefa), 201   # 201 = Created

# Para testar o POST use isso no CMD:
# curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"titulo\":\"Estudar Python\"}"

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Procura a tarefa pelo id
    tarefa = next((task for task in tasks if task['id'] == task_id), None)

    if tarefa:
        return jsonify(tarefa)
    else:
        return jsonify({"mensagem": "Tarefa nao encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()  # Pega o JSON enviado
    tarefa = next((task for task in tasks if task['id'] == task_id), None)

    if tarefa:
        # Atualiza os campos (se foram enviados)
        tarefa['titulo'] = data.get('titulo', tarefa['titulo'])
        tarefa['status'] = data.get('status', tarefa['status'])
        return jsonify(tarefa)
    else:
        return jsonify({"mensagem": "Tarefa nao encontrada"}), 404

# Para testar o PUT use isso no CMD:
#curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d "{\"titulo\":\"Estudar Flask\",\"status\":\"concluida\"}"

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    nova_lista = [task for task in tasks if task['id'] != task_id]

    if len(nova_lista) != len(tasks):
        tasks = nova_lista
        return jsonify({"mensagem": "Tarefa excluída com sucesso"})
    else:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

# Para testar o DELETE use isso no CMD:
# curl -X DELETE http://127.0.0.1:5000/tasks/1

if __name__ == '__main__':
    app.run(debug=True)
