from flask import Flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Team 18!'