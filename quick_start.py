from flask import Flask, request
from flask_restx import Resource, Api, reqparse, fields

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


todos = {}


@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')


@api.route('/todos')
class Todos(Resource):
    def put(self):
        args = parser.parse_args(strict=True)
        rate = args['rate']
        return {"rate": rate}, 201


model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
})


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


@api.route('/todo', endpoint='todo_ep')  # 엔드포인트 이름 명시
class Todo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
