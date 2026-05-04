"""
Time-Pattern Based Smart Lock System
Author: Your Name

Description:
This project implements a secure smart lock system using:
- Matrix Keypad (4x4)
- Raspberry Pi GPIO
- Time-based pattern authentication

Authentication is based on:
1. Key sequence
2. Time intervals between key presses
"""

import RPi.GPIO as GPIO
import time

# ------------------ GPIO SETUP ------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# ------------------ KEYPAD CONFIG ------------------
keypad = [
    ['0','1','2','3'],
    ['4','5','6','7'],
    ['8','9','A','B'],
    ['C','D','E','F']
]

# Adjust pins according to your hardware
rows = [40, 38, 36, 32]
cols = [37, 35, 33, 31]

# ------------------ OUTPUT PINS ------------------
RELAY = 19
LED_GREEN = 11
LED_RED = 7

# ------------------ SETUP ------------------
for r in rows:
    GPIO.setup(r, GPIO.OUT)
    GPIO.output(r, 1)

for c in cols:
    GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(RELAY, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)

# ------------------ PASSWORD ------------------
correct_keys = ['1','5','9']
correct_times = ['SHORT','LONG']

# ------------------ TIME CLASSIFICATION ------------------
def classify_time(t):
    """
    Classifies time interval into SHORT, MEDIUM, LONG
    """
    if t < 0.7:
        return "SHORT"
    elif t < 1.5:
        return "MEDIUM"
    else:
        return "LONG"

# ------------------ KEYPAD SCANNING ------------------
def read_key():
    """
    Reads key from 4x4 matrix keypad
    """
    for i in range(4):
        GPIO.output(rows[i], 0)

        for j in range(4):
            if GPIO.input(cols[j]) == 0:
                time.sleep(0.05)  # debounce

                if GPIO.input(cols[j]) == 0:
                    key = keypad[i][j]

                    # Wait until key release
                    while GPIO.input(cols[j]) == 0:
                        pass

                    GPIO.output(rows[i], 1)
                    return key

        GPIO.output(rows[i], 1)

    return None

# ------------------ GET USER PATTERN ------------------
def get_pattern():
    """
    Captures key sequence and timing pattern
    """
    keys = []
    times = []
    prev_time = None

    print("\nEnter Pattern:")

    while len(keys) < len(correct_keys):
        key = read_key()

        if key:
            now = time.time()
            print("Pressed:", key)
            keys.append(key)

            if prev_time is not None:
                diff = now - prev_time
                times.append(classify_time(diff))

            prev_time = now
            time.sleep(0.3)  # avoid multiple detection

    return keys, times

# ------------------ AUTHENTICATION ------------------
def check_pattern(user_keys, user_times):
    """
    Checks if entered pattern matches stored pattern
    """
    return user_keys == correct_keys and user_times == correct_times

# ------------------ MAIN LOOP ------------------
try:
    while True:
        user_keys, user_times = get_pattern()

        print("Keys:", user_keys)
        print("Times:", user_times)

        if check_pattern(user_keys, user_times):
            print("ACCESS GRANTED")
            GPIO.output(RELAY, 1)
            GPIO.output(LED_GREEN, 1)

            time.sleep(3)

            GPIO.output(RELAY, 0)
            GPIO.output(LED_GREEN, 0)

        else:
            print("ACCESS DENIED")
            GPIO.output(LED_RED, 1)

            time.sleep(2)

            GPIO.output(LED_RED, 0)

except KeyboardInterrupt:
    print("\nExiting Program...")
    GPIO.cleanup()
