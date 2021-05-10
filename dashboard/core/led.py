import board
# import neopixel
from colour import Color
import time
from model.models import db, ColorSchema, Led as LedModel, LedSchema, LedOutput, LedSchema

class Led():
    def __init__(self):
        # self.pixels = neopixel.NeoPixel(board.D18, 8)
        self.pixels = [0,1,2,3,4,5,6,7,8,9]
        self.leds = None
        self.all_on = False
    def start(self, outputs):
        for led in self.leds:
            output = self.find_output(outputs, led.channel_output_id)
            for led_output in LedOutput.query.filter_by(led_id=led.id):
                self.on(led, led_output, output)

    def find_output(self, outputs, output_id):
        for output in outputs:
            if output['id'] == output_id:
                return output

    def on(self, led, led_output, output):
        if output['value'] > float(led_output.value_end):
            self.blink(led_output)
        elif output['value'] > float(led_output.value_start) and output['value'] < float(led_output.value_end):
            self.raw_data(led, led_output, output)
        else:
            self.turn_off(led_output)

    def raw_data(self, led, led_output, output):
        result = self.linear_function(output['value'], float(led_output.value_start), float(led_output.value_end), output['min_output'], output['max_output'])
        result_percent = ((result * 100) / output['max_output'])
        percent = []
        led_total = self.get_led_total(led_output)
        total_percent = 100 / led_total
        self.turn_on(result_percent, led_total, total_percent,led, led_output, output)

    def turn_on(self, result_percent, led_total, total_percent, led, led_output, output):
        start = Color(led_output.color_start.name)
        colors = list(start.range_to(Color(led_output.color_end.name), led_total))
        for led_strip in range((led_output.led_start-1), (led_output.led_end)):
            rgb = self.get_rgb(colors, led_strip)
            self.pixels.brightness = (float(led.brightness) / 100)
            if result_percent > (total_percent * (led_strip + 1)):
                self.pixels[led_strip] = rgb
            else:
                if result_percent < total_percent:
                    rgb = self.get_rgb(colors, (led_output.led_start-1))
                    self.pixels[(led_output.led_start-1)] = rgb
                elif result_percent >= 97.0:
                    rgb = self.get_rgb(colors, (led_output.led_end-1))
                    self.pixels[(led_output.led_end - 1)] = rgb
                    self.all_on = True
                elif result_percent < (total_percent * led_strip):
                    self.pixels[led_strip] = (0, 0, 0)

    def blink(self, led_output):
        if self.all_on:
            self.turn_off(led_output)
        else:
            led_total = self.get_led_total(led_output)
            start = Color(led_output.color_start.name)
            colors = list(start.range_to(Color(led_output.color_end.name), led_total))
            for led_strip in range((led_output.led_start-1), (led_output.led_end)):
                rgb = self.get_rgb(colors, led_strip)
                self.pixels[led_strip] = rgb
            self.all_on = True

    def get_led_total(self, led_output):
        led_total = 1
        for led_strip in range(led_output.led_start, led_output.led_end):
            led_total += 1
        return led_total

    def get_rgb(self, colors, led_strip):
        r = self.linear_function(colors[led_strip].rgb[0], 0, 1 , 0, 255)
        g = self.linear_function(colors[led_strip].rgb[1], 0, 1 , 0, 255)
        b = self.linear_function(colors[led_strip].rgb[2], 0, 1 , 0, 255)
        return (int(r), int(g), int(b))

    def turn_off(self, led_output):
        for led_strip in range((led_output.led_start-1), (led_output.led_end)):
            self.pixels[led_strip] = (0, 0, 0)
        self.all_on = False

    def linear_function(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min