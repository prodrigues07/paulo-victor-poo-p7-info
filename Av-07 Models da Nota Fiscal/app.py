from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atvd07.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from rotas import *

if __name__ == "__main__":
    app.run()
