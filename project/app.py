from flask import Flask, request, jsonify, render_template, redirect, session
import json
import sqlite3
from flask_restful import Api, Resource
import requests
from storage import Storage
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, UserMixin, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from models import User




db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
db.__init__(app)
bcrypt = Bcrypt(app)

# Login_Manager = LoginManager()
# Login_Manager.init_app(app)
# Login_Manager.login_view = 'login'

# @Login_Manager.user_loader
# def load_user(user_id):
#     return Storage.getuserId(user_id)


@app.route("/products", methods=['POST'])
def products():
    cur = Storage()
    cur.insert_products()
    return "products inserted"

    

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/register", methods=['POST', 'GET'])
def register():  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        #Add hashed password here!
        cur = Storage()
        cur.register_user(username, password, email)
        return "registered user"

    if request.method == 'GET':

        return render_template('register.html')

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
        if user[0] == 1:
            return "you are admin"
       
    #     session['username'] = user[1]
    #     session['password'] = user[2]
    
    # elif "userId" in session:
        print("Already logged in")
        return "logged in"
    
     
    if request.method == 'GET':

        return render_template('login.html')

# @app.route("/admin", methods=['GET', 'POST'])
# @login_required
# def admin():
#     if request.method == 'POST':
#         cur = Storage()
#         id = current_user.id
#         cur.getuserId()
#         if id == 1:
#             return "Admin page"
#         else:
#             return "No access allowed"
        
    
        


    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     cur = Storage()
    #     user = cur.findUser(username, password)
    #     print(user)
        




    

#@app.route("/delete", methods=['DELETE'])





# python -m flask run (to run server, make sure cd into project)
if __name__ == '__main__':
    app.run(port=5000, debug=True)