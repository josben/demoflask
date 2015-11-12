
from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World"

@app.route('/mongo')
def home_page():
    online_users = mongo.db.users.find({'online': True})
    print online_users
    return render_template('index.html', online_users=online_users)

if __name__ == "__main__":
    app.run()

