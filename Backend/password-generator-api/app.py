import os

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from password import generator


class GeneratePasswordView(Resource):
    def get(self, length):
        # generating a random password 
        password = generator.Password(length).generate_password()
        password_length = len(password)
        
        return {"password": password, "length": password_length}, 200
    

# accessing the secret key from the environment variable configuration file
# def get_secret_key():
#     secret_key = os.environ.get('FLASK_APP_SECRET_KEY')

#     # Check if the secret key is set
#     if not secret_key:
#         raise ValueError("No secret key set for Flask application. Please set FLASK_APP_SECRET_KEY environment variable.")
    
#     return str(secret_key)

    
def init_app():
    # creating an instance of Flask application
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "DEFINITELY_NOT_SECURE"

    # creating an Api instance and passing Flask application as argument
    api = Api(app)

    # enabling CORS support for our Flask application
    CORS(app)

    # adding the resource to our api
    api.add_resource(GeneratePasswordView, '/api/password/<int:length>')

    return app


if __name__ == "__main__":
    init_app().run(debug=True)