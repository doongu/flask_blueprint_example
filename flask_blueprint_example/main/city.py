from flask import Blueprint
#   - name은 블루프린트의 이름을 나타낸다. 

#   - import_name은 블루프린트 패키지의 이름이다. 보통 __name__으로 많이 쓰인다. 이는 블루프린트의 root_path의 위치를 찾는데 도움을 준다.
# Blueprint( 이름, 모듈명, URL 프리픽스(url_prefix) )
blue_city = Blueprint("city", import_name = __name__, url_prefix="/city")

@blue_city.rout("/seoul")
def seoul():
    return "this is Seoul"

@blue_city.route("/busan")
def busan():
    return "this is busan"

