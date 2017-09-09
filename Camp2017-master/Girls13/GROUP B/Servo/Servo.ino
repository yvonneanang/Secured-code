int potentiometer = A0;
int potValue;
int mappedValue;
#include<Servo.h>
Servo myservo;
int Yvonne= 3;
void setup() {
  myservo.attach(9);
  pinMode(potentiometer, INPUT);
  pinMode(Yvonne, OUTPUT);
  Serial.begin(9600);
  
  // put your setup code here, to run once:

}

void loop() {
  
  potValue= analogRead(potentiometer);
  mappedValue=map(potValue, 0, 1023, 0, 180);
  myservo.write( mappedValue);
  int ledVal = map(potValue, 0, 1023, 0, 255);
  analogWrite(Yvonne, ledVal);
 
  
  // put your main code here, to run repeatedly:

}
