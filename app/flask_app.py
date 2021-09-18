import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify


file_path = os.path.abspath(os.getcwd()) + "\database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route('/<name>/')
def index(name):
    return jsonify(name=name)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.username}"


@app.route('/users')
def users():
    all_users = User.query.all()
    return f"{all_users}"















