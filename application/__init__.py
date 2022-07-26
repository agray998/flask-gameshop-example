from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///flask-demo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import application.routes