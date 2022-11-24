from flask import Flask
from config import Configuration

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


