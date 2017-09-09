int potentiometer=A0;
int ledRed=13;
int ledYellow=12;
int ledGreen=11;
int ledBlue=10;
int ledWhite=9;
int potValue;
int mappedValue;
void setup() {
  pinMode(potentiometer, INPUT);
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledBlue, OUTPUT);
  pinMode(ledWhite, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
potValue=analogRead(potentiometer);
mappedValue= map(potValue, 0, 1023, 0, 255);
if ((potValue>=0)&&(potValue<=204)){
digitalWrite(ledRed, HIGH);
digitalWrite(ledYellow, LOW);
digitalWrite(ledGreen, LOW);
digitalWrite(ledBlue, LOW);
digitalWrite(ledWhite, LOW);}
if ((potValue>=205)&&(potValue<=410)){
digitalWrite(ledRed, HIGH);
digitalWrite(ledYellow, HIGH);
digitalWrite(ledGreen, LOW);
digitalWrite(ledBlue, LOW);
digitalWrite(ledWhite, LOW);}
if ((potValue>=206)&&(potValue<=616)){
digitalWrite(ledRed, HIGH);
digitalWrite(ledYellow, HIGH);
digitalWrite(ledGreen, HIGH);
digitalWrite(ledBlue, LOW);
digitalWrite(ledWhite, LOW);}
if ((potValue>=617)&&(potValue<=816)){
digitalWrite(ledRed, HIGH);
digitalWrite(ledYellow, HIGH);
digitalWrite(ledGreen, HIGH);
digitalWrite(ledBlue, HIGH);
digitalWrite(ledWhite,LOW);}

if ((potValue>=817)&&(potValue>=1023)){
digitalWrite(ledRed, HIGH);
digitalWrite(ledYellow, HIGH);
digitalWrite(ledGreen, HIGH);
digitalWrite(ledBlue, HIGH);
digitalWrite(ledWhite, HIGH);}
  // put your main code here, to run repeatedly:

}
