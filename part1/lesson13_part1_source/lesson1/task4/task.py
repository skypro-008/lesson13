# app.py
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/something/<str:test>')
def user_salary(test: str):
    sort = request.args.get('sort')
    r = {
        "name": test,
        "salary": sort
    }
    return json.dumps(r)


if __name__ == '__main__':
    app.run()
