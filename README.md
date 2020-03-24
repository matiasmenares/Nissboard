# Nissboard

### Version
0.9 (Beta)

![Nissboard Gif](https://github.com/matiasmenares/Nissboard/blob/master/extras/ezgif.com-video-to-gif.gif?raw=true)

### Whats is Nissboard?

Nissboard is a realtime dashbaord for Nissan (soon for others brands) made with Raspberry pi, this project tested only in Nissan Skyline R34 for a while.

## Requirements

* Raspberry pi 3 
* Python3
* Screen LCD
* Accelerometer
* GPS
* Nissan consult

## Tested on

* Nissan Skyline R34 RB25DET
* Raspberry pi 3B+
* Raspbian GNU/Linux 10 (buster)
* Accelerometer ADXL345

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
pip3 install requirements.txt 
```
#### Run server
```
python3 /home/pi/nissboard/accelerometer/dashboard/dash.py -d /dev/ttyUSB0 &amp;
```
Note: /dev/ttyUSB0 is a path of USB Nissan consult, in development mode just add any path

## Whats next?

We will add a GPS to get time on track and add the following sensors through an Arduino (to define) communicate with USB To Pi

* Boost
* Oil Press
* Oil Temp
* AFR

## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/alcheco"><img src="https://avatars2.githubusercontent.com/u/1217849?s=400&u=1ff2307579594780330c3f9f29efcb54b2ba567a&v=4" width="100px;" alt=""/><br /><sub><b>Alfonso Pacheco</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=alcheco" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/fbarriosCL"><img src="https://avatars0.githubusercontent.com/u/10846283?s=400&u=b4c9e041a98ad862386e2068abd31fdd9fa9168e&v=4" width="100px;" alt=""/><br /><sub><b>Felipe Barrios</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=fbarriosCL" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/pornoob"><img src="https://avatars0.githubusercontent.com/u/10846283?s=400&u=b4c9e041a98ad862386e2068abd31fdd9fa9168e&v=4" width="100px;" alt=""/><br /><sub><b>Claudio Olivares</b></sub></a><br /><a href="https://github.com/matiasmenares/Nissboard?author=pornoob" title="Code">🧠</a></td>
  </tr>
</table>