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

products = ('Картошка в фольге http://vkysno.kiev.ua/d-recept-action-detail-rid-1414-page-3.html',
            'Картофель запеченый с грибами и беконом под сыром ',
            'Картофельно-мясная вкусняшка http://vkysno.kiev.ua/d-recept-action-detail-rid-1270-page-4.html',
            'картошка', 'бекон')

meal = ('Гречневая каша с фрикассе', 'Рис с рыбными котлетами', 'Яичница с беконом', 'Борщ',
        'Пюре с отбивными', 'А закажи-ка пиццу в Watatsumi +380505078111', 'Стейк с салатом из пекинской капусты',
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
    if command == "/pizza":
        answer = "Watatsumi +380505078111"
        send(chat_id, answer)
    if command == "/sushi":
        answer = "Watatsumi +380505078111"
        send(chat_id, answer)
    return "OK"
