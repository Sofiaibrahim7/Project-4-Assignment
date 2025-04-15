
# 🎲 Random Numbers Generator

## 📝 Problem Statement

Write a Python program that prints **10 random numbers** in the range of **1 to 100**.

Each time the program is run, it should generate a **different set of random numbers** using the `random.randint()` function.

---

## 🧪 Sample Output

Example run 1:

99 42 70 76 8 26 77 51 91 78

arduino
Copy
Edit

Example run 2:

17 63 91 24 3 85 40 60 98 12

yaml
Copy
Edit

Each time, the numbers will be different because we are using a random number generator.

---

## 🧠 Concepts Used

- **`random.randint(a, b)`**: Generates a random integer between `a` and `b` (inclusive).
- **`for` loop**: To repeat the action 10 times.
- **Variables**: To define number of outputs and range.

---

## 📜 Python Code

```python
import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1    # Minimum value for the random number
MAX_VALUE = 100  # Maximum value for the random number

def main():
    # Generate and print 10 random numbers in the range of 1 to 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

if __name__ == '__main__':
    main()
✅ How to Run
Save the file as app.py

Open terminal in the folder

Run the program using:

bash
Copy
Edit
python app.py
🏁 Output Example
Each time you run the file:

vbnet
Copy
Edit
You're going to see 10 random numbers between 1 and 100!
📌 Conclusion
This program is a simple demonstration of:

Generating random numbers

Using loops and functions in Python