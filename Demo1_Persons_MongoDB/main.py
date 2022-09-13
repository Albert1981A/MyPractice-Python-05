from flask import Flask
from Routers.persons import persons
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = JSONEncoder

app.register_blueprint(persons, url_prefix='/persons')

app.run()

