# 🔐 SecurePass — Console Password Manager

SecurePass is a lightweight, local-first Python console application designed to securely manage account credentials. Built as part of a Python Capstone project, it leverages core programming paradigms to solve a real-world problem: **password fatigue and security vulnerabilities due to credential reuse.**

---

## 🚀 Key Features

* **In-Memory Vaulting:** Employs an efficient data structure layer utilizing a list of structured dictionaries to manage login records smoothly.
* **Smart Password Generator (Innovation Feature):** Instantly creates high-entropy, 12-character passwords using alphanumeric characters and symbols if a custom password isn't provided.
* **Tabular Terminal UI (Enhanced UX):** Formats output using precision string padding rules to ensure perfectly aligned rows and headers.
* **Sandboxed Compatibility:** Optimized to run flawlessly in all local setups as well as strict, permission-locked online environments (like Programiz or OnlineGDB).

---

## 🛠️ Tech Stack & Concepts Demonstrated

* **Language:** Python 3.x
* **Primary Concepts:** * **String Manipulation:** Dynamic padding (`:<15`, `:<20`), data joining, and character pooling.
  * **Data Layouts:** Key-value pairs matching unique account credentials.
  * **Control Flow Logic:** Fail-safe validation loops, menu routing branches, and structured system exits.

---

## 📋 How It Works & Evaluation Rubric Mapping

1. **Option 1: Add a Password** * Captures the target application, account identifier, and password.
   * *Rubric Match:* Fulfills **Programming Logic** and triggers the **Innovation Feature** if you let it auto-generate a strong password string.
2. **Option 2: View Passwords**
   * Parses current runtime arrays and prints them in a clean visual table.
   * *Rubric Match:* Fulfills **User Experience** marks through deliberate alignment configurations.
3. **Option 3: Exit**
   * Gracefully terminates the terminal execution system loop.

---

## 💻 Setup and Usage Instructions

### Prerequisites
Make sure you have Python 3 installed on your system. 

### Running Locally
1. Clone this repository to your machine:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SecurePass-Manager.git](https://github.com/YOUR_USERNAME/SecurePass-Manager.git)
   
