# 📏 Feet to Inches Converter

## 📌 Problem Statement
This Python program converts feet to inches using the formula:

\[
\text{inches} = \text{feet} \times 12
\]

Where:
- **Feet** (user input) is an imperial unit of measurement.
- **Inches** is the equivalent value after conversion.
- **12 inches** make up **1 foot**.

---

## 📌 Features of the Program
✅ **Allows multiple conversions** (User can enter multiple values)  
✅ **Ensures only non-negative values** (Prevents negative inputs)  
✅ **Displays inches with two decimal places** (Formatted output)  
✅ **Handles invalid input gracefully** (Prevents crashes)  
✅ **Exit option** (User can type `'exit'` anytime to stop)  
✅ **Colorful output** using `colorama` for better readability  

---

## 📌 How to Run the Program?
1. Install Python (if not already installed)  
2. Install the required package (colorama) by running:
   ```bash
   pip install colorama
   ```
3. Open **VS Code** or a terminal.
4. Save the Python file as **`app.py`**.
5. Run the program using the command:
   ```bash
   python app.py
   ```

---

## 📌 Code Implementation
```python
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Constant for conversion
INCHES_IN_FOOT = 12  

def main():
    while True:
        try:
            # User input
            feet = input(Fore.CYAN + "\nEnter number of feet (or type 'exit' to quit): ")

            # Exit condition
            if feet.lower() == 'exit':
                print(Fore.GREEN + "\nExiting the program. Goodbye! 🚀")
                break

            # Convert input to float
            feet = float(feet)

            # Validate input (feet should be positive)
            if feet < 0:
                print(Fore.RED + "❌ Error: Feet value must be a non-negative number!")
                continue

            # Convert feet to inches
            inches = feet * INCHES_IN_FOOT

            # Display output
            print(Fore.YELLOW + "\n📏 **Conversion Result** 📏")
            print(Fore.BLUE + f"🔹 Feet = {feet:.2f} ft")
            print(Fore.BLUE + f"🔹 Inches = {inches:.2f} inches ✨")

        except ValueError:
            print(Fore.RED + "❌ Invalid input! Please enter a valid number.")

# Standard Python entry point
if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```bash
Enter number of feet (or type 'exit' to quit): 5

📏 **Conversion Result** 📏
🔹 Feet = 5.00 ft
🔹 Inches = 60.00 inches ✨

Enter number of feet (or type 'exit' to quit): exit

Exiting the program. Goodbye! 🚀
```

---

### **🚀 Created by: Sofia Ibrahim**

