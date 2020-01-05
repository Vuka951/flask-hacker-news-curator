from flask import Flask, request, render_template
from scrape import get_posts

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hacker_news', methods=['POST'])
def hacker_news():
    if request.method == 'POST':
        data = request.form
        posts = get_posts(int(data['num_pages']), int(data['min_upvotes']))
        return render_template('hacker_news.html', posts=posts, num_of_pages=int(data['num_pages']), min_upvotes=int(data['min_upvotes']))
    else:
        return 'something went wrong. Try again!'


if __name__ == '__main__':
    app.run()
