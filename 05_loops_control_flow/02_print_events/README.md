# 🔢 First 20 Even Numbers

## 📘 Problem Statement

Write a Python program that prints the **first 20 even numbers** starting from 0.

> ⚠️ You must **use a loop** (like `for`) to solve this problem.  
> Do **not** use 20 `print()` statements manually.

---

## ▶️ Sample Output


0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38


## ✅ Python Code

**Save this code in a file like `even_numbers.py`:**

```python
# 📄 even_numbers.py
# This program prints the first 20 even numbers using a loop

def main():
    # Loop runs 20 times, from 0 to 19
    for i in range(20):
        even_number = i * 2
        print(even_number)

# This ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
💡 Explanation
Here's how the program works:

Loop Setup
The loop for i in range(20) runs 20 times (from i = 0 to i = 19).

Calculate Even Numbers
Inside the loop, we multiply the index i by 2 to get the even number:

makefile
Copy
Edit
i = 0 → 0 × 2 = 0  
i = 1 → 1 × 2 = 2  
i = 2 → 2 × 2 = 4  
...
Print Output
Each calculated even number is printed on a new line.

