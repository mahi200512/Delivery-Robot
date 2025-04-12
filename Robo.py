import RPi.GPIO as GPIO
import time

# GPIO Pin Assignments
IR_SENSOR_PIN = 17   # IR Sensor (Pin 11)
BUZZER_PIN = 12      # Buzzer (Pin 32)
SERVO_PIN = 18       # Servo Motor (Pin 12)
TRIG_PIN = 27        # HC-SR04 TRIG (Pin 13)
ECHO_PIN = 23        # HC-SR04 ECHO (Pin 16) (via Voltage Divider)

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # IR Sensor as Input
GPIO.setup(BUZZER_PIN, GPIO.OUT)    # Buzzer as Output
GPIO.setup(TRIG_PIN, GPIO.OUT)      # HC-SR04 Trigger
GPIO.setup(ECHO_PIN, GPIO.IN)       # HC-SR04 Echo
GPIO.setup(SERVO_PIN, GPIO.OUT)     # Servo as Output

# Initialize Servo
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
servo.start(7.5)  # Center position (90°)

def measure_distance():
    """Measure distance using HC-SR04 ultrasonic sensor."""
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10µs pulse
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()  # Start timing

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()  # Stop timing

    # Time difference between start and stop
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Convert to cm
    return distance

def rotate_servo(angle):
    """Rotate servo to a specific angle."""
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.7)
    servo.ChangeDutyCycle(0)  # Stop the servo

def scan_and_turn():
    """Scan in 30° increments and turn if object is detected."""
    for angle in range(0, 181, 30):  # Sweep from 0° to 180° in 30° steps
        print(f"🚦 Checking {angle}°...")
        rotate_servo(angle)  # Move servo to the angle
        time.sleep(0.5)  # Wait for movement
        distance = measure_distance()

        print(f"📏 Distance at {angle}°: {distance:.2f} cm")

        if distance > 20:  # If path is clear, stop rotating
            print(f"✅ Path clear at {angle}°! Moving in this direction.")
            return
        
    print("🚫 No clear path! Staying in position.")
    rotate_servo(90)  # Reset to center if no clear path

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance:.2f} cm")

        if distance < 20:  # If object is detected
            print("⚠️ Object Detected! Buzzer ON ⚠️")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn Buzzer ON
            time.sleep(1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn Buzzer OFF
            
            scan_and_turn()  # Scan and move accordingly

        time.sleep(0.2)  # Small delay

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    GPIO.cleanup()
