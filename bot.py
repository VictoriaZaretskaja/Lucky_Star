from flask import Flask, request
from pymongo import MongoClient
import random
import requests, json
import urllib.request, urllib.parse, urllib
import urllib.request
import random  as  random_number

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

products = ("Готовим картошку в фольге. Нарезать картофель мелкими кубиками. Разогреть масло на сковороде и бросить
            картофель на сковороду, обжаривать 2 минуты на сильном огне, постоянно помешивая. Нарезать колбасу,
            ветчину соломкой, нарезать лук мелко. В картофель добавить шпик, ветчину и колбасу. В конце - лук и
            чеснок. Обжаривать до золотой корочки на картофеле. Затем смазать фольгу маслом, выложить картофель,
            посолить, поперчить (можно добавить любимую приправу). Завернуть картофель в фольгу и запекать в
            духовке 30-40 минут.", 'Masha', 'Lena', 'Oleg', 'Dima')

meal = ('Гречневая каша с фрикассе', 'Рис с рыбными котлетами', 'Яичница с беконом', 'Борщ',
        'Пюре с отбивными', 'А закажи-ка пиццу в Watatsumi - +380505078111', 'Стейк с салатом из пекинской капусты',
        'Жареная картошка с колбасками')


@app.route("/hook", methods=['POST'])
def hook():
    chat_id = request.get_json()["message"]["chat"]["id"]
    text = request.get_json()["message"]["text"]
    command, *args = text.split()
    if command == "/add_dish":
        db.products.insert({"dish": args})
        send(chat_id, "Dish added")
    if command == "/hi":
        answer = "Hi, LUCKY`s Friend!"
        send(chat_id, answer)
    if command == "/dish":
        answer = random.choice(products)
        send(chat_id, answer)
    if command == "/help":
        answer = "Do you need some help?"
        send(chat_id, answer)
    if command == "/meal":
        answer = random.choice(meal)
        send(chat_id, answer)
    return "OK"
