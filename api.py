from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

pets = {}

class PetsService(Resource):
    def get(self, pet_id):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int,
            help='Rate to charge for this resource')
        return {pet_id, pets[pet_id]}

    def put(self, pet_id):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int,
            help='Rate to charge for this resource')
        pets[pet_id] = request.form['data']
        return {pet_id: pets[pet_id]}

api.add_resource(PetsService, '/', '/<string:pet_id>')

if __name__ == '__main__':
    app.run(debug=True)