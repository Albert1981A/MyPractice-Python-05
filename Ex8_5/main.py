from flask import Flask
from Routers.students import students
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = JSONEncoder

app.register_blueprint(students, url_prefix='/students')

app.run()

#2:12:30