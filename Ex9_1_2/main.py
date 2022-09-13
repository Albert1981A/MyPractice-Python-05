from flask import Flask
from Routers.users import users
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        # return json.JSONEncoder.default(self, obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = JSONEncoder

app.register_blueprint(users, url_prefix='/users')

app.run()