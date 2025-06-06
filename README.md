# 🚨 ScanAlert-Pi  
An intelligent Raspberry Pi + Arduino-based system for smart object detection using a servo-mounted ultrasonic sensor. It captures images, sends email alerts, and activates LED + buzzer when an object is detected.

---

## 🔧 Features

- 🔁 Sweeping motion using servo motor (Arduino)
- 🧠 Object detection using HC-SR04 (Ultrasonic Sensor)
- 📸 Captures an image on detection using Raspberry Pi Camera
- 📧 Sends real-time email alert with captured image
- 🔊 Buzzer + LED alert system
- 🔗 Raspberry Pi and Arduino serial communication

---

## 🛠️ Hardware Components

| Component                  | Description / Notes                  | Quantity     |
|---------------------------|--------------------------------------|--------------|
| Raspberry Pi              | Any model with GPIO & Camera support | 1            |
| Arduino UNO               | For controlling servo motor          | 1            |
| SG90 Micro Servo Motor    | Mounted with HC-SR04 for sweeping    | 1            |
| HC-SR04 Ultrasonic Sensor | For distance measurement             | 1            |
| Raspberry Pi Camera       | Used to capture image                | 1            |
| LED + Resistor (100Ω)     | Visual alert when object detected    | 1            |
| Buzzer                    | Audio alert                          | 1            |
| Breadboard + Jumper Wires | For circuit connections              | As required  |
| USB Cable (Arduino to Pi) | Serial communication                 | 1            |

---

## 🎥 Watch the System in Action

[![Watch the video](https://img.youtube.com/vi/pLq_paAQXFs/0.jpg)](https://www.youtube.com/shorts/pLq_paAQXFs)

Click the image above to watch the project demo on YouTube.

---

## ⚙️ Setup Instructions

### 🔌 Arduino

- Connect the **servo motor** to pin **D6**
- Connect **HC-SR04** to **D9 (TRIG)** and **D10 (ECHO)**
- Upload the `servo_sweep_detection.ino` sketch
- On object detection, Arduino sends `"ALERT"` to Raspberry Pi over Serial

### 🐍 Raspberry Pi

- Connect **LED** to **GPIO17** (Physical Pin 11) via **100Ω resistor**
- Connect **buzzer** to **GPIO25** (Physical Pin 22)
- Connect and enable the **camera module** using `libcamera`
- Clone the project and install dependencies:

```bash
sudo apt update
pip install yagmail
```

- Set up Gmail App Password and insert it in the Python script
- Run the Python program:

```bash
python3 iotproject.py
```

---

## 🔄 How It Works

1. Arduino sweeps the servo motor.
2. HC-SR04 checks for nearby objects.
3. If an object is within 15 cm:
   - Arduino sends `"ALERT"` to the Raspberry Pi.
4. Raspberry Pi:
   - Lights up the LED
   - Activates the buzzer
   - Captures an image via the camera
   - Sends an email with the image attached
5. After sending, Pi replies with `"R"` to resume scanning.

---

## 💡 Possible Enhancements

- Object tracking with motor movement
- Facial recognition before alerting
- Logging detection timestamps to a file or database
- Telegram or WhatsApp integration for alerts

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and share it.

---
