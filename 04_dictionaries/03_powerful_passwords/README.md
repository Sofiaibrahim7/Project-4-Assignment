# 🔐 Hashed Password Login Checker

## 📝 Problem Statement

You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called `SHA256(...)`, something as simple as:


Write the `login(...)` function for a website that hashes their passwords. `login` should return `True` if an email's stored password hash in `stored_logins` is the same as the hash of `password_to_check`.

---

## ✅ Solution in Python

```python
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }
    
    print(login("example@gmail.com", stored_logins, "word"))         # False
    print(login("example@gmail.com", stored_logins, "password"))     # True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # False

    print(login("student@stanford.edu", stored_logins, "password"))  # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True

if __name__ == '__main__':
    main()

Write the `login(...)` function for a website that hashes their passwords. `login` should return `True` if an email's stored password hash in `stored_logins` is the same as the hash of `password_to_check`.

---

## ✅ Solution in Python

```python
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }
    
    print(login("example@gmail.com", stored_logins, "word"))         # False
    print(login("example@gmail.com", stored_logins, "password"))     # True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # False

    print(login("student@stanford.edu", stored_logins, "password"))  # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True

if __name__ == '__main__':
    main()

Write the `login(...)` function for a website that hashes their passwords. `login` should return `True` if an email's stored password hash in `stored_logins` is the same as the hash of `password_to_check`.

---

## ✅ Solution in Python

```python
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }
    
    print(login("example@gmail.com", stored_logins, "word"))         # False
    print(login("example@gmail.com", stored_logins, "password"))     # True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # False

    print(login("student@stanford.edu", stored_logins, "password"))  # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True

if __name__ == '__main__':
    main()

False
True
True
False
False
True
