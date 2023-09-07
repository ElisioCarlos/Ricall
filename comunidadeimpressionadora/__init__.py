from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gigsqiuryksrvm:1c7210bf232de84bbca256e75676094545c67ab5c1a1e759f87972d20393e490@ec2-18-214-134-226.compute-1.amazonaws.com:5432/d1sr36kdmobr4v'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'



database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
from comunidadeimpressionadora import routes

