from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "This is About Page!"

@app.route('/user/<username>')
def user_profile(username):
    return f'UserName: {username}'

    

if __name__ == '__main__':
    app.run()



    