#include <Adafruit_MLX90614.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include "HX711.h"
#define DOUT 24
#define CLK 22
HX711 scale(DOUT, CLK);
float calibration_factor = 96651;
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified();
const int stepPin = 48;
#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
#define LCD_RESET A4
#define BLACK 0x0000
#define ILI9341_WHITE 0xFFFF

#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;
int16_t x = 20;
int16_t y = 80;
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
     while (!Serial);

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  } else if (!accel.begin()) {
    Serial.println("No valid sensor found");
    while (1);
  }

  scale.set_scale(157860);
  scale.tare();

  uint16_t identifier = tft.readID();
  identifier = 0x9341;
  tft.begin(identifier);
  tft.setRotation(1);
  tft.fillScreen(BLACK);
  tft.setTextSize(3);
  tft.setTextColor(ILI9341_WHITE);
  tft.setCursor(x+30, y-50);
  tft.print("SENSOR DATA");
  tft.setCursor(x, y);
  tft.print("Temp: ");
  tft.setCursor(x, y + 50);
  tft.print("Acc.z: ");
  tft.setCursor(x, y + 100);
  tft.print("Load: ");

  tft.setCursor(x+220, y);
  tft.print("C");
  tft.setCursor(x+220, y + 50);
  tft.print("M/s2");
  tft.setCursor(x+220, y + 100);
  tft.print("Kg ");
  // tft.setCursor(x, y + 150);
  // tft.print("Load: ");
}
void loop() {
  // put your main code here, to run repeatedly:
  readsensors();
  // float avgRPM = 0;
  // float objectTemperatureC = mlx.readObjectTempC();
  // sensors_event_t event;
  // accel.getEvent(&event);
  // float vibration = event.acceleration.z;
  // float load = scale.get_units();

  // String datatosend = String(objectTemperatureC) + "," + String(vibration) + "," + String(abs(load));
  // Serial.println(datatosend);
  // delay(100); // Adjust as needed for your application

}
void readsensors() {
  float avgRPM = 0;
  float objectTemperatureC = mlx.readObjectTempC();
  sensors_event_t event;
  accel.getEvent(&event);
  float vibration = event.acceleration.z;
  float load = scale.get_units();
  // if (Serial.available() > 0) {
  //   String command = Serial.readStringUntil('\n');
  //   command.trim();
  // if (command == "slowdrill" || command == "fastdrill"|| command== "stopmachine") {
  //     if (command == "slowdrill") {
  //       speed = 200;
  //     } else if (command == "fastdrill") {
  //       speed = 255;
  //     }
  //     else if (command == "stopmachine") {
  //       analogWrite(enA, 0);
  //       digitalWrite(enPin, HIGH);
  //       timebt = 0;
  //       speed = 0;
  //     }
  // }}
  String datatosend = String(objectTemperatureC) + "," + String(vibration) + "," + String(load);
  Serial.println(datatosend);
  int16_t xRect = x + 120;
  int16_t yRect = y;
  int16_t widthRect = 25;
  int16_t heightRect = tft.height();
  tft.setCursor(xRect, yRect);
  tft.fillRect(xRect, yRect, 80, 100, BLACK);
  tft.print(objectTemperatureC, 1);

  int16_t yRect1 = y + 50;
  tft.setCursor(xRect, yRect1);
  tft.fillRect(xRect, yRect1, 80, 100, BLACK);
  tft.print(vibration, 1);

  int16_t yRect2 = y + 100;
  tft.setCursor(xRect, yRect2);
  tft.fillRect(xRect, yRect2, 80, 100, BLACK);
  tft.print(abs(load), 1);

  // int16_t yRect3 = y + 150;
  // tft.setCursor(xRect, yRect3);
  // tft.fillRect(xRect, yRect3, 80, 100, BLACK);
  // tft.print(load, 1);
}
