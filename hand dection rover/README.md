# Gesture Controlled Rover using ESP32 and Computer Vision

## Overview
This project implements a four wheeled rover that is controlled using hand gestures captured through a webcam.
A computer vision based hand detection model runs on a PC and converts recognized gestures into motion commands that are transmitted to an ESP32 for real time control.

## Key Features
- Hand gesture based control
- Four wheel differential drive
- Web based command communication
- Modular separation of perception and embedded control

## Hardware Used
- ESP32
- L298 motor driver
- DC motors and rover chassis
- External power supply

## Software and Tools
- Python
- OpenCV
- MediaPipe
- Arduino IDE
- ESP32 WebServer

## System Architecture
Hand gesture recognition is performed on the PC using a computer vision pipeline.
Recognized gestures are mapped to motion commands and sent to the ESP32 via HTTP requests.
The ESP32 interprets the commands and drives the motors using differential drive logic.

## How It Works
1. Webcam captures hand movements
2. Hand landmarks are detected and gestures classified
3. Corresponding motion commands are generated
4. ESP32 controls the rover motors accordingly

## Demo
Add video or images of the rover in operation.

## What I Learned
- Integration of machine learning with embedded systems
- Real time computer vision processing
- Wireless communication using HTTP
- Differential drive motor control

## Future Improvements
- Add gesture confidence filtering
- Implement speed control
- Improve robustness under varying lighting conditions
