import <Servo.h>

Servo base
Servo shoulder
Servo arm
Servo wrist
servo_pin_1 = 4
servo_pin_2 = 5
servo_pin_3 = 6
servo_pin_4 = 7

void setup() {
  // put your setup code here, to run once:
  base.attach(servo_pin_1);
  shoulder.attach(servo_pin_2);
  arm.attach(servo_pin_3);
  wrist.attach(servo_pin_4);

}

void loop() {
  // put your main code here, to run repeatedly:
  base.write(60);
  shoulder.write(70);
  arm..write(90);
  wrist.write(30);
}
