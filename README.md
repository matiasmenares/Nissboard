# Nissboard

### Version
0.9 (Beta)

[![Code Climate](https://codeclimate.com/github/matiasmenares/Nissboard/badges/gpa.svg)](https://codeclimate.com/github/matiasmenares/Nissboard)

![Nissboard Gif](https://github.com/matiasmenares/Nissboard/blob/master/extras/video-readme.gif?raw=true)

### Whats is Nissboard?

Nissboard is a realtime dashboard for Nissan (soon for others brands) made with Raspberry pi, this project has been tested only in Nissan Skyline R34 for a while.

## Requirements

* Vuejs
* Python3
* Raspberry pi 3 
* Screen LCD
* Accelerometer
* GPS
* Nissan consult
* Serial to USB cable

## Tested on

* Nissan Skyline R34 RB25DET
* Raspberry pi 3B+
* Raspbian GNU/Linux 10 (buster)
* Accelerometer ADXL345
* Accelerometer ADXL345
* Arduino Nano every

## Sensor Displayed

* KPH
* RPM
* Water temp
* TPS
* Battery Volt
* Timming
* 02
* AAC
* Injector
* Lamda
* G-force meter

## Start up

### Frontend

#### Project setup
```
npm install
```
#### Compiles and hot-reloads for development
```
npm run serve
```

### Backend

#### Project setup
```
pip3 install -r requirements.txt 
```
#### Run server
```
python3 dashboard/dash.py -d /dev/ttyUSB0 -g /dev/cu.usbserial-0001 -a /dev/cu.usbmodem144101
```
Note: /dev/ttyUSB0 is a path of USB Nissan consult, in development mode just add any path

## Screen Shots
<img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/dash-1.png" width="380"><img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/dash-2.png" width="380">
<img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/track-list.png" width="380"><img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/track-map.png" width="380">
<img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/g-force.png" width="380"><img src="https://raw.githubusercontent.com/matiasmenares/Nissboard/master/extras/setting.png" width="380">

## Whats next?

We will add a GPS to get time on track and add the following sensors through an Arduino (to define) communicate with USB To Pi

* Boost
* Oil Press
* Oil Temp
* AFR

### How to Contributing?

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'ADD: some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/alcheco"><img src="https://avatars2.githubusercontent.com/u/1217849?s=400&u=1ff2307579594780330c3f9f29efcb54b2ba567a&v=4" width="100px;" alt=""/><br /><sub><b>Alfonso Pacheco</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=alcheco" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/fbarriosCL"><img src="https://avatars0.githubusercontent.com/u/10846283?s=400&u=b4c9e041a98ad862386e2068abd31fdd9fa9168e&v=4" width="100px;" alt=""/><br /><sub><b>Felipe Barrios</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=fbarriosCL" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/pornoob"><img src="https://avatars1.githubusercontent.com/u/6501343?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Claudio Olivares</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=pornoob" title="Code">🧠</a></td>
  </tr>
</table>

Inpired in this project https://github.com/gregsqueeb/consultDash