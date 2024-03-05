from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from password import generator

app = Flask(__name__)
api = Api(app)
CORS(app)

class GeneratePasswordView(Resource):
    def get(self, length):
        # generating a random password 
        password = generator.Password(length).generate_password()
        password_length = len(password)
        
        return {"password": password, "length": password_length}, 200
    
api.add_resource(GeneratePasswordView, '/api/password/<int:length>')

if __name__ == "__main__":
    app.run(debug=True)