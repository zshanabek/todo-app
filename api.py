from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, inputs
import datetime
import pdb

app = Flask(__name__)
api = Api(app)

now = str(datetime.datetime.now())

TODOS = [
    {
        'id': 1,
        'title': 'build an API',
        'description': 'this is desc1',
        'due_date': now,
        'completed': True,
        'created_at': now,
        'updated_at': now
    },
    {
        'id':2,
        'title': "write article",
        'description': 'this is desc1',
        'due_date': now,
        'completed': True,
        'created_at': now,
        'updated_at': now
    },
    {
        'id':3,
        'title': 'profit!',
        'description': 'this is desc1',
        'due_date': now,
        'completed': True,
        'created_at': now,
        'updated_at': now
    }
]


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')
parser.add_argument('due_date')
parser.add_argument('completed', type=inputs.boolean)
parser.add_argument('created_at')
parser.add_argument('updated_at')

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        prev = TODOS[todo_id]
        task = {
                'title': prev['title'] if args['title'] == None else args['title'],
                'description': prev['description'] if args['description'] == None else args['description'],
                'due_date': prev['due_date'] if args['due_date'] == None else args['due_date'],
                'completed': prev['completed'] if args['completed'] == None else args['completed'],
                'created_at': prev['created_at'] if args['created_at'] == None else args['created_at'],
                'updated_at': prev['updated_at'] if args['updated_at'] == None else args['updated_at']
                }
        TODOS[todo_id] = task
        return task, 201

class TodoList(Resource):
    def get(self):
        return TODOS, 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys())) + 1
        todo_id = '%i' % todo_id
        TODOS[todo_id] = {
            'title': args['title'],
            'description': args['description'],
            'due_date': args['due_date'],
            'completed': args['completed'],
            'created_at': args['created_at'],
            'updated_at': args['updated_at']
            }
        return TODOS[todo_id], 201
    

api.add_resource(TodoList, '/todos', '/todos/')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)