# Add Two Numbers Program

## Description:
This program takes two integer inputs from the user and calculates their sum.

## Steps:
1. Prompt the user to enter the first number.
2. Convert the input to an integer.
3. Prompt the user to enter the second number.
4. Convert the input to an integer.
5. Calculate the sum.
6. Display the result.

## Code:
```python
def main():
    print("This program adds two numbers.")
    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))  
    total = num1 + num2  
    print("The total sum is:", total)  

if __name__ == '__main__':
    main()
