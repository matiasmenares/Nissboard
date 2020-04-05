
//Arduino pro micro, .93" I2C OLED use pin 2 for SDA and 3 for SCL ***Look up i2c pins for your controller

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define sensorPin A0

int OLED_RESET = 4;
Adafruit_SSD1306 display(OLED_RESET); //driver for the screen

// bar graph

float rawval = 0; // Setup raw sensor value
float barboost = 0; // Setup value for boost bar

// peak

int boostPeakReset = 4000; // time in milis to reset peak value
float boostPeak = 0.00;
float boostMax = 0.00;
unsigned long boostPeakTimer = 0;



// log

byte count;
byte sensorArray[128];
byte drawHeight;
boolean filled = 0; //decide either filled, or dot-display. 0==dot display.


//Send Data 

String sender;
String peak;

void setup()
{
  Serial.begin(9600); // start monitoring raw voltage for calibration
  display.begin(SSD1306_SWITCHCAPVCC); // 3.3V power supply
  display.clearDisplay(); // Clear the display and ram
  display.display();
  delay(2000); // display Adafruit logo for 2 seconds
  for (count = 0; count <= 128; count++) //zero all elements
  {
    sensorArray[count] = 0;
  }
}


void loop() // Start loop
{


  
  int boostmbar = map(analogRead(sensorPin), 21, 961, 100, 2600);
  rawval = analogRead(0); // Read MAP sensor raw value on analog port 0
  barboost = (((rawval * 0.19) - 69.45) + 10); // Calculate boost value for the graph



  if (boostPeak < boostmbar && boostmbar > 0.50) {
    boostPeak = boostmbar;
    boostPeakTimer = millis();
    if (boostMax < boostPeak) {
      boostMax = boostPeak;
    }
  }
  else if (boostPeak > boostmbar && (millis() - boostPeakTimer) > boostPeakReset) {
    boostPeak = 0.00;
  }


  // log 

  drawHeight = map(analogRead(A0), 0, 1023, 0, 25 );  

  sensorArray[0] = drawHeight;

  for (count = 55; count <= 128; count++ )
  {
    if (filled == false)
    {
      display.drawPixel(count, 71 - sensorArray[count - 55], WHITE);
    }
    else
      display.drawLine(count, 1, count, 71 - sensorArray[count - 55], WHITE); 
  }

  for (count = 80; count >= 2; count--) // count down from 160 to 2
  {
    sensorArray[count - 1] = sensorArray[count - 2];
  }
;

  display.setTextSize(1); //Display peak boost
  display.setCursor(97, 10);
  peak = (((boostPeak * 0.001) - 0.865)*14); // 0.97 = 970mbar atmospheric pressure correction

  if ((((boostmbar  * 0.001) - 0.865)*14) < 0) {
    display.println(((boostmbar * 0.001) - 0.865)*63.2);
    sender = "{'psi': "+String(((boostmbar * 0.001) - 0.865)*63.2)+",'peak': "+String(peak)+", 'raw': "+ String(rawval) +"}";
  }
  else if ((((boostmbar * 0.001) - 0.865)*14) > 0) {
    display.println(((boostmbar * 0.001) - 0.865)*14);   // calibrated for a 2.5 bar sensor in Denver (+/- 1psi)
    sender = "{'psi': "+String(((boostmbar * 0.001) - 0.865)*14)+", 'peak': "+String(peak)+",'raw': "+ String(rawval) +"}";
}

  delay(1);
    Serial.println(sender);
  delay(10); // delay half second between numbers
}
