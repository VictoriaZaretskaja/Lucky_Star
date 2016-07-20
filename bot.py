from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "It works!"

@app.route("/hook", methods=['POST'])
def hook():
    return "OK"



app.run