from flask import Blueprint

blue_city = Blueprint("city", __name__, url_prefix="/city")

@blue_city.rout("/seoul")
def seoul():
    return "this is Seoul"

@blue_city.route("/busan")
def busan():
    return "this is busan"

