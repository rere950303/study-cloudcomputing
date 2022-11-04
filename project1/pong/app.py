from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '[receiver_pong] Hello, I am pong container! nice to meet you\n'

@app.route('/pong')
def pong():
    return 'Hi Hi Hi'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)