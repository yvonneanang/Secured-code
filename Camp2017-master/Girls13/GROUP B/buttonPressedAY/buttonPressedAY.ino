int buttonPressed = LOW;
int ledRed = 13;
void setup() {
pinMode(7, INPUT);  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
 buttonPressed = digitalRead(7); // put your main code here, to run repeatedly:
Serial.println(buttonPressed);
if(buttonPressed == 1){
  digitalWrite(ledRed, HIGH);
  }
  if(buttonPressed ==0){
    digitalWrite(ledRed, LOW);
  }
}
