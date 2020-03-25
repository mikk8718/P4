
#include <LiquidCrystal.h>

int potPin = 1;
int potPin2 = 2;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
    Serial.begin(9600);
    lcd.begin(16, 2);
    //lcd.print("David is a dick");
}

void loop() {
  //lcd.setCursor(0, 1);
  int valPotLCD = 0;
  valPotLCD = analogRead(potPin); //Value goes from 0 to 1023 with potentiometers
    if (valPotLCD > 0 && valPotLCD < 800){
      lcd.setCursor(0, 1);
      Serial.println("interval 1");
      lcd.print("David is a dick  ");
  }
    if (valPotLCD > 801 && valPotLCD < 900){
      lcd.setCursor(0, 1);
      Serial.println("interval 2");
      lcd.print("David is a cunt  ");
  }
    if (valPotLCD > 901 && valPotLCD < 1023){
      lcd.setCursor(0, 1);
      Serial.println("interval 3");
      lcd.print("David is a twat ");
  }
  //This is for testing the rotary pots
  valPotLCD = analogRead(potPin2);
  if (valPotLCD > 901 && valPotLCD < 1023){
      lcd.setCursor(0, 0);
      Serial.println("Pot Test");
      lcd.print("David is a Javid");
  }
  Serial.println();
}
