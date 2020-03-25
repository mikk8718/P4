/*
  The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * LCD VSS pin to ground
 * LCD VCC pin to 5V
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)

 */

// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int a0Pin = A0;
int a1Pin = A1;
int a2Pin = A2;
int a4Pin = A4;
int a5Pin = A5;
String s1 = "Footsteps";
String s2 = "Send Nudes";
String s3 = "The act of anal penetration";

// RGB LED vars:
int redP = 10;
int greenP = 6;
int blueP = 9;


void setup() {
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows:
  lcd.setCursor(0, 0);  // put cursor to the left of first line
  lcd.print("Selecting:");
  Serial.begin(9600);   // for potentiometer (unnecessary?)
  lcd.setCursor(0, 1);
  //lcd.scrollDisplayLeft();
  
  //RGB LED setup:
  pinMode(blueP, OUTPUT);
  pinMode(greenP, OUTPUT);
  pinMode(redP, OUTPUT);
  
  //buttons setup
  pinMode(a1Pin, INPUT);
  pinMode(a2Pin, INPUT);
}

// RGB LED custom funcion
void color(int red, int green, int blue) {
  digitalWrite(redP, red);
    digitalWrite(greenP, green);
    digitalWrite(blueP, blue);
}

void loop() {
  lcd.noAutoscroll();
  //lcd.setCursor(0, 0);
  //lcd.print(millis() / 1000);
  int val = analogRead(a0Pin);
  int pitch = analogRead(a4Pin);
  int echo = analogRead(a5Pin);
  
  if (digitalRead(a1Pin) == HIGH) {
    lcd.setCursor(0, 0); 
    lcd.print("Playing:        ");
    Serial.println("PLAY pressed");
  }
  if (digitalRead(a2Pin) == HIGH) {
    lcd.setCursor(0, 0); 
    lcd.print("Selecting:      ");
    Serial.println("STOP pressed");
  }
  
  if (val <= 300) {
    if (s1.length() < 16) {
      //Serial.println("dick"); 
      s1 += " ";
    }
    lcd.print(s1);
    lcd.setCursor(0, 1); // set the cursor to column 0, line 1
    
    //RGB dependent on button presses
    if (digitalRead(a1Pin) == HIGH) {
       color(200, 0, 0); }
    if (digitalRead(a2Pin) == HIGH) {
      color(0, 0, 0); }
  }
  if (val > 300 && val < 600){ 
    if (s2.length() < 16) {
      //Serial.println("dick"); 
      s2 += " ";
    }
    lcd.print(s2);
    lcd.setCursor(0, 1);
    //lcd.setCursor(0, 0);
    lcd.noAutoscroll();
    
    if (digitalRead(a1Pin) == HIGH) {
      color(0, 200, 0); }
    if (digitalRead(a2Pin) == HIGH) {
      color(0, 0, 0); }
  }
  if (val > 600){
    if (s2.length() < 16) {
      //Serial.println("dick"); 
      s2 += " ";
    }
    else {
    //lcd.autoscroll(); 
    }
    lcd.print(s3);
    lcd.setCursor(0, 1);
    
    if (digitalRead(a1Pin) == HIGH) {
      color(0, 0, 250); }
    if (digitalRead(a2Pin) == HIGH) {
      color(0, 0, 0); }
  }
  
  //Serial.println(val);
  delay(1);
}
 
