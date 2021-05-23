from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import m2m_scrape

app = Flask(__name__)

# instantiate mongo client
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_scraper')
db = mongo.db

@app.route('/')
def index():
    post = db.posts
    return render_template('index.html', post=post)

@app.route('/scrape')
def scrape():
    post = m2m_scrape()
    db.posts.update({}, post, upsert=True)

    # redirect to index
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)