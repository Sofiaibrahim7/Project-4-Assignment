# 📝 Assignment Solution - Division and Remainder Calculator

## 📌 Problem Statement
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

---

## 📚 Solution Explanation
The program follows these steps:

1. **Take Input:**  
   - Ask the user to enter two integers (`dividend` and `divisor`).
   - Convert input values into integers.

2. **Handle Errors:**  
   - If the divisor is `0`, show an error message and exit.  
   - If the input is not a valid integer, show an error message.

3. **Perform Division:**  
   - Calculate **quotient** using `//` (integer division).  
   - Calculate **remainder** using `%` (modulus operator).  

4. **Print the Result:**  
   - Display the quotient and remainder in a user-friendly format.

---

## 🖥 Python Code:
```python
def main():
    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        if divisor == 0:
            print("❌ Error: Division by zero is not allowed!")
            return

        quotient = dividend // divisor
        remainder = dividend % divisor

        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("❌ Error: Please enter valid integer numbers!")

if __name__ == '__main__':
    main()
```

---

## 🔢 How Division Works

### Formula:
```
Dividend = (Divisor × Quotient) + Remainder
```

### Example: `10 ÷ 3`
1. **Integer Division (`//`)**
   ```
   10 ÷ 3 = 3 (quotient)
   ```
2. **Multiply Quotient by Divisor**
   ```
   3 × 3 = 9
   ```
3. **Find Remainder**
   ```
   10 - 9 = 1 (remainder)
   ```
✅ **Final Answer:** `The result of this division is 3 with a remainder of 1`

### 📊 Examples:
| Dividend | Divisor | Quotient (`//`) | Remainder (`%`) |
|----------|--------|----------------|----------------|
| 10       | 3      | 3              | 1              |
| 15       | 4      | 3              | 3              |
| 22       | 7      | 3              | 1              |
| 19       | 5      | 3              | 4              |
| 50       | 6      | 8              | 2              |
| 7        | 2      | 3              | 1              |

---

## 🛠 Edge Cases
✅ **Dividing by 1:** `The result of 5 ÷ 1 is 5 with a remainder of 0`  
✅ **Dividing by itself:** `The result of 7 ÷ 7 is 1 with a remainder of 0`  
✅ **Dividing a smaller number by a larger number:** `The result of 2 ÷ 5 is 0 with a remainder of 2`  

---

## 🚀 How to Run
To run this program, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory where `app.py` is located.
3. Run the following command:
   ```
   python app.py
   ```
4. Enter two integer values when prompted.
5. See the result! 🎯

✅ **This solution correctly calculates the quotient and remainder and handles invalid inputs.** 🎯🚀

