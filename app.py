from flask import Flask, render_template, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'thisisasecretkey'


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route('/')
def home():
    return render_template('ho.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Category': Category }

if __name__ == "__main__":
    app.run(port=5500, debug=True)
    db.create_all()
