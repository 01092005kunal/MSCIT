from flask import Flask, request, jsonify

import datetime

app =  Flask(__name__)

todos = []
next_id = 1
@app.route('/todos',methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()

    task = data.get('task')
    status = data.get('status')
    date = datetime.datetime.now()

    if task is None:
        return jsonify({'error':'Task is required'}),400
    
    new_todo = {
        'id': next_id,
        'task': task,
        'date': date,
        'status': status
    }

    todos.append(new_todo)
    next_id += 1

    return "task added", 201

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):

    todo = next(
        (todo for todo in todos if todo['id'] == todo_id),
        None
    )

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):

    data = request.get_json()
    task = data.get('task')

    if task is None:
        return jsonify({'error': 'Todo is required'}), 400

    todo = next(
        (todo for todo in todos if todo['id'] == todo_id),
        None
    )

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    todo['task'] = task

    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):

    global todos

    todos = [
        todo for todo in todos
        if todo['id'] != todo_id
    ]

    return jsonify("TASK DELETED")


if __name__ == '__main__':
    app.run(debug=True)