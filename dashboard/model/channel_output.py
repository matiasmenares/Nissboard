from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask import Flask
from model.channel_input import ChannelInput
from model.channel_input import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../Database.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ChannelOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    input_min_val = db.Column(db.Integer, nullable=False)
    input_max_val = db.Column(db.Integer, nullable=False)
    output_min_val = db.Column(db.Integer, nullable=False)
    output_max_val = db.Column(db.Integer, nullable=False)
    channel_inputs_id = db.Column(db.Integer, db.ForeignKey('channel_input.id'))
    channel_input = db.relationship('ChannelInput')
    # measure_id = db.Column(db.Integer, db.ForeignKey('measures.id'))

class ChannelOutputSchema(ma.Schema):
    class Meta:
        model = ChannelOutput
        fields = ("name", "input_max_val")

class ChannelInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class ChannelInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "analog_channel_id")

db.create_all()
db.session.commit()