from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, inputs
import datetime
import pdb
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)

now = str(datetime.datetime.now())
TODOS = [
    {
        'id': 1,
        'title': 'build an API',
        'description': 'this is desc1',
        'due_date': str(datetime.date.today() + datetime.timedelta(days=1)),
        'completed': True,
        'created_at': now,
        'updated_at': now
    },
    {
        'id': 2,
        'title': "write article",
        'description': 'this is desc1',
        'due_date': str(datetime.date.today() + datetime.timedelta(days=2)),
        'completed': True,
        'created_at': now,
        'updated_at': now
    },
    {
        'id': 3,
        'title': 'profit!',
        'description': 'this is desc1',
        'due_date': str(datetime.date.today() + datetime.timedelta(days=3)),
        'completed': False,
        'created_at': now,
        'updated_at': now
    }
]

def abort_if_todo_doesnt_exist(todo_id):
	a = any(d['id'] == todo_id for d in TODOS)
	if (a == False):
		abort(404, message="Todo {} doesn't exist".format(todo_id))

def find_todo(todo_id):
    ok = next(item for item in TODOS if item["id"] == todo_id)
    return ok

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('description')
parser.add_argument('due_date')
parser.add_argument('completed', type=inputs.boolean)
parser.add_argument('created_at')
parser.add_argument('updated_at')

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        t = find_todo(todo_id)
        return t

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        t = find_todo(todo_id)
        TODOS.remove(t)
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = parser.parse_args()
        prev = find_todo(todo_id)
        prev['title'] =  prev['title'] if args['title'] == None else args['title']
        prev['description'] = prev['description'] if args['description'] == None else args['description']
        prev['due_date'] = prev['due_date'] if args['due_date'] == None else args['due_date']
        prev['completed'] = prev['completed'] if args['completed'] == None else args['completed']
        prev['created_at'] = prev['created_at'] if args['created_at'] == None else args['created_at']
        prev['updated_at'] = prev['updated_at'] if args['updated_at'] == None else args['updated_at']
        return prev, 201

class TodoList(Resource):
    def get(self):
        return TODOS, 200

    def post(self):
        now = str(datetime.datetime.now())
        args = parser.parse_args()
        if (len(TODOS) == 0):
            todo_id = 1
        else:
            todo_id = max(TODOS, key=lambda x:x['id'])['id'] + 1
        todo = {
            'id': todo_id,
            'title': args['title'],
            'description': args['description'],
            'due_date': args['due_date'],
            'completed': False,
            'created_at': now,
            'updated_at': now
        }
        TODOS.append(todo)
        return todo, 201

api.add_resource(TodoList, '/todos', '/todos/')
api.add_resource(Todo, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
