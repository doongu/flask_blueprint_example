from flask import Flask
from . import book
from . import city

app = Flask(__name__)

app.register_blueprint(book.blue_book)
app.register_blueprint(city.blue_city)