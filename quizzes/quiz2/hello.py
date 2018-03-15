from flask import Flask
from flask import request, Response
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def add_user():
    name = request.form["name"]
    user_id = 1
    user = {
        "name" : name,
        "id" : user_id
    }
    return jsonify(user), 201

@app.route("/users/<id>", methods=['GET'])
def get_users(id):
    user_id = id
    user = {
        "name" : "foo",
        "id" : user_id
    }    
    return jsonify(user)

@app.route("/users/<id>", methods=['DELETE'])
def delete_users(id):
    user_id = id    
    return user_id, 204