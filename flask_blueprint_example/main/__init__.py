#  python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420). 
# 하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.

from flask import Flask
from . import book
from . import city

app = Flask(__name__)

app.register_blueprint(book.blue_book)
app.register_blueprint(city.blue_city)