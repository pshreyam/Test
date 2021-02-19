from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Timepass(Resource):
    cricketers = [
        { 
            'name': 'MS Dhoni',
            'country': 'India'
        },
        { 
            'name': 'Jos Buttler',
            'country': 'England'
        },
        { 
            'name': 'Virat Kohli',
            'country': 'India'
        },
        { 
            'name': 'Joe Root',
            'country': 'England'
        },
    ]

    def get(self):
        return self.cricketers
    
    def post(self):
        data = request.get_json()
        if data not in self.cricketers:
            self.cricketers.append(data)
            return {
                'data': self.cricketers[-1],
                'message': 'Data succesfully inserted!'
            }
        return {
            'error': 'duplicate data not allowed!'
        }

api.add_resource(Timepass, '/')