from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../Database.db"
db = SQLAlchemy(app)

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    formula = db.Column(db.String, unique=True, nullable=False)
    undo_formula = db.Column(db.String, unique=True, nullable=False)
    explanation = db.Column(db.String, unique=True, nullable=False)

db.create_all()
db.session.commit()