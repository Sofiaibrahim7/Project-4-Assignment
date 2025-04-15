🔢 Divisors Finder — Python Program
🧠 Problem Statement
Write a function print_divisors(num) that takes a number as input and prints all of its divisors (all the numbers from 1 to num inclusive that can cleanly divide num, i.e., without leaving a remainder).

🧪 Solution
Function:
print_divisors(num):

This function takes a number num and prints all the numbers between 1 and num that can divide num evenly.

The function loops from 1 to num and checks if num % i == 0. If this condition is met, i is a divisor of num.

main():

The main() function prompts the user to input a number, then calls print_divisors(num) to display the divisors of the given number.

💻 Python Code
python

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:  # Check if 'i' divides 'num' without a remainder
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
🧪 Example Run:
mathematica

Enter a number: 12
Here are the divisors of 12
1
2
3
4
6
12
📌 Key Concepts
Looping: The program uses a for loop to iterate through the range of numbers from 1 to num.

Modulo Operation: The modulo operation (%) is used to check if a number is a divisor by ensuring there is no remainder.

