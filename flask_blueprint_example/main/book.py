from flask import Blueprint, blueprints

blue_book = Blueprint("book", __name__, url_prefix="/book")

@blue_book.route("/read")
def read():
    return "this is read"

@blue_book.rout("/write")
def write():
    return "this is write"
