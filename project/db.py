from flask import Flask, request, jsonify
import json
import sqlite3



app = Flask(__name__)
app.debug = True




@app.route("/")

def home():
    
    return "Home Page"


# @app.route("/login", methods=['GET'])

# @app.route("/register", methods=['GET'])

# @app.route("/delete", methods=['DELETE'])



if __name__ == '__main__':
    
    app.run(host='0.0.0', port=3000)