# Automatic Irrigation System using ESP8266

## Overview
This project automates irrigation by monitoring soil moisture, temperature, and humidity.
Based on sensor readings, a water pump is automatically controlled and system data is displayed on a mobile application.

## Key Features
- Automatic irrigation based on soil condition
- Real time environmental monitoring
- Remote data visualization
- Threshold based control logic

## Hardware Used
- ESP8266
- Soil moisture sensor
- DHT11 temperature and humidity sensor
- Relay module
- Water pump

## Software and Tools
- Arduino IDE
- Blynk IoT platform

## System Architecture
Sensor data is collected by the ESP8266 and processed locally.
Control decisions are made using predefined thresholds.
Pump operation is controlled through a relay and live data is sent to the mobile application.

## How It Works
1. Sensors collect soil and environmental data
2. Data is evaluated against threshold values
3. Water pump is activated or deactivated
4. Sensor values are displayed on the dashboard

## Demo
Add screenshots or video of system operation.

## What I Learned
- Designing IoT based automation systems
- Sensor interfacing and calibration
- Embedded control logic implementation

## Future Improvements
- Add adaptive irrigation scheduling
- Integrate weather based control
- Improve energy efficiency
