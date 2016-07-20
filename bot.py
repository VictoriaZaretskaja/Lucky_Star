from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def test():
    return "It works!"

@app.route("/hook", methods=['POST'])
def hook():
    chat_id = request.get_json()["message"]["chat"]["id"]
    requests.post("https://api.telegram.org/bot253643907:AAGRFi8w-YJiyHw-2qioYIn2wQJMdLx-cnQ/sendMessage",
        {
            "chat_id": chat_id,
            "text": "Hi!"
        })
    return "OK"



app.run