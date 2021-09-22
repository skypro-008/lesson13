import json
from operator import itemgetter

from flask import Flask, render_template, request

app = Flask(__name__)

avia_tickets = [
    {
        "from": {
            "country": "Russia",
            "airport": "DME",
        },
        "to": {
            "country": "USA",
            "airport": "LAX",
        },
        "price": 78634,
        "available": True,
        "date": "2011-03-16",
    },
    {
        "from": {
            "country": "Russia",
            "airport": "SVO",
        },
        "to": {
            "country": "USA",
            "airport": "ATL",
        },
        "price": 87909,
        "available": False,
        "date": "2011-03-14",
    },
    {
        "from": {
            "country": "Russia",
            "airport": "VKO",
        },
        "to": {
            "country": "USA",
            "airport": "ORD",
        },
        "price": 19000,
        "available": True,
        "date": "2011-02-11",
    },
]


@app.route('/get_tickets')
def get_tickets():
    response = avia_tickets
    price_filter = request.args.get('price')
    splitted = price_filter.split(":")
    op = splitted[0]
    price = int(splitted[1])
    if price is not None:
        response = []
        for t in avia_tickets:
            if op == "eq":
                if t.get("price") == price:
                    response.append(t)
            elif op == "gt":
                if t.get("price") > price:
                    response.append(t)
            elif op == "lt":
                if t.get("price") < price:
                    response.append(t)
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
