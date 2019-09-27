const int PushButton = 21;
const int Switch = 22;
const int JoyX = 25;
const int JoyY = 26;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PushButton, INPUT_PULLUP);
  pinMode(Switch, INPUT_PULLUP);
  pinMode(JoyX, INPUT);
  pinMode(JoyY, INPUT);
  
  digitalWrite(JoyX, LOW);
  digitalWrite(JoyY, LOW);
  
//  pinMode(JoyX, INPUT_PULLUP);
//  digitalWrite(JoyX, INPUT_PULLUP);
//  pinMode(JoyY, INPUT);
//  digitalWrite(JoyY, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int PushButtonState = digitalRead(PushButton);

  Serial.print("Button - ");
  Serial.print(PushButtonState);
  Serial.println(" ");

  int SwitchState = digitalRead(Switch);

  Serial.print("Switch - ");
  Serial.println(SwitchState);

  int JoyXState = analogRead(JoyX);

  Serial.print("joyX - ");
  Serial.println(JoyXState);

  int JoyYState = analogRead(JoyY);
  Serial.print("joyY - ");
  Serial.println(JoyYState);

//  Serial.println(PushButtonState + '--' + SwitchState + '--' + JoyXState + '--' + JoyYState);

  delay(1000);

}

//serial script ie.serial.send
//then you have a python script that you put in rpi that calls serial.receive
