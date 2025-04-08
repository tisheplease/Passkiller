# **PASSKILLER: Password Security Toolkit**

PASSKILLER is a versatile password security toolkit designed to help users manage and test the strength of their passwords. It includes a password generator, password strength checker, hashing functionalities, and a brute force tool for cracking MD5 hashes using a dictionary attack.

### **Features**

1. **Password Generator**: 
   - Generate secure random passwords of a specified length using a combination of letters, digits, and special characters.

2. **Password Strength Checker**:
   - Evaluate the strength of a given password based on various criteria, including length, use of uppercase/lowercase letters, digits, and special characters.

3. **Password Hashing**:
   - Hash passwords using popular algorithms such as MD5, SHA-256, and bcrypt.

4. **Brute Force MD5 Hash Cracker**:
   - Attempt to crack MD5 password hashes using a dictionary-based brute force attack.

5. **Leak Database Check (In Development)**:
   - This feature is currently under development and will be available in future releases to check if a password has been exposed in known breaches.

6. **Exit Option**: 
   - Exit the program.

### **Requirements**

- Python 3.x
- `pyfiglet` library (for ASCII art)
- `termcolor` library (for colored output)
- `bcrypt` library (for bcrypt hashing)

### **Installation**

1. Clone the repository:

    ```bash
    git clone https://github.com/tisheplease/passkiller.git
    cd passkiller
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the program:

    ```bash
    python passkiller.py
    ```

### **Usage**

Once the program starts, you'll be presented with the following options:

1. **Generate Password**: Create a strong random password.
2. **Check Password Strength**: Evaluate the strength of an entered password.
3. **Hash Password**: Hash a password using MD5, SHA-256, or bcrypt.
4. **Brute Force MD5 Hash**: Attempt to crack an MD5 hash using a dictionary.
5. **Leak Database**: (Under development)
6. **Exit**: Exit the program.

### **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to your branch (`git push origin feature-branch`)
6. Create a pull request

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This software is intended for educational purposes only. Misuse of this tool for illegal activities is not supported or endorsed by the developers.
