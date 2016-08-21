from flask import Flask, request
import requests
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://Victoria:260784zvg@ds029635.mlab.com:29635/heroku_3gwq73vd")
db = client.heroku_3gwq73vd


@app.route('/')
def test():
    return "It works!"


def send(chat_id, text):
    requests.post("https://api.telegram.org/bot253643907:AAGRFi8w-YJiyHw-2qioYIn2wQJMdLx-cnQ/sendMessage",
                  {
                      "chat_id": chat_id,
                      "text": text
                  })


@app.route("/hook", methods=['POST'])
def hook():
    chat_id = request.get_json()["message"]["chat"]["id"]
    text = request.get_json()["message"]["text"]

    command, *args = text.split()

    if command == "/add":
        db.products.insert({"products": args})
        send(chat_id, "Products added")
    if command == "/get":
        answer = "\n".join(
            map(str, db.products.find())
        )
        send(chat_id, answer)
    if command == "/add_dish":
        answer = "\n".join(
            map(str, db.products.find())
        )
        send(chat_id, answer)
    if command == "/dish":
        answer = "\n".join(
            map(str, db.products.find())
        )
        send(chat_id, answer)


    return "OK"
