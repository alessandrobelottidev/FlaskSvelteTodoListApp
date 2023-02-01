from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)


# Enable CORS
CORS(app)


# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    # Convert the data to python dictionary
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Create tables in database
with app.app_context():
    db.create_all()


# Route to get all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])


# Route to create a new todo
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    return jsonify(todo.to_dict())


# Route to create a new todo
@app.route('/api/todos', methods=['POST'])
def create_todo():
    todo = Todo(text=request.json['text'], complete=False)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict())


# Route to update a todo
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    db.session.query(Todo).filter_by(id=todo_id).update(dict(complete=request.json['complete']))
    db.session.commit()
    return jsonify(dict(message='Todo updated successfully'))


# Route to delete a todo
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(todo.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
