
const int limitSwitchPin =2;
const int stepPin = 3;
const int dirPin = 4;
const int enPin = 9;
int enA = 7;
int in1 = 6;
int in2 = 5;
int speed = 0;
bool stopMachine = false;
bool motorEnabled = false;
bool checkstop = false;
int stepperDirection = 1;
unsigned long previousMillis = 0;
const long interval = 50;
int timebt = 0;
// Define states for the state machine
enum State
{
  IDLE,
  RUN_DC_MOTOR,
  RUN_STEPPER_MOTOR,
};

State currentState = IDLE;
unsigned long previousMillisDCMotor = 0;
unsigned long previousMillisStepperMotor = 0;

void setup() {
  Serial.begin(9600);      // Serial Monitor on Arduino Mega
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW);
  pinMode(limitSwitchPin, INPUT_PULLUP);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

void loop() {
  int limitSwitchState = digitalRead(limitSwitchPin);
  Serial.println(speed);
  // Handle serial commands
  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "stopmachine")
    {
      analogWrite(enA, 0);
      digitalWrite(enPin, HIGH);
      timebt = 0;
      speed = 0;
    }
    else if (command == "slowdrill" || command == "fastdrill")
    {
      motorEnabled = true;
      speed = 0;
      timebt = 10;

      if (command == "slowdrill")
      {
        speed = 200;
        while (Serial.available() > 0) {
          char c = Serial.read();
        }
      }
      else if (command == "fastdrill")
      {
        speed = 255;
        while (Serial.available() > 0) {
          char c = Serial.read();
         }
      }

      runDCMotor(speed);
      
      }
  }
  currentState = RUN_STEPPER_MOTOR;
  // Run stepper motor based on state
  if (currentState == RUN_STEPPER_MOTOR)
  {
    runStepperMotor(timebt); // You may adjust the number of steps
    currentState = IDLE;
  }

  if (limitSwitchState == HIGH)
  {
   
    for (int m = 0; m < 5; m++)
    {
      if (checkstop == false)
      {
        for (int i = 0; i < 600; i++)
        {
          digitalWrite(dirPin, HIGH);
          digitalWrite(enPin, LOW);

          // Step the motor
          digitalWrite(stepPin, HIGH);
          delayMicroseconds(2000);
          digitalWrite(stepPin, LOW);
          delayMicroseconds(2000);
        }
      }
      if (Serial.available() > 0)
      {
        String command = Serial.readStringUntil('\n');
        command.trim();
        if (command == "stopmachine")
        {
          analogWrite(enA, 0);
          digitalWrite(enPin, HIGH);
          timebt = 0;
          checkstop = true;
          speed = 0;
        }
    }
  }
  //limitSwitchState =LOW;
  }
  }
void runDCMotor(int speed)
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, speed);
}
void runStepperMotor(int steps)
{
  digitalWrite(dirPin, LOW);
  digitalWrite(enPin, LOW);

  for (int i = 0; i < steps; i++)
  {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(16385);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(16385);
  }
}

  



