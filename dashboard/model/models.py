from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask import Flask
import os 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.getcwd()+"/Database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ChannelOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    input_min_val = db.Column(db.Integer)
    input_max_val = db.Column(db.Integer)
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
    analog_input_id = db.Column(db.Integer, db.ForeignKey('analog_input.id'))
    analog_input = db.relationship('AnalogInput')
    obd_input_id = db.Column(db.Integer, db.ForeignKey('obd_input.id'))
    obd_input = db.relationship('ObdInput')
    nissan_input_id = db.Column(db.Integer, db.ForeignKey('nissan_input.id'))
    nissan_input = db.relationship('NissanInput')

class ChannelInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "analog_input_id", "obd_input_id")

class Obd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    command = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    measure = db.relationship('Measure')
    measure_id = db.Column(db.Integer, db.ForeignKey('measure.id'))  

class ObdSchema(ma.Schema):
    class Meta:
        model = Obd
        fields = ("id", "name", "description")

class ObdInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    obd_id = db.Column(db.Integer, db.ForeignKey('obd.id'), nullable=False)
    obd = db.relationship('Obd')

class ObdInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "description", "obd_id")

class NissanCmd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    cmd = db.Column(db.String, unique=True, nullable=False)


class NissanCmdSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "cmd")

class NissanInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    obd_id = db.Column(db.Integer, db.ForeignKey('nissan_cmd.id'), nullable=False)
    obd = db.relationship('NissanCmd')

class NissanInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "description", "nissan_cmd_id")

class AnalogInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pin = db.Column(db.String, nullable=False)
    voltage_resistance = db.Column(db.Boolean, nullable=False)

class AnalogInputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "pin","analog_channel_id")

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
        model = Measure
        fields = ("id", "name")

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

class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    life_second = db.Column(db.Integer, nullable=False)
    alarm_type_id = db.Column(db.Integer,db.ForeignKey('alarm_type.id'))
    alarm_type = db.relationship('AlarmType')
    
class AlarmSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "description", "alarm_type_id", "life_second")

class AlarmType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
class AlarmTypeSchema(ma.Schema):
    class Meta:
        model = AlarmType
        fields = ("id", "name")

class Condition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)

class ConditionSchema(ma.Schema):
    class Meta:
        model = AlarmType
        fields = ("id", "name", "condition")

class AlarmOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String, nullable=False)
    channel_output_id = db.Column(db.Integer,db.ForeignKey('channel_output.id'))
    channel_output = db.relationship('ChannelOutput')
    alarm_id = db.Column(db.Integer,db.ForeignKey('alarm.id'))
    alarm = db.relationship('Alarm')
    condition_id = db.Column(db.Integer,db.ForeignKey('condition.id'))
    condition = db.relationship('Condition')

class AlarmOutputSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "value", "channel_output_id", "alarm_id", "condition_id")

class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    hexadecimal = db.Column(db.Integer)
    rgb = db.Column(db.Integer)

class ColorSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "hexadecimal", "rgb")


class Led(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    brightness = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    channel_output_id = db.Column(db.Integer,db.ForeignKey('channel_output.id'))
    channel_output = db.relationship('ChannelOutput')

class LedSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "brigness", "priority", "channel_output_id")

class LedOutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    led_start = db.Column(db.Integer, nullable=False)
    color_start_id = db.Column(db.Integer, db.ForeignKey(Color.id))
    color_start = db.relationship("Color", backref="color", uselist=False, foreign_keys=[color_start_id])
    value_start = db.Column(db.String)
    led_end = db.Column(db.Integer, nullable=False)
    color_end_id = db.Column(db.Integer, db.ForeignKey(Color.id))
    color_end = db.relationship("Color", backref="reference", uselist=False, foreign_keys=[color_end_id])
    value_end = db.Column(db.String)
    led_id = db.Column(db.Integer,db.ForeignKey('led.id'))
    led = db.relationship('Led')

class LedSchema(ma.Schema):
    class Meta:
        model = ChannelInput
        fields = ("id", "name", "max_blink")
db.create_all()
db.session.commit()