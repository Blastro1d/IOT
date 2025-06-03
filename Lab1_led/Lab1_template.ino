// // -------------------------------------------
// //
// //  Poject: Lab1_task1
// //  Group: Labduo 42
// //  Students: Ivash Yu en Dorus van den Akker
// //  Date: 2 june 2025
// //  ------------------------------------------

// #define OFF 0
// #define ON 1

// // put your setup code here
// void setup() {

//   // initialize digital pin LED_BUILTIN as an output.
//   pinMode(LED_BUILTIN, OUTPUT);

//   // initialize serial port and wait for port to open:
//   Serial.begin(9600);

//   // wait for serial port to connect. Needed for native USB port only
//   // while (!Serial) {} 
  
//   // // init digital IO pins
//   digitalWrite(LED_BUILTIN, LOW); 
// }


// // put your main code here
// void loop() {
//   digitalWrite(LED_BUILTIN, HIGH); 
//   Serial.println("Led on");
//   delay(1000);
//   digitalWrite(LED_BUILTIN, LOW); 
//   Serial.println("Led off");
//   delay(1000);

// }

unsigned long startMillis;
unsigned long currentMillis;
const unsigned long period = 1000;

arduino::String input; 
arduino::String status;
void setup() { 
  pinMode(LED_BUILTIN, OUTPUT);
	Serial.begin(115200); 
	Serial.setTimeout(1);
  
  startMillis = millis();
  status = "off";
  digitalWrite(LED_BUILTIN, LOW); 
} 
void loop() { 
  input = "";
  currentMillis = millis();
	if(Serial.available()) {
    input = Serial.readString();
  }
	if (input == "on") {
    digitalWrite(LED_BUILTIN, HIGH);
    status = "LED on";
    Serial.println(status);
  }
  else if (input == "off") {
    status = "LED off";
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println(status);
  }
  else if (input == "blink") {
    status = "LED blink";
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
    Serial.println(status);
  }
  else if (input == "status") {
    Serial.println(status);
  }
  else if (status == "LED blink") {
    if (currentMillis - startMillis >= period) {
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      startMillis = currentMillis;
    }
  }
} 
