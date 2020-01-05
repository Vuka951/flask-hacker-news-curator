from flask import Flask, request
from scrape import get_posts

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.args)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
