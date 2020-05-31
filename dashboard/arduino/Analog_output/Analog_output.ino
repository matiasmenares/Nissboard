
#include <Wire.h>
#define sensorPin A0
// bar graph

byte count;

//Send Data 

String sender;

void setup()
{
  Serial.begin(9600); // start monitoring raw voltage for calibration
}


void loop() // Start loop
{
 int analog_0 = analogRead(A0);
 int analog_1 = analogRead(A1);
 int analog_2 = analogRead(A2);
 int analog_3 = analogRead(A3);
 int analog_4 = analogRead(A4);
 sender = "{'A0': "+String(analog_0)+",'A1': "+String(analog_1)+",'A2': "+String(analog_2)+",'A3': "+String(analog_3)+",'A4': "+String(analog_4)+"}";
 Serial.println(sender);
}
