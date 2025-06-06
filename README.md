````markdown
# ScanAlert-Pi 🚨🎥
An intelligent Raspberry Pi + Arduino-based system for smart object detection using a servo-mounted ultrasonic sensor. It captures images, sends email alerts, and activates LED + buzzer when an object is detected.

## 🔧 Features

- 🔁 Sweeping motion using servo motor (Arduino)
- 🧠 Object detection using HC-SR04 (Ultrasonic Sensor)
- 📸 Captures an image on detection using Raspberry Pi Camera
- 📧 Sends real-time email alert with captured image
- 🔊 Buzzer + LED alert system
- 🔗 Raspberry Pi and Arduino serial communication

## 🛠️ Hardware Components

|   Component                | Description / Notes                  | Quantity     |
| -------------------------- | ------------------------------------ | ------------ |
| Raspberry Pi               | Any model with GPIO & Camera support | 1            |
| Arduino UNO                | For controlling servo motor          | 1            |
| SG90 Micro Servo Motor     | Mounted with HC-SR04 for sweeping    | 1            |
| HC-SR04 Ultrasonic Sensor  | For distance measurement             | 1            |
| Raspberry Pi Camera Module | Used to capture image                | 1            |
| LED + Resistor (100Ω)      | Visual alert when object detected    | 1            |
| Buzzer                     | Audio alert                          | 1            |
| Breadboard + Jumper Wires  | For circuit connections              | As required  |
| USB Cable (Arduino to Pi)  | Serial communication                 | 1            |

## 📷 Demo Video

🎥 Watch the system in action:

<video src="iot_p_vd.mp4" controls width="600"></video>

---

## ⚙️ Setup Instructions

### Arduino

 Connect the servo to pin D6
 Connect the HC-SR04 sensor to pins D9 (TRIG) and D10 (ECHO)
 Upload `servo_sweep_detection.ino` sketch
 HC-SR04 detects object → sends "ALERT" to Raspberry Pi over Serial

### Raspberry Pi

 Connect the LED to GPIO17 (Physical pin 11) through 100Ω resistor
 Connect the buzzer to GPIO25 (Physical pin 22)
 Connect camera module and enable `libcamera`
 Clone the project and install dependencies:

```bash
sudo apt update
pip install yagmail
```

 Make sure your Gmail App Password is generated and added in the script
 Run the Python script:

```bash
python3 iotproject.py
```

---

## 🧪 How It Works

1. Arduino sweeps the servo back and forth.
2. HC-SR04 checks distance.
3. If object detected (e.g., <15 cm), it sends **"ALERT"** to Raspberry Pi.
4. Raspberry Pi:

    Lights up LED and buzzer
    Captures image via camera
    Sends an email with the photo attached
5. After sending, Pi replies with **"R"** (resume) to Arduino, and sweep continues.

---

## 🧠 Possible Enhancements

Object tracking with motor movement
Facial recognition before alerting
Logging detection timestamps to a file or database
Telegram or WhatsApp integration

---

## 📜 License

This project is licensed under the MIT License — feel free to use, modify, and share it.

---
