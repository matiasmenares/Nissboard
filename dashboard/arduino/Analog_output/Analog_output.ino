
#include <Wire.h>
#define sensorPin A0
// bar graph

byte count;

//Send Data 

String sender;
int Vin= 5;
float Vout= 0;
float R1= 1000;
float R2= 0;
float buffer= 0;

void setup()
{
  Serial.begin(19200); // start monitoring raw voltage for calibration
}


void loop() // Start loop
{
 int analog_0 = analogRead(A0);
 int analog_1 = analogRead(A1);
 int analog_2 = analogRead(A2);
 int analog_3 = analogRead(A3);
 int analog_4 = analogRead(A4);
 int analog_5 = analogRead(A5);
 int analog_6 = analogRead(A6);
 int analog_7 = analogRead(A7);

 sender = "{'A0': "+String(analog_0)+",'A1': "+String(analog_1)+",'A2': "+String(analog_2)+",'A3': "+String(analog_3)+",'A4': "+String(analog_4)+", 'A5': "+String(analog_5)+", 'A6': "+String(analog_6)+", 'A7': "+String(analog_7)+"}";
 Serial.println(sender);
}

int resistance(int raw){
    buffer= raw * Vin;
    Vout= (buffer)/1024.0;
    buffer= (Vin/Vout) -1;
    R2= R1 * buffer;
    return R2;
}
