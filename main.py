from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        data = json.loads(request.data)
        resp = {
            "session": data["session"],
            "response": {
                "text": "Привет вездекодерам!",
                "tts": "Привет вездекодерам!",
                "end_session": True
            },
        }
        if ("ThereIsNoInfoRoma" in data["request"]["command"] and "Вездекод" in data["request"]["command"]):
            resp["response"] = {
                "text": "Привет вездекодерам!",
                "tts": "Привет вездекодерам!",
                "end_session": True
            },
            return json.dumps(resp)
        
        resp["response"] = {
                "text": "Сегодня без привета",
                "tts": "Сегодня без привета",
                "end_session": True
        },
        return json.dumps(resp)
    else:
        return "Hello"
    

