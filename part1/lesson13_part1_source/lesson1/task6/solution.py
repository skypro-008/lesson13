import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/get_users')
def get_users():
    with open('users.txt') as json_file:
        users = json.load(json_file)
        d = json.dumps(users)
        return d, 200


@app.route('/get_user/<int:id>')
def get_user(id: int):
    with open('users.txt') as json_file:
        users = json.load(json_file)
        for u in users:
            if u.get("id") == id:
                return json.dumps(u), 200
    return "", 404


@app.route('/create_user', methods=['POST'])
def create_user():
    users = None
    with open('users.txt') as json_file:
        users = json.load(json_file)
        data = request.get_json()
        if not data:
            return "", 400
        users.append(data)
        return "", 201


if __name__ == '__main__':
    app.run()
