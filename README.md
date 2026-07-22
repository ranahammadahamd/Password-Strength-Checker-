# 🔐 SecurePass Analyzer

A professional Password Strength Checker developed as a Cyber Security Internship Project.

---

# 📌 Project Overview

SecurePass Analyzer evaluates the security of passwords using multiple security checks instead of simply checking their length.

It analyzes password complexity, estimates entropy, predicts crack time, detects common passwords, and provides recommendations to improve password security.

---

# 🚀 Features

### Password Length Check

Checks if the password has sufficient length.

---

### Uppercase Detection

Detects uppercase letters.

---

### Lowercase Detection

Detects lowercase letters.

---

### Number Detection

Checks for numeric digits.

---

### Special Character Detection

Detects symbols such as:

```
@
#
$
%
&
*
!
```

---

### Password Score

Calculates a security score out of **100**.

Example

```
Score : 87/100
```

---

### Password Strength

Classifies passwords as

- Weak
- Medium
- Strong
- Very Strong

---

###  Password Entropy

Calculates entropy in bits.

Example

```
Entropy : 86.42 bits
```

---

### Crack Time Estimation

Predicts approximate brute-force cracking time.

Example

```
Instantly
Minutes
Hours
Days
Months
Years
Centuries
```

---

### Common Password Detection

Detects passwords such as

```
password
123456
admin
qwerty
abc123
```

---

### Sequential Character Detection

Detects patterns like

```
abc
123
XYZ
```

---

### Repeated Character Detection

Detects repeated characters

```
aaaa
1111
$$$$
```

---

### Password Complexity

Displays

```
Poor
Average
Good
Very Good
Excellent
```

---

### Security Suggestions

Provides recommendations for stronger passwords.

Example

```
Increase password length.

Use uppercase letters.

Include symbols.

Avoid common passwords.
```

---

### Scan History

Every password analysis is automatically saved into

```
history.txt
```

---

# Project Structure

```
SecurePassAnalyzer/

│── main.py
│── password_checker.py
│── utils.py
│── common_passwords.txt
│── history.txt
│── README.md
│── requirements.txt
```

---

# 🛠 Technologies Used

- Python 3
- File Handling
- Object-Oriented Programming
- String Handling
- Math Library
- Datetime Module

---

# ▶ How to Run

Install Python 3.

Clone or download the project.

Run

```bash
python main.py
```

---

# 📸 Sample Output

```
======================================================
        PASSWORD SECURITY REPORT
======================================================

Length                : 14
Uppercase             : Yes
Lowercase             : Yes
Digits                : Yes
Symbols               : Yes

Score                 : 94/100

Strength              : VERY STRONG

Entropy               : 96.84 bits

Estimated Crack Time  : Centuries

Complexity            : Excellent

Security Suggestions

✔ Excellent! Your password follows good security practices.
```

---

# 🔮 Future Improvements

- GUI Version using Tkinter
- Dark Theme
- Password Generator
- Password Manager
- SHA-256 Hashing
- Have I Been Pwned API Integration
- Password Leak Detection
- PDF Report Export
- QR Code Login
- Multi-language Support

---

# 🎯 Learning Outcomes

This project demonstrates

- Password Security
- Cyber Security Fundamentals
- Secure Coding
- Input Validation
- String Processing
- OOP
- File Handling
- Risk Analysis

---

# 👨‍💻 Author

**RANA HAMMAD AHMAD**
Cyber Security Intern
2026

---

# 📄 License
This project was created for educational and internship purposes only.
