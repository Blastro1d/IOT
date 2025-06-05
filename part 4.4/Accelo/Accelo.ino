// // -------------------------------------------
// //
// //  Poject: Lab1_task1
// //  Group: Labduo 42
// //  Students: Ivash Yu en Dorus van den Akker
// //  Date: 2 june 2025
// //  ------------------------------------------

#include <Arduino_LSM6DS3.h>

float x, y, z;

void setup() {
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);


    /*
      According to https://docs.arduino.cc/tutorials/nano-33-iot/imu-gyroscope/
      the accelerometer has a resolution of 0,122 mg.
      Following this we decided to report the values with an accuracy of 3 decimals.
      As using more decimals wouldn't result in more accurate values.
    */

    Serial.print(x, 3);
    Serial.print('\t');
    Serial.print(y, 3);
    Serial.print('\t');
    Serial.println(z, 3);
  }
}
