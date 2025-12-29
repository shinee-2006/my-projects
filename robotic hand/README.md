# Blynk Controlled Robotic Arm using ESP32

## Overview
This project implements a robotic arm controlled remotely through a mobile application.
Servo motors are used for arm joints and gripper control, while an L298 motor driver is used for base movement.

## Key Features
- Mobile app based control
- Multi servo joint actuation
- Real time user interaction
- Modular actuator control

## Hardware Used
- ESP32
- Servo motors
- L298 motor driver
- DC motor for base rotation
- External power supply

## Software and Tools
- Arduino IDE
- Blynk IoT platform
- Embedded C++

## System Architecture
User input is provided through joystick and slider widgets on the mobile application.
The ESP32 processes control signals and drives the corresponding servos and motors in real time.

## How It Works
1. User inputs commands via mobile application
2. ESP32 receives control data from the app
3. Servo motors and base motor are actuated
4. Arm movement responds immediately to user input

## Demo
Add video demonstrating arm movement and control.

## What I Learned
- Servo motor control techniques
- Human machine interface design
- Coordinated actuator control
- Mobile app based embedded control

## Future Improvements
- Add preset arm positions
- Implement smooth motion profiles
- Introduce safety limits and feedback
