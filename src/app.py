import json

from flask import request

from . import create_app, Database
from .model import Cats

app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    cats = Database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200