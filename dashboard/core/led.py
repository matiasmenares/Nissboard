import board
import neopixel
from colour import Color
import time
from model.models import db, ColorSchema, Led as LedModel, LedSchema, LedOutput, LedSchema

class Led():
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 8)

    def start(self, outputs):
        for led in LedModel.query.all():
            output = self.find_output(outputs, led.channel_output_id)
            for led_output in LedOutput.query.filter_by(led_id=led.id):
                self.on(led, led_output, output)

    def find_output(self, outputs, output_id):
        for output in outputs:
            if output['id'] == output_id:
                return output

    def on(self, led, led_output, output):
        if output['value'] > float(led_output.value_start) and output['value'] < float(led_output.value_end):
            self.raw_data(led, led_output, output)
        else:
            self.turn_off(led_output)

    def raw_data(self, led, led_output, output):
        result = self.linear_function(output['value'], float(led_output.value_start), float(led_output.value_end), output['min_output'], output['max_output'])
        result_percent = ((result * 100) / output['max_output'])
        percent = []
        led_total = 0
        for led_strip in range(led_output.led_start, led_output.led_end):
            led_total += 1
        total_percent = 100/led_total
        self.turn_on(result_percent, led_total, total_percent,led, led_output, output)

    def turn_on(self, result_percent, led_total, total_percent, led, led_output, output):
        start = Color(led_output.color_start.name)
        colors = list(start.range_to(Color(led_output.color_end.name), led_total))
        for led_strip in range((led_output.led_start-1), (led_output.led_end-1)):
            if result_percent > (total_percent*led_strip):
                self.pixels.brightness = (float(led.brightness) / 100)
                self.pixels[led_strip] = colors[led_strip].rgb

    def turn_off(self, led_output):
        for led_strip in range(led_output.led_start, led_output.led_end):
            self.pixels[led_strip] = (0,0,0)

    def linear_function(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min