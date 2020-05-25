#include <LiquidCrystal.h>

int potPinLCD = A1;
int potPinVol = A5;
int potPinReverb = A3;
int potPinPitch = A4;
LiquidCrystal lcd(12, 9, 5, 4, 3, 2);
int button = 8;
int button2 = 7;
int selectedTrack;
int selectedReverb;
int selectedPitch;


void setup() {
    Serial.begin(115200); 
    lcd.begin(16, 2); 
    pinMode(button, INPUT);
    pinMode(button2, INPUT);
    delay(1000);
   
}

void loop() {
  int valPotLCD = 0;
  int valPotReverb = 0;
  int valPotPitch = 0;
  valPotLCD = analogRead(potPinLCD);
  valPotReverb = analogRead(potPinReverb);
  valPotPitch = analogRead(potPinPitch); 
  
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
    
//Reverb----------------------------------------
 if (valPotReverb > 0 && valPotReverb < 341){
    selectedReverb = 1;
 }
 if (valPotReverb > 341 && valPotReverb < 682){
    selectedReverb = 2;
 }
 if (valPotReverb > 682 && valPotReverb < 1023){
    selectedReverb = 3;
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
    Serial.print("selectedReverb");
    Serial.println(selectedReverb);
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
