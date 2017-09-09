int potentiometer = A0; 
int potValue;
int ledRed = 11;
void setup() {
  pinMode(potentiometer, INPUT);
  Serial.begin(9600);
  pinMode(ledRed, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
 potValue = analogRead(potentiometer);
 Serial.println(potValue);
 int mappedValue = map(potValue, 0, 1023, 0, 255);
 analogWrite(ledRed, mappedValue);
 // put your main code here, to run repeatedly:

}
