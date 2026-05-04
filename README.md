# 🔐 Time-Pattern Based Smart Lock System (Raspberry Pi)

A secure electronic lock system that uses **time-based pattern authentication** instead of traditional PIN systems.

---

## 📌 Project Overview

This project implements a smart lock using:

- 🔢 **4x4 Matrix Keypad**
- 🧠 **Raspberry Pi (GPIO)**
- ⏱️ **Time-based authentication**
- 🔌 **Relay Module (Lock control)**
- 💡 **LED indicators**

Unlike normal locks, access is granted only when:
1. Correct **key sequence** is entered  
2. Correct **timing pattern** is followed  

---

## 🎯 Features

- 🔐 Dual authentication (pattern + timing)
- 🚫 Resistant to guessing attacks
- ⚡ Real-time key detection
- 💡 LED feedback system
- 🔌 Relay-based door unlocking
- 🧩 Low-cost implementation

---

## 🧠 How It Works

1. User enters pattern using keypad  
2. System records:
   - Key sequence (e.g., `1 → 5 → 9`)
   - Time intervals between presses  
3. Time is classified as:

| Time Interval | Type |
|--------------|------|
| < 0.7 sec | SHORT |
| 0.7 – 1.5 sec | MEDIUM |
| > 1.5 sec | LONG |

4. System compares input with stored pattern  

✔ If matched:
- Relay turns ON (Unlock)
- Green LED glows  

❌ If incorrect:
- Red LED glows  

---

## 🧩 Hardware Components

| Component | Description |
|----------|------------|
| Raspberry Pi | Main controller |
| Matrix Keypad | User input |
| Relay Module | Lock control |
| LEDs | Status indication |

---

## 🔌 GPIO Pin Configuration

| Component | Pin (BOARD) |
|----------|------------|
| Rows | 40, 38, 36, 32 |
| Columns | 37, 35, 33, 31 |
| Relay | 19 |
| Green LED | 11 |
| Red LED | 7 |

---

## ⚙️ Installation

### 1. Clone Repository

```git clone https://github.com/your-username/time-pattern-lock.git```
```cd time-pattern-lock```

## ⚙️ Installation
### 2. Install Dependencies
pip3 install RPi.GPIO

### 3. Run Program
python3 time_pattern_lock.py

## 🎮 Usage
- Run the script  
- Enter key sequence using keypad  
- Follow timing pattern  

### Example Pattern:
- Keys: 1 → 5 → 9  
- Timing: SHORT → LONG  

## 🧪 Output Example
Enter Pattern:
Pressed: 1
Pressed: 5
Pressed: 9

ACCESS GRANTED

## 📸 Project Images
- Hardware Setup  
- Relay Module  
- Keypad  
- Output  
- Access Granted  
- Access Denied  

## 🔄 System Workflow
User Input → Time Measurement → Pattern Matching → Access Decision → Output  

## 🔐 Security Advantages
- More secure than static PIN  
- Hard to replicate timing behavior  
- Adds behavioral authentication layer  

## ⚠️ Limitations
- Requires timing accuracy  
- Keypad wiring must be correct  
- Not suitable for beginners without calibration  

## 🚀 Future Enhancements
- RFID authentication  
- Fingerprint module  
- Mobile app control  
- Cloud-based logging  
- Multi-user system  

## 🎯 Applications
- Smart door locks  
- Secure lockers  
- Industrial access systems  
- IoT security systems  
