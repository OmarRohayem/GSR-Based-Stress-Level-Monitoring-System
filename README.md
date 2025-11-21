# GSR-Based Stress Level Monitoring System

**Author:** Omar Rohayem  
**Date:** May 07, 2025  
**Institution:** Arab Academy for Science and Technology

---

## 1. Abstract
This project presents a simple and affordable Galvanic Skin Response (GSR) monitoring system using an Arduino microcontroller. The system detects physiological stress by measuring changes in skin conductivity triggered by sweat gland activity. It interprets stress levels in real-time and displays the results via a computer interface, providing a foundation for biofeedback systems and mental health monitoring.

## 2. Introduction
In modern health and research domains, stress monitoring is critical as stress impacts physical well-being, productivity, and long-term health. A non-invasive method to detect stress is measuring Galvanic Skin Response (GSR). This phenomenon involves measuring changes in skin conductivity controlled by the sympathetic nervous system.

## 3. System Overview
The primary purpose of this project is to measure physiological stress, analyze the sensor signal using microcontroller logic, and display the user's stress level dynamically.

### Key Components:
* **GSR Sensor Module:** Detects skin resistance.
* **Arduino UNO/Nano:** Reads and processes analog sensor data.
* **Serial Monitor/Plotter:** Displays timestamped readings and visualizes skin resistance changes over time.
* **LCD Display (Optional):** For standalone output.

## 4. Methodology

### 4.1 Working Principle
The GSR sensor outputs an analog voltage corresponding to skin resistance, which the Arduino reads through an analog pin (A0). To reduce signal noise, the system averages a small number of readings (default: 10).

### 4.2 Stress Classification
The firmware compares the averaged value against defined thresholds to classify the user's state into three categories:
1.  **Very Calm / Dry Skin** (< Low Threshold)
2.  **Normal / Relaxed State** (Between Thresholds)
3.  **High Stress Level Detected** (> High Threshold)

## 5. Hardware Implementation

### Wiring Diagram
The system requires the following connections between the GSR Module and the Arduino:

| GSR Module Pin | Arduino Pin |
| :--- | :--- |
| **VCC** | 5V |
| **GND** | GND |
| **OUT** | A0 |

### Electrode Placement
The electrodes should be attached to two fingers (e.g., index and middle) or the palm/wrist using conductive straps.

## 6. Software Implementation (Python)
To provide advanced analysis beyond the standard Arduino Serial Plotter, this project includes a custom Python script located in the `/software` directory.

### Features:
* **Real-time Data Logging:** Captures GSR sensor data via Serial communication (UART).
* **Data Visualization:** Uses `matplotlib` to create live graphs of skin resistance.
* **Data Storage:** Automatically saves session data to a CSV file for later analysis.

## 7. Usage Guide

### Step 1: Assembly & Upload
Assemble the hardware using the wiring table above. Open the Arduino IDE, upload the provided firmware code, and connect to the correct COM port.

### Step 2: Calibration
Sit calmly for 10 seconds to allow the system to set baseline thresholds based on current skin resistance.

### Step 3: Monitoring
Open the **Serial Monitor** (9600 baud) to view live readings or run the Python script for advanced plotting.

### Step 4: Simulation
To test the system, you can simulate stress by clenching your fist, holding your breath, or performing mental math.

## 8. Applications
This system has potential applications in various fields:
* **Biofeedback Therapy:** For managing stress and anxiety.
* **UX Studies:** Tracking emotions during user testing.
* **Lie Detection:** Prototyping polygraph-style systems.
* **Interactive Installations:** Utilizing biosignals for art or control.

## 9. Future Improvements
* **Data Logging:** Saving sessions to an SD card.
* **Wireless Connectivity:** Sending data to mobile or cloud via Bluetooth/WiFi.
* **Machine Learning:** Applying ML algorithms for precise emotion recognition.

---
*Reference: Rohayem, O. (2025). GSR-Based Stress Level Monitoring System Using Arduino. Project Report.*
