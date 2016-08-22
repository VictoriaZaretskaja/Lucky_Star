from flask import Flask, request
import requests
from pymongo import MongoClient
import random

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


    if command == "/add_dish":
        db.products.insert({"dish": args})
        send(chat_id, "Dish added")
    if command == "/dish":
        answer = random.choice(db.products.find({}))
        send(chat_id, answer)
    if command == "/Help":
        answer1 = "You could add a dish with command /add_dish or give a dish with command /dish"
        send(chat_id, answer1)
    if command == "/Hi":
        answer2 = "Hi, Lucky's friend!"
        send(chat_id, answer2)

    return "OK"
