🔢 Even and Odd Number Checker — Python Program
🧠 Problem Statement
The goal is to print the numbers from 10 to 19, followed by whether each number is even or odd. For example:

python-repl

10 even
11 odd
12 even
...
🧪 Solution
Function:
main():

This function loops through numbers from 10 to 19.

It checks whether each number is odd or even using the is_odd() function.

The result is printed with the format number even/odd.

is_odd(value):

This function takes an integer value and returns True if the number is odd, otherwise False.

It uses the modulo operator to check if the remainder of the number when divided by 2 is 1 (which means it's odd).

💻 Python Code
python

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(f'{i} odd')
        else:
            print(f'{i} even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

if __name__ == '__main__':
    main()
🧪 Example Run:
Copy
Edit
10 even
11 odd
12 even
13 odd
14 even
15 odd
16 even
17 odd
18 even
19 odd
📌 Key Concepts
Looping: The program uses a for loop to iterate over numbers from 10 to 19.

Even/Odd Checking: The is_odd() function uses the modulo operation to determine if a number is odd.

