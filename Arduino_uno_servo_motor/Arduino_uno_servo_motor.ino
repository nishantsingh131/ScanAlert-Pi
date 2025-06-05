#include <Servo.h>

Servo myServo;  // create servo object

void setup() {
  myServo.attach(9);  // attach servo signal wire to pin 9
}

void loop() {
  // sweep from 0 to 180 degrees
  for (int pos = 0; pos <= 180; pos += 1) {
    myServo.write(pos);    // set servo position
    delay(15);             // wait for servo to reach the position
  }
  // sweep back from 180 to 0 degrees
  for (int pos = 180; pos >= 0; pos -= 1) {
    myServo.write(pos);
    delay(15);
  }
}
