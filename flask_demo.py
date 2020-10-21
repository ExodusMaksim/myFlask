from flask import Flask, jsonify, g, request
from tinydb import TinyDB, Query
import uuid
import re

DB = './users.json'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = TinyDB(DB)
    return db


app = Flask(__name__)


@app.route('/hello')
def hello():
    return jsonify({"message": "hello world"})


@app.route('/api/v1/get_users', methods=['GET'])
def get_users():
    db = get_db()
    users = db.all()
    return jsonify(users)


@app.route('/api/v1/get_user/<int:user_id>', methods=['GET'])  # 获取单个数数据
def get_user(user_id):
    db = get_db()
    result = db.search(Query().user_id == user_id)
    if len(result) > 0:
        return jsonify(result)
    else:
        return jsonify({'message': 'not found'}), 442


@app.route('/api/v1/add_user', methods=['POST'])
def add_user():
    db = get_db()
    user = request.json
    if user is not None and user['user_id']:
        user_data = {"user_id": user['user_id'], "name": user['name'], "age": user['age'], "address": user['address']}
        db.insert(user_data)
        return jsonify({'message': 'succsess'})
    else:
        return jsonify({'message': 'user can be empty'})


@app.route('/api/v1/update_user', methods=['PUT'])
def update_user():
    db = get_db()
    user = request.json
    if user is not None and user['user_id']:
        user_data = {"user_id": user['user_id'], "name": user['name'], "age": user['age'], "address": user['address']}
        db.update(user_data, Query().user_id == user['user_id'])
        return jsonify({'message': 'succsess'})
    else:
        return jsonify({'message': 'user can be empty'})


@app.route('/api/v1/del_user/<int:user_id>', methods=['DELETE'])  # 删除单个数据
def del_user(user_id):
    db = get_db()
    result = db.search(Query().user_id == user_id)
    if len(result) > 0:
        db.remove(Query().user_id == user_id)
        return jsonify({'message': 'delete success'})
    else:
        return jsonify({'message': 'not found'})


if __name__ == '__main__':
    app.run(debug=True)
