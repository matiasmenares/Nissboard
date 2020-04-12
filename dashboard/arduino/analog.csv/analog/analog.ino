
//Arduino pro micro, .93" I2C OLED use pin 2 for SDA and 3 for SCL ***Look up i2c pins for your controller

#include <Wire.h>
#define sensorPin A0
// bar graph

float rawval = 0; // Setup raw sensor value
float barboost = 0; // Setup value for boost bar

// peak

int boostPeakReset = 4000; // time in milis to reset peak value
float boostPeak = 0.00;
float boostMax = 0.00;
unsigned long boostPeakTimer = 0;
float maxBar = 0.0;
float barAbsolute = 0.0;


// log

byte count;

//Send Data 

String sender;
String peak;

void setup()
{
  Serial.begin(9600); // start monitoring raw voltage for calibration
  maxBar = 2000;
}


void loop() // Start loop
{

 //int boostmbar = map(analogRead(sensorPin), 21, 1300, 100, 2600);
  int boostmbar = map(analogRead(sensorPin), 0, 1023, 0, maxBar);
  int boostpercentage = map(analogRead(sensorPin), 0, 1023, 0, 100);

  rawval = analogRead(0); // Read MAP sensor raw value on analog port 0
  barboost = (((rawval * 0.19) - 69.45) + 10); // Calculate boost value for the graph

  if (boostPeak < boostmbar && boostmbar > 0.50) {
    boostPeak = boostmbar;
  }
  
  peak = (((boostPeak * 0.001) - barAbsolute) * 14) - 14 ; // 0.97 = 970mbar atmospheric pressure correction

  if ((((boostmbar  * 0.001) * 14) - 14) < 0) {
    sender = "{'psi': "+String(((boostmbar * 0.001) * 14) - 14)+", 'peak': "+String(peak)+", 'raw': "+ String(rawval) +", 'voltage': "+String(rawval * (5.0 / 1023.0))+", 'boostmar': "+boostmbar+", 'percentage': "+boostpercentage+"}";
  }
  else if ((((boostmbar * 0.001) * 14) - 14) > 0) {
    sender = "{'psi': "+String(((boostmbar * 0.001) * 14) - 14)+", 'peak': "+String(peak)+",'raw': "+ String(rawval) +", 'voltage': "+String(rawval * (5.0 / 1023.0))+", 'boostmar': "+boostmbar+", 'percentage': "+boostpercentage+"}";
}

  Serial.println(sender);
}
