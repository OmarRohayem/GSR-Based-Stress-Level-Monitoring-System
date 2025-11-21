#include <EEPROM.h>
// Uncomment if using LCD
// #include <LiquidCrystal.h>
// LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int GSR = A0;

int sensorValue = 0;
int gsr_average = 0;
int stressThresholdHigh = 650; // High stress
int stressThresholdLow = 500;  // Calm

int eepromAddress = 0;

void setup() {
  Serial.begin(9600);
  delay(1000);

  // Save one baseline reading to EEPROM on startup
  gsr_average = getGsrAverage();
  EEPROM.put(eepromAddress, gsr_average);
}

void loop() {
  gsr_average = getGsrAverage();
  unsigned long timeStamp = millis();

  Serial.print("Time: ");
  Serial.print(timeStamp);
  Serial.print(" ms, GSR Avg: ");
  Serial.print(gsr_average);
  Serial.print(" --> ");

  // Interpret the result
  if (gsr_average > stressThresholdHigh) {
    Serial.println("High Stress Level Detected");
  } else if (gsr_average > stressThresholdLow) {
    Serial.println("Normal / Relaxed State");
  } else {
    Serial.println("Very Calm / Dry Skin");
  }

  delay(1000);  // 1 second between readings
}

int getGsrAverage() {
  long sum = 0;
  for (int i = 0; i < 10; i++) {
    sensorValue = analogRead(GSR);
    sum += sensorValue;
    delay(5);
  }
  return sum / 10;
}
