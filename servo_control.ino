#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle nh;

String val;
char ctrl_val; //value for control

//Motor
const byte LEFT1 = 8;
const byte LEFT2 = 9;
const byte LEFT_PWM = 10;
const byte RIGHT1 = 7;
const byte RIGHT2 = 6;
const byte RIGHT_PWM = 5;
byte Speed = 100;
byte Speed_slow = 50;
void forward();
void stopp();

//set up subscriber
void message_cb( const std_msgs::UInt16& str_msg) {
  if (str_msg.data == 1) {
    forward();
  }
  else if (str_msg.data == 0) {
    stopp();
  }
}
ros::Subscriber<std_msgs::UInt16> sub("servo", message_cb);

void setup() {
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1000);

}
void forward() {
  digitalWrite(LEFT1, HIGH);
  digitalWrite(LEFT2, LOW);
  analogWrite(LEFT_PWM, Speed);
  digitalWrite(RIGHT1, LOW);
  digitalWrite(RIGHT2, HIGH);
  analogWrite(RIGHT_PWM, Speed);
}
void stopp() {
  digitalWrite(LEFT1, LOW);
  digitalWrite(LEFT2, LOW);
  digitalWrite(RIGHT1, LOW);
  digitalWrite(RIGHT2, LOW);
}
