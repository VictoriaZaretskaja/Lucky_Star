from flask import Flask, request
from pymongo import MongoClient
import random
import requests, json
import urllib.request, urllib.parse,urllib
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


def video(bot, update, msg):
    link = urllib.parse.urlencode({"search_query": msg})
    content = urllib.request.urlopen("https://www.youtube.com/results?" + link)
    search_results = re.findall('href=\"\/watch\?v=(.*?)\"', content.read().decode())
    if len(search_results) > 0:
        # Первые 10 результатов
        search_results = search_results[0:9:1]
        choice_f = random_number.choice(search_results)
        yt_link = "https://www.youtube.com/watch?v=" + choice_f
        bot.sendMessage(update.message.chat_id, text=yt_link, parse_mode=ParseMode.MARKDOWN)
    else:
        bot.sendMessage(update.message.chat_id, text='Ничего не найдено.')

products = ['Салат Ингредиенты: Кочан пекинской капусты, хлеб серый смешанный(украинский) 3-4 ломтика',
            'Masha', 'Lena', 'Oleg', 'Dima']

@app.route("/hook", methods=['POST'])
def hook():
    chat_id = request.get_json()["message"]["chat"]["id"]
    text = request.get_json()["message"]["text"]
    command, *args = text.split()
    if command == "/add_dish":
        db.products.insert({"dish": args})
        send(chat_id, "Dish added")
    if command == "/Hi":
        answer = "Hi, LUCKY`s Friend!"
        send(chat_id, answer)
    if command == "/dish1":
        answer = random.choice(products)
        send(chat_id, answer)
    if command == "/pic":
        answer = "http://www.virtusinterpress.org/IMG/jpg/ukr_26740.jpg"
        send(chat_id, answer)
    if command == "video":

        send(chat_id, video())
    if command == "/dish":
        answer = random.choice(db.products)
        send(chat_id, answer)

    return "OK"