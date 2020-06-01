from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask import Flask
import os 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////"+os.getcwd()+"/Database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class ChannelOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    input_min_val = db.Column(db.Integer, nullable=False)
    input_max_val = db.Column(db.Integer, nullable=False)
    output_min_val = db.Column(db.Integer, nullable=False)
    output_max_val = db.Column(db.Integer, nullable=False)
    channel_input_id = db.Column(db.Integer, db.ForeignKey('channel_input.id'), nullable=False)
    channel_input = db.relationship('ChannelInput')
    measure_id = db.Column(db.Integer, db.ForeignKey('measure.id'))
    measure = db.relationship('Measure')

class ChannelOutputSchema(ma.Schema):
    class Meta:
        model = ChannelOutput
        fields = ("id","name", "input_max_val", "measure_id")

class ChannelInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    analog_input_id = db.Column(db.Integer, db.ForeignKey('analog_input.id'), nullable=False)
    analog_input = db.relationship('AnalogInput')

class ChannelInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "analog_channel_id")

class AnalogInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pin = db.Column(db.String, nullable=False)
    voltage_resistance = db.Column(db.Boolean, nullable=False)

class AnalogInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "analog_channel_id")

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    formula = db.Column(db.String, nullable=False)
    undo_formula = db.Column(db.String, nullable=False)
    explanation = db.Column(db.String, nullable=False)
    measure_group_id = db.Column(db.Integer, db.ForeignKey('measure_group.id'))
    measure = db.relationship('MeasureGroup')

class MeasureSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "analog_channel_id")

class MeasureGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
class MeasureGroupSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name")

class Dashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    red_line = db.Column(db.String, nullable=False)
    yellow_line = db.Column(db.String, nullable=False)
    
class DashboardSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "red_line", "yellow_line")

class DashboardOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboard.id'))
    dashboard = db.relationship('Dashboard')
    channel_output_id = db.Column(db.Integer,db.ForeignKey('channel_output.id'))
    channel_output = db.relationship('ChannelOutput')
    
class DashboardOutputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "dashboard_id", "channel_output_id")

class DashboardHasOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dashboard_output_id = db.Column(db.Integer,db.ForeignKey('dashboard_output.id'))
    dashboard_output = db.relationship('DashboardOutput')
    channel_output_id = db.Column(db.Integer,db.ForeignKey('channel_output.id'))
    channel_output = db.relationship('ChannelOutput')

class DashboardHasOutputSchema(ma.Schema):
    class Meta:
        model = DashboardHasOutput
        fields = ("dashboard_output_id","channel_output_id")

db.create_all()
db.session.commit()