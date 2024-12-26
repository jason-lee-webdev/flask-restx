from flask import Flask
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

### Documenting with the @api.doc() decorator
# @api.route('/my-resource/<id>', endpoint='my-resource')
# @api.doc(params={'id': 'An ID'})
# class MyResource(Resource):
#     def get(self, id):
#         return {}
#
#     @api.doc(responses={403: 'Not Authorized'})
#     def post(self, id):
#         api.abort(403)


### The @api.marshal_with() decorator
# resource_fields = api.model('Resource', {
#     'name': fields.String,
# })


# @api.route('/my-resource/<id>', endpoint='my-resource')
# class MyResource(Resource):
#     @api.marshal_with(resource_fields, as_list=True)
#     def get(self):
#         return get_objects()
#
#     @api.marshal_with(resource_fields, code=201)
#     def post(self):
#         return create_object(), 201


if __name__ == '__main__':
    app.run(debug=True)
