# Problem: Print Ones Digit

## Problem Statement

Write a function called `print_ones_digit` that takes an integer `num` as a parameter and prints its ones digit. Use the modulo (remainder) operator `%` to accomplish this task. Call the function from `main()`.

### Sample Run

Enter a number: 42 The ones digit is 2

python


## Solution

```python
def print_ones_digit(num):
    # Using modulo operator to find the ones digit
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))  # Prompt user for input
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()  # Execute main function
Explanation:
print_ones_digit(num) Function:

This function takes an integer num as an argument.

The ones digit is found using the modulo operation (num % 10).

The result is printed with the message: "The ones digit is".

main() Function:

The main() function prompts the user to enter a number.

The input is converted into an integer using int().

The function print_ones_digit() is called with the input number as the argument.

Example
Input:
css

Enter a number: 42
Output:
csharp
The ones digit is 2
Additional Information:
The modulo operator % is used to find the remainder of a division operation. In this case, num % 10 gives the last digit of the number.



