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

    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.println(z);
  }
}
