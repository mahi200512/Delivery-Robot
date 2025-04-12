# Smart Delivery Robot 🤖📦

This is a Raspberry Pi–based self-driving delivery robot that can:
- Detect objects using sensors
- Stream camera feed
- Move autonomously using servo & motor
- Communicate locally via RPi Connect

## 🛠️ Components Used
- Raspberry Pi 3
- Servo Motor (SG90)
- IR Sensor (HW-201)
- Ultrasonic Sensor (HC-SR04)
- GY-521 Gyroscope
- Raspberry Pi Camera
- ESP-01 Wi-Fi Module (optional)
- Breadboard + Jumper Wires
- 5V Buzzer

## 🔌 Wiring Connections

| Component        | VCC  | GND  | Signal Pin |
|------------------|------|------|------------|
| IR Sensor        | 5V   | GND  | GPIO17     |
| Ultrasonic Trig  | 5V   | GND  | GPIO23     |
| Ultrasonic Echo  | 5V   | GND  | GPIO24     |
| Servo Motor      | 5V   | GND  | GPIO18     |
| GY-521 (SDA/SCL) | 3.3V | GND  | SDA: GPIO2, SCL: GPIO3 |
| Buzzer (Active)  | 5V   | GND  | GPIO12    |
| Pi Camera        | CSI Port |


<img width="191" alt="image" src="https://github.com/user-attachments/assets/08f797f5-f265-4fcf-b8a5-d5059b70a09f" />
![Screenshot 2025-04-04 144648](https://github.com/user-attachments/assets/d897dad9-4963-41f6-8de9-7f2a1c63e823)
## 💻 Installation

```bash
sudo apt update
sudo apt install python3-gpiozero python3-rpi.gpio python3-pip
python3 -m venv robot-env
source robot-env/bin/activate
pip install -r requirements.txt


