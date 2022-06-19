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
            "response": {},
            "version": "1.0"
        }
        if ("thereisnoinforoma" in data["request"]["command"] and "вездеход" in data["request"]["command"]):
            resp["response"] = {
                "text": "Привет вездекодерам!",
                "tts": "Привет вездекодерам!",
                "end_session": True
            }
            return json.dumps(resp)
        resp["response"] = {
                "text": "Сегодня без привета",
                "tts": "Сегодня без привета",
                "end_session": True
        }
        return json.dumps(resp)
    else:
        return "Hello"


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        data = json.loads(request.data)
        resp = {
            "session": data["session"],
            "response": {},
            "version": "1.0"
        }   
        if ("старт" in data["request"]["command"]):
            resp["response"] = {
                "text": "Поехали! Первый вопрос: В каком году разработали первый айфон",
                "tts": "Поехали! Первый вопрос: В каком году разработали первый айфон",
                "end_session": False,
            }

            resp["session_state"] = { 
                "question": "1",
                "score": "0"
            }
            return json.dumps(resp)
        if "state" in data.keys():
            if data["state"]["session"]["question"] == "1":
                resp["response"] = {
                    "text": "Второй вопрос: В каком Doom первый раз запустили не на компьютере",
                    "tts": "Второй вопрос: В каком Doom первый раз запустили не на компьютере",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "1923" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "2":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "3":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "4":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "5":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "6":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "7":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "2",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "8":
                resp["response"] = {
                    "text": "Третий вопрос: В каком году на рынок вышла фигма",
                    "tts": "Третий вопрос: В каком году на рынок вышла фигма",
                    "end_session": False,
                }

                score = int(data["state"]["session"]["score"])
                if "2015" in data["request"]["command"]:
                    score += 1
                resp["session_state"] = { 
                    "question": "8",
                    "score": srt(score)
                }
                return json.dumps(resp)
            elif data["state"]["session"]["question"] == "8":
                score = int(data["state"]["session"]["score"])
                if score <= 5:
                    resp["response"] = {
                        "text": "Вам подойдут все категории, кроме дизайна",
                        "tts": "Вам подойдут все категории, кроме дизайна",
                        "end_session": True,
                    }
                else:
                    resp["response"] = {
                        "text": "Больше всего вам подойдет дизайн",
                        "tts": "Больше всего вам подойдет дизайн",
                        "end_session": True,
                    }
                score = int(data["state"]["session"]["score"])
                return json.dumps(resp)

        resp["response"] = {
                "text": "Ошибка",
                "tts": "Ошибка",
                "end_session": True
        }
        return json.dumps(resp)
    else:
        return "Quiz Page"
    

