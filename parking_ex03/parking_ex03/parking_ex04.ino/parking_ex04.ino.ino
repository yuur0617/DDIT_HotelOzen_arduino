#include <unordered_map>

std::unordered_map<int, int> sensor_pins = {
  {A0, 0},
  {A1, 1},
  {A2, 2}
};

void setup() {
  Serial.begin(9600);
  for (auto const& pair : sensor_pins) {
    pinMode(pair.first, INPUT);
  }
}

void loop() {
  for (auto const& pair : sensor_pins) {
    int sensor_value = digitalRead(pair.first);
    int sensor_index = pair.second;
    Serial.print(sensor_value);
    Serial.print(" A0");
    Serial.println(sensor_index + 1);
  }
  delay(1000);
}
