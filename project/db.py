from flask import Flask, request, jsonify
import json
import sqlite3
from flask_restful import Api, Resource



app = Flask(__name__)
api = Api(app)




@app.route("/")

def home():
    
    return "Home Page"


# @app.route("/login", methods=['GET'])

# @app.route("/register", methods=['GET'])

# @app.route("/delete", methods=['DELETE'])


# python -m flask run (to run server, make sure cd into project)
if __name__ == '__main__':
    
    app.run(host='0.0.0', port=3000, debug=True)