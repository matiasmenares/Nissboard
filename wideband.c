#include "U8glib.h"

#define OLED_RESET 4
U8GLIB_SSD1306_128X64 u8g(U8G_I2C_OPT_NONE | U8G_I2C_OPT_DEV_0); // I2C / TWI


void setup() {

  // screen is mounted upside down. 180 rotation is needed to display correctly
  u8g.setRot180();
  Serial.begin(9600);
}


void loop() {

  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);

  // convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);

  // convert voltage to a value mirroring AFR data displayed on the AEM gauge
  float AFR = (voltage * 2.375) + 7.3125;

  // print the AFR value on serial monitor
  Serial.println(AFR);

  // draw the value on the OLED screen
  u8g.firstPage();
  do
  {
    u8g.setFont(u8g_font_unifont);
    u8g.setPrintPos(36, 10);
    u8g.print("AIR/FUEL");
    u8g.setPrintPos(36, 30);
    u8g.print(AFR);

  }
  while ( u8g.nextPage() );

  // delay added to slow readings displayed. didn't work
  //delay(100);

}