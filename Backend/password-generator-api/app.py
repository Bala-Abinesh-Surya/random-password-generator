import os
from dotenv import load_dotenv

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from password import generator


class GeneratePasswordView(Resource):
    def get(self):
        # parsing the incoming request
        parser = reqparse.RequestParser()

        parser.add_argument("length", type=int, required=True, help="Length pf the password cannot be empty!")
        parser.add_argument("numbers", type=bool, required=True, help="Choose whether numbers should be included in the password!")
        parser.add_argument("special", type=bool, required=True, help="Choose whether special characters should be included in the password!")

        args = parser.parse_args()

        # accessing the user's choice from the parsed request
        length = args.get("length")
        numbers = args.get("numbers")
        special = args.get("special")

        # generating a random password 
        password = generator.Password(length, numbers, special).generate_password()
        password_length = len(password)
        
        return {"password": password, "length": password_length}, 200
    

# accessing the secret key from the environment variable configuration file
def get_secret_key():
    # loading the environment variables from the .env file
    load_dotenv()

    secret_key = os.getenv('FLASK_APP_SECRET_KEY')

    # Check if the secret key is set
    if not secret_key:
        raise ValueError("No secret key set for Flask application. Please set FLASK_APP_SECRET_KEY environment variable.")
    
    return str(secret_key)

    
def init_app():
    # creating an instance of Flask application
    app = Flask(__name__)
    app.config["SECRET_KEY"] = get_secret_key()

    # creating an Api instance and passing Flask application as argument
    api = Api(app)

    # enabling CORS support for our Flask application
    CORS(app)

    # adding the resource to our api
    api.add_resource(GeneratePasswordView, '/api/generate-password')

    return app


if __name__ == "__main__":
    init_app().run(debug=True)