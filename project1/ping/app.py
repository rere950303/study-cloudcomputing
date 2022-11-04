import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '[sender_ping] Hello stranger, I am ping container! nice to meet u!!!!!\n'

@app.route('/ping')
def ping():
    request = '---ping--->'
    response = requests.get('http://pong:5001/pong').text
    return '[sender_ping] ' + request + '[receiver_pong] ' + response + '\n'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)