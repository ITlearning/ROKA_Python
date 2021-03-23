# flask 모듈 사용하기
from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터
def hello():
    return "<h1>Hello World!</h1>"

# 하.. 서버가 열리긴 하는데, 또또또또또또 사지방이라 막힘..