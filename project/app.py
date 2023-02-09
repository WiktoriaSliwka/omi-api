from flask import Flask, request, jsonify
import json
import sqlite3
from flask_restful import Api, Resource
import requests
import db
from db import connect_to_db



app = Flask(__name__)
api = Api(app)


@app.route("/products", methods=['GET'])
def products():
    connect_to_db()
    req = requests.get('https://api.storerestapi.com/products')
    return (req.content)

@app.route("/")
def home():
    return "Home page"

# @app.route("/users")
# def log_in():
#     return "log in page"

# @app.route("/register", methods=['GET'])
# def register():  
#     return 

#@app.route("/delete", methods=['DELETE'])


# python -m flask run (to run server, make sure cd into project)
if __name__ == '__main__':
    app.run()