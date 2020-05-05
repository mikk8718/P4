#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
SoftwareSerial mySerial(11, 10);

int potPinLCD = A1;
int potPinVol = A5;
int potPinEcho = A3;
int potPinPitch = A4;
LiquidCrystal lcd(12, 9, 5, 4, 3, 2);
int button = 8;
int button2 = 7;
int selectedTrack;
int selectedEcho;
int selectedPitch;
int selectedVol;

void setup() {
    Serial.begin(115200); //this is the rate for the serial monitor, can be changed, doesn't matter much.
    lcd.begin(16, 2); //This is the LCD (Collums, Rows) so max 16 letters per row.
    pinMode(button, INPUT);
    pinMode(button2, INPUT);
    delay(1000);
   
}
void loop() {
  int valPotLCD = 0;
  int valPotVol = 0;
  int valPotEcho = 0;
  int valPotPitch = 0;
  valPotLCD = analogRead(potPinLCD);
  valPotVol = analogRead(potPinVol);
  valPotEcho = analogRead(potPinEcho);
  valPotPitch = analogRead(potPinPitch); //Value goes from 0 to 1023 with potentiometers
  //From here we treshhold values from the slider to display text on the LCD.
  //However due to a 1k resistor being attached to the slider, the first threshold is larger
  //Than the other... IDK if this is why, but my best guess. (It should change around 1/3 of the way for each.

//LCD------------------------------------
  if (valPotLCD > 0 && valPotLCD < 150){
    selectedTrack = 3;
    lcd.setCursor(0, 1);
    lcd.print("Adventure track ");
  }
  if (valPotLCD > 150 && valPotLCD < 275){
    selectedTrack = 2;
    lcd.setCursor(0, 1);
    lcd.print("Journey track   ");
  }
  if (valPotLCD > 275 && valPotLCD < 1023){
    selectedTrack = 1;
    lcd.setCursor(0, 1);
    lcd.print("Mikkel track   ");
  }
//Volume-------------------------------------

   if (valPotVol > 0 && valPotVol < 341){
      selectedVol = 1;
   }
   if (valPotVol > 341 && valPotVol < 682){
      selectedVol = 2;
   }
   if (valPotVol > 682 && valPotVol < 1023){
      selectedVol = 3;
   }
   
//Echo----------------------------------------
 if (valPotEcho > 0 && valPotEcho < 341){
    selectedEcho = 1;
 }
 if (valPotEcho > 341 && valPotEcho < 682){
    selectedEcho = 2;
 }
 if (valPotEcho > 682 && valPotEcho < 1023){
    selectedEcho = 3;
 }

//Pitch---------------------------------------
  if (valPotPitch > 0 && valPotPitch < 341){
    selectedPitch = 1;
 }
  if (valPotPitch > 341 && valPotPitch < 682){
    selectedPitch = 2;
 }
  if (valPotPitch > 682 && valPotPitch < 1023){
    selectedPitch = 3;
 }
    
  if (digitalRead(button) == HIGH){
    Serial.print("selectedTrack");
    Serial.println(selectedTrack);
    Serial.print("selectedVol");
    Serial.println(selectedVol);
    Serial.print("selectedEcho");
    Serial.println(selectedEcho);
    Serial.print("selectedPitch");
    Serial.println(selectedPitch);
    Serial.print("playButton");
    Serial.println(1);
    delay(1000);
    }
  
  if (digitalRead(button2) == HIGH){
    Serial.print("stopButton");
    Serial.println(1);
    delay(1000);
  }
  
  lcd.setCursor(0, 0);
  lcd.print(valPotVol);
}
