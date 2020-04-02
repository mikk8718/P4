//
//#include <LiquidCrystal.h>
//#include <DFRobotDFPlayerMini.h>
//#include <SoftwareSerial.h>
//
//SoftwareSerial mySoftwareSerial(10, 11); // RX, TX pins on DF
//DFRobotDFPlayerMini myDFPlayer;
//int potPin = A1;
//int pauseBut = A4;
//int playBut = A5;
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
//boolean playing = false;
//int playState = 0;
//
//void setup() {
//    Serial.begin(9600); //this is the rate for the serial monitor, can be changed, doesn't matter much.
//    lcd.begin(16, 2); //This is the LCD (Collums, Rows) so max 16 letters per row.
//
//    //buttons
//    pinMode(pauseBut, INPUT);
//    pinMode(playBut, INPUT);
//    
//}
//void loop() {
//  int valPotLCD = 0;
//  valPotLCD = analogRead(potPin); //Value goes from 0 to 1023 with potentiometers
//  //From here we treshhold values from the slider to display text on the LCD.
//  //However due to a 1k resistor being attached to the slider, the first threshold is larger
//  //Than the other... IDK if this is why, but my best guess. (It shoudl change around 1/3 of the way for each.
//    if (valPotLCD > 0 && valPotLCD < 800){
//      lcd.setCursor(0, 1);
//      Serial.println("interval 1");
//      lcd.print("David is a dick  ");
//  }
//    if (valPotLCD > 801 && valPotLCD < 900){
//      lcd.setCursor(0, 1);
//      Serial.println("interval 2");
//      lcd.print("David is a cunt  ");
//  }
//    if (valPotLCD > 901 && valPotLCD < 1023){
//      lcd.setCursor(0, 1);
//      Serial.println("interval 3");
//      lcd.print("David is a twat ");
//  }
//  playState = digitalRead(playBut);
//  //IsPlaying
//  if (playState = HIGH){
//    myDFPlayer.play(1);
//  }else {
//    playState == LOW;
//    myDFPlayer.pause(); 
////  }
//  playState = digitalRead(playBut);
//  //PlayButton
//  if (playState == LOW){
//    myDFPlayer.play(1);
//    Serial.println("PLAY PRESSED");
//  }
//  Serial.println();
//}

/////////////////////////////
#include <DFRobotDFPlayerMini.h>
#include <SoftwareSerial.h>
SoftwareSerial mySoftwareSerial(10, 11); // RX, TX pins on DF
DFRobotDFPlayerMini myDFPlayer;
int buttonPin = A5;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == LOW) {
    Serial.println("Button Pressed");
    myDFPlayer.play(1);
  }
  Serial.println();
}
