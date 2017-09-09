int ledRed = 13;
int ledBlue = 12;
int ledGreen = 10;
void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledBlue, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  digitalWrite(ledRed, HIGH);
  digitalWrite(ledBlue, LOW);
  digitalWrite(ledGreen, LOW);
  delay(100);
  digitalWrite(ledRed, LOW);
  digitalWrite(ledBlue, HIGH);
  digitalWrite(ledGreen, LOW);
  delay(100);
  digitalWrite(ledRed, LOW);
  digitalWrite(ledBlue, LOW);
  digitalWrite(ledGreen, HIGH);
  delay(100);
  // put your main code here, to run repeatedly:

}
