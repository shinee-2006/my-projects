# Adaptive Chassis Robot for Narrow Space Navigation

## Overview
This project demonstrates a four wheeled robotic platform with an adaptive chassis mechanism that automatically expands or contracts based on surrounding wall distances.
The robot is manually controlled via a web interface, while chassis adaptation operates autonomously.

## Key Features
- Automatic chassis width adjustment
- Ultrasonic based distance sensing
- Four wheel differential drive
- Independent manual and autonomous subsystems

## Hardware Used
- ESP32
- Ultrasonic sensors
- Servo motor
- L298 motor driver
- Four DC motors

## Software and Tools
- Arduino IDE
- ESP32 WebServer
- Embedded C++

## System Architecture
Ultrasonic sensors continuously measure lateral distances.
Based on sensor readings, the ESP32 controls a servo motor to adjust the chassis width.
Motion commands are handled independently through a web interface.

## How It Works
1. Ultrasonic sensors measure side distances
2. Distance values are compared against thresholds
3. Chassis expands or contracts automatically
4. User controls robot movement via web interface

## Demo
Add images or video demonstrating chassis adaptation.

## What I Learned
- Sensor based autonomous control
- Embedded decision making
- Mechanical and electronic integration
- Real time system coordination

## Future Improvements
- Add closed loop control for chassis positioning
- Integrate front obstacle avoidance
- Improve mechanical stability
