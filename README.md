````markdown
# Password Strength Checker

## Internship ID
**CITS7218**

## Project Overview
Password Strength Checker is a Python-based cybersecurity project that analyzes passwords based on length, uppercase letters, lowercase letters, numbers, and special characters.

The project classifies passwords as **Weak, Medium, or Strong** based on the security checks they pass.

## Objectives
- To understand basic password security concepts.
- To analyze password complexity.
- To identify common password characteristics.
- To provide a simple password strength assessment.

## Features
- Password length checking
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Weak, Medium, and Strong classification

## Technologies Used
- Python
- Regular Expressions (`re`)

## How It Works
The program takes a password as input and performs multiple security checks. Each successful check increases the password score. Based on the final score, the program displays the password strength.

## How to Run

### 1. Install Python
Make sure Python 3 is installed.

### 2. Run the Program

```bash
python password_strength_checker.py
````

### 3. Enter a Test Password

Enter a test password when prompted. The program will analyze it and display the results.

## Sample Output

```text
Password Analysis
-----------------
Length: Good
Uppercase: Yes
Lowercase: Yes
Number: Yes
Special Character: Yes

Strength: STRONG
```

## Screenshots

### Weak Password

![Weak Password](screenshots/weak.png)

### Medium Password

![Medium Password](screenshots/medium.png)

### Strong Password

![Strong Password](screenshots/strong.png)

## Learning Outcomes

* Learned basic Python programming.
* Learned conditional statements and regular expressions.
* Understood basic password security concepts.
* Learned how to test and document a cybersecurity project.

## Future Improvements

* Graphical User Interface (GUI)
* Password entropy calculation
* Common password detection
* Secure password generator
* Detailed password scoring

## Disclaimer

This project is developed for educational and cybersecurity learning purposes.

```
```
