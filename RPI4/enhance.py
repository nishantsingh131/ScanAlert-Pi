nishant@raspberrypi:~ $ cat iotproject.py o
import RPi.GPIO as GPIO
import time
import subprocess
import yagmail
import os

# === GPIO Pin Setup ===
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24
LED_PIN = 5
BUZZER_PIN = 25

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# === Distance Measurement Function ===
def measure_distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance_cm = (time_elapsed * 34300) / 2
    return distance_cm

# === Image Capture Function ===
def capture_image_libcamera(filename="captured.jpg"):
    subprocess.run(["libcamera-still", "-o", filename, "--nopreview"], check=True)

# === Email Sending Function ===
def send_email_with_attachment(sender, app_password, receiver, subject, message, attachment_path):
    yag = yagmail.SMTP(user=sender, password=app_password)
    yag.send(
        to=receiver,
        subject=subject,
        contents=message,
        attachments=attachment_path
    )
    print("📧 Email sent successfully!")

# === Main Function ===
if __name__ == '__main__':
    try:
        image_sent = False  # To avoid sending multiple emails rapidly

        while True:
            dist = measure_distance()
            print(f"Measured Distance = {dist:.1f} cm")

            if dist < 10.0:
                GPIO.output(LED_PIN, GPIO.HIGH)
                GPIO.output(BUZZER_PIN, GPIO.HIGH)

                if not image_sent:
                    print("📸 Object detected! Capturing image and sending email...")

                    # Capture image
                    image_file = "captured.jpg"
                    capture_image_libcamera(image_file)

                    # Send email
                    sender_email = "nishantsingh2jan1998@gmail.com"
                    app_password = "rooh lcrd byqw wuab"
                    receiver_email = "nishantkumarsingh131@gmail.com"
                    subject = "Captured Image from Raspberry Pi"
                    message = "Hi, this is the captured image attached."
                    send_email_with_attachment(sender_email, app_password, receiver_email, subject, message, image_file)

                    # Remove image after sending
                    if os.path.exists(image_file):
                        os.remove(image_file)
                        print("🗑️ Temporary image file removed.")

                    image_sent = True  # Mark as sent

            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                GPIO.output(BUZZER_PIN, GPIO.LOW)
                image_sent = False  # Reset flag when object is gone

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Program stopped by user.")
        GPIO.cleanup()