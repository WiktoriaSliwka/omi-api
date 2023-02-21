from flask import Flask, request, jsonify, render_template, redirect
import json
import sqlite3
from flask_restful import Api, Resource
import requests
from storage import Storage
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
bcrypt = Bcrypt(app)




@app.route("/products", methods=['POST'])
def products():
    cur = Storage()
    cur.insert_products()
    return "products inserted"

    

@app.route("/")
def home():
    return "home page"
    # return render_template('home.html')


@app.route("/register", methods=['POST','GET'])
def register():  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        #Add hashed password here!
        cur = Storage()
        cur.register_user(username, password, email)
    return "registered user"


@app.route("/login", methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cur = Storage()
        user = cur.findUser(username, password)

        print(user)
        
        if not user:
            return "username or password incorrect"
        
        
    return "logged in user"

        




    

#@app.route("/delete", methods=['DELETE'])





# python -m flask run (to run server, make sure cd into project)
if __name__ == '__main__':
    app.run(port=5000, debug=True)