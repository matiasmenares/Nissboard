from flask_restful import Resource
from flask import request, jsonify
from rpi_backlight import Backlight

class ScreenSetting(Resource):

    def __init__(self):
        self.backlight = Backlight()

    def get(self):
        return {'brightness': self.backlight.brightness }

    def post(self):
        self.backlight.brightness = request.json['screen']
        return {'response': True}