from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///escola.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True

db = SQLAlchemy(app)
