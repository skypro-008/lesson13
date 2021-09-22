# app.py
import json
from operator import itemgetter

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/something/<str:test>')
def user_salary(test: str):
    sort = request.args.get('sort')
    r = {
        "name": test,
        "salary": sort
    }
    return json.dumps(r)


@app.route('/salary/<int:salary>')
def user_salary(salary: int):
    # get parameter from query path
    name = request.args.get('name')
    # get and check parameter from segment of URL
    r = {
        "name": name,
        "salary": salary
    }
    return json.dumps(r)


if __name__ == '__main__':
    app.run()
