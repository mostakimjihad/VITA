#include <Servo.h>
Servo body, arm;
void setup() {

  Serial.begin(9600);
  body.attach(9); 
  arm.attach(10);  

  arm.write(180);
  delay(2000);
  body.write(90);
  delay(3000);
  
}

void loop() {

  while(Serial.available() == 0);
  char command = Serial.read();

  if(command == 'h'){
    arm.write(20);
    delay(300);
    arm.write(0);
    delay(300);
    arm.write(20);
    delay(300);
    arm.write(0);
    delay(300);
    arm.write(180);
  }
   if(command == 's'){
    arm.write(10);
    delay(1000);
    arm.write(180);
  }
  if(command == 'b'){
    body.write(30);
    delay(1000);
    body.write(90);
    delay(1000);
    body.write(0);
    delay(1000);
    body.write(90);
    delay(1000);    
  }
 
}
