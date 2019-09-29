const int TreeButton = 0;
const int CarSwitch = 22;
const int WaveButton = 21;
const int LeafSwitch = 0;
const int WildSwitch = 0;
const int iterate = 0;

const int amp = 25;
const int shift = 26;
const int wildcardX = 0;
const int wildcardY = 0;

int TreeButtonState = 0;
int WaveButtonState = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TreeButton, INPUT_PULLUP);
  pinMode(CarSwitch, INPUT_PULLUP);
  pinMode(WaveButton, INPUT_PULLUP);
  pinMode(LeafSwitch, INPUT_PULLUP);
  pinMode(WildSwitch, INPUT_PULLUP);
  pinMode(iterate, INPUT_PULLUP);
  
  pinMode(amp, INPUT);
  pinMode(shift, INPUT);
  pinMode(wildcardX, INPUT);
  pinMode(wildcardY, INPUT);

  digitalWrite(amp, LOW);
  digitalWrite(shift, LOW);
  digitalWrite(wildcardX, LOW);
  digitalWrite(wildcardY, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (digitalRead(TreeButton) == HIGH) {
    TreeButtonState = !TreeButtonState;
  }
  Serial.print(!TreeButtonState);
  Serial.print("--");

  int CarSwitchState = digitalRead(CarSwitch);
  Serial.print(CarSwitchState);
  Serial.print("--");

  if (digitalRead(WaveButton) == LOW) {
    WaveButtonState = !WaveButtonState;
  }
  Serial.print(WaveButtonState);
  Serial.print("--");

  int LeafSwitchState = digitalRead(LeafSwitch);
  Serial.print(LeafSwitchState);
  Serial.print("--");

  int WildSwitchState = digitalRead(WildSwitch);
  Serial.print(WildSwitchState);
  Serial.print("--");

  int iterateState = digitalRead(iterate);
  Serial.print(iterateState);
  Serial.print("--");

  int ampState = analogRead(amp);
  Serial.print(ampState);
  Serial.print("--");

  int shiftState = analogRead(shift);
  Serial.print(shiftState);
  Serial.print("--");

  int wildcardXstate = analogRead(wildcardX);
  Serial.print(wildcardXstate);
  Serial.print("--");

  int wildcardYstate = analogRead(wildcardY);
  Serial.println(wildcardYstate);

  delay(1000);

}

//serial script ie.serial.send
//then you have a python script that you put in rpi that calls serial.receive
