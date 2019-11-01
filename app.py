#import flask
from flask import Flask, render_template

#declare an app instance
app = Flask(__name__)

#declare routes
@app.route('/')
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run()