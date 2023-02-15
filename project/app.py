from flask import Flask, request, jsonify
import json
import sqlite3
from flask_restful import Api, Resource
import requests
from storage import Storage
from flask_bcrypt import Bcrypt



app = Flask(__name__)
bcrypt = Bcrypt(app)




@app.route("/products", methods=['GET'])
def products():
    req = requests.get('https://api.storerestapi.com/products')
    return (req.content)

@app.route("/")
def home():
    return "Home page"

#@app.route("/users")
 #def log_in():
#     return "log in page"

@app.route("/register", methods=['POST','GET'])
def register():  

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    cur = Storage()
    #cur.register_user()
    return "registered user"

#@app.route("/delete", methods=['DELETE'])


# python -m flask run (to run server, make sure cd into project)
if __name__ == '__main__':
    app.run(port=5000, debug=True)