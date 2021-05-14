import os
import db
from datetime import datetime
from flask import Flask, request


app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')


@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    return 'Hello, World!' + name


@app.route('/path/<x>/<y>/<z>')
def path(x, y, z):
    return "path is " + x + " " + y + " " + z


@app.route('/env')
def env():
    return os.getenv('DETA_PATH', 'ERROR')


@app.route('/version')
def version():
    return "7"


@app.route('/time')
def time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


@app.route('/db')
def db_check():
    return db.check(db)


@app.route('/')
def root():
    return app.send_static_file('index.html')

