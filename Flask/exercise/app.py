from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return 'index'

@app.route('/user/<username>')
def profile(username):
    return f'{username}님의 프로필 페이지입니다. 홈으로 가기:http://127.0.0.1:5000{url_for("index")}'
