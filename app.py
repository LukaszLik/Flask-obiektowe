from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Flask</h1> <span>przejdź do <a href="https://github.com/LukaszLik/Flask-obiektowe">Githuba</a></span>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
