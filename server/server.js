var PATH_TO_SERIAL_PORT = '';
var path = require('path');
var fs = require('fs');
var express = require('express');
var serialport = require("serialport");
var SerialPort = serialport.SerialPort;

// Don't set the serialport on development
if (process.env.NODE_ENV != "development"){
  var sp =  new serialport('/dev/tty.usbserial-A103NKGZ', { baudRate: 9600 });
}

// All the values we are getting from the ECU
var rpm, mph, coolantTemp = 0;

var currentData= [];
var frameStarted = false;
var lengthByte;

function handleData(data, bytesExpected){
  // create an array of the size of requested data length and fill with requested data
  for(var i = 0; i < data.length; i++){
    // read just 1 byte at a time of the stream
    var char = data.toString('hex',i,i+1);
    if(char === "ff"){
      // Beginning of data array, the frame has started
      frameStarted = true;
      // Get rid of last frame of data
      currentData = [];
      // remove last lengthByte number so that we can check what this frame's byte should be
      lengthByte = undefined;
    }else if(frameStarted){
      // frame has started
      if(!lengthByte){
        // read lengthByte from the ECU
        lengthByte = parseInt(char, 16);
      }else{
        // push byte of data onto our array
        currentData.push(parseInt(char, 16));
      }
    }
  }
  if(currentData.length === bytesExpected){
    // End of data, return the array of data
    frameStarted = false;
    return currentData.slice();
  }
}

function convertRPM(mostSignificantBit, leastSignificantBit){
  // combine most significant bit and least significant bit and convert to RPM
  return ((mostSignificantBit << 8) + leastSignificantBit) * 12.5;
}

function convertCoolantTemp(data){
  // Subtract 50 for Celsius
  var celciusCoolantTemp = data - 50;
  // Convert celcius to fahrenheit
  var fahrenheitCoolantTemp = celciusCoolantTemp * 1.8 + 32;

  return fahrenheitCoolantTemp;
}

function convertKPH(data){
  // data * 2 gives KPH
  return data * 2;
}

function convertMPH(data){
  // data * 2 gives KPH
  return convertKPH(data) * 0.6213711922;
}

function parseData(data){

  if(data !== undefined){
    rpm = convertRPM(data[1], data[2]);
    coolantTemp = convertCoolantTemp(data[0]);
    mph = convertMPH(data[3]);
  }

}

var isConnected = false;
var command = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0b,0xF0];
var bytesRequested = (command.length - 1) / 2;

// Don't run this part for development.
if (process.env.NODE_ENV != "development"){

  sp.on("open", function () {
    // Write initialization bytes to the ECU
    sp.write([0xFF, 0xFF, 0xEF], function(err, results) {});
    sp.on('data', function(data) {
      // Check to see if the ECU is connected and has sent the connection confirmation byte "10"
      if(!isConnected && data.toString('hex') === "10"){
        console.log("connected");
        isConnected = true;
        // Tell the ECU what data we want it to give us
        sp.write(command, function(err,results){});
      }else{
        // Read the data from the stream and parse it
        parseData(handleData(data, bytesRequested));
      }
    });
  });
}

// Server part
var app = express();

app.use('/', express.static(path.join(__dirname, 'public')));

var server = app.listen(8090);
console.log('Server listening on port 8090');

// Socket.IO part
var io = require('socket.io')(server);

const function_interval = (socket) => { 
	if (process.env.NODE_ENV === "development"){
		if(rpm < 7200){
			rpm += 220
		} else{
			rpm = 0
		}
		if(mph < 120){
			mph += 1
		} else{
			mph = 0
		}
		if(coolantTemp < 200){
			coolantTemp += 10
		} else{
			coolantTemp = 0
		}
	}
	socket.emit('ecuData', {'rpm': Math.floor(rpm),'mph':Math.floor(mph),'coolantTemp':Math.floor(coolantTemp)});
}

const on_connection = (socket) => {
  console.log('New client connected!');
  setInterval(function_interval.bind(this, socket), 200);
};

// ejo ejo

io.on('connection', on_connection);
